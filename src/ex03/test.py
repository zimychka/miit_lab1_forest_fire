#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
    }
    
    url = "https://finance.yahoo.com/quote/MSFT/financials/"
    
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if we got the actual page or a blocked page
        title = soup.find('title')
        if title and 'financials' in title.text.lower():
            print("Success! Got the financials page")
            print(f"Title: {title.text}")
            
            # Look for financial data
            tables = soup.find_all('table')
            print(f"Number of tables found: {len(tables)}")
            
        else:
            print("Page loaded but might be blocked or redirected")
            print(f"Title: {title.text if title else 'No title'}")
            
    else:
        print(f"Failed to access page. Status: {response.status_code}")

if __name__ == "__main__":
    main()