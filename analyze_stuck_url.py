#!/usr/bin/env python3
"""Analyze the URL where scraping gets stuck"""

import asyncio
import sys
from pathlib import Path
from urllib.parse import quote, unquote

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper

async def analyze_stuck_url():
    """Analyze the problematic URL"""
    
    # The URL from the progress file
    stuck_url = "https://developer.apple.com/documentation/accelerate/bnnsgraphcontextsetworkspaceallocationcallback(_:_:_:_:_:)"
    
    print("🔍 Analyzing stuck URL")
    print(f"Original URL: {stuck_url}")
    print()
    
    # Create scraper
    scraper = AppleJSONDocumentationScraper("accelerate", "Accelerate")
    
    # Test URL conversions
    print("1️⃣ Testing URL conversions:")
    json_url = scraper._convert_doc_url_to_json_url(stuck_url)
    print(f"JSON URL: {json_url}")
    
    # Check if the URL has special characters
    print("\n2️⃣ URL encoding analysis:")
    print(f"Has parentheses: {'(' in stuck_url}")
    print(f"Has colons: {':' in stuck_url}")
    print(f"URL-encoded version: {quote(stuck_url, safe=':/')}")
    
    # Test the JSON URL directly
    print("\n3️⃣ Testing JSON URL fetch:")
    async with scraper:
        try:
            # Try fetching the JSON
            result = await scraper.fetch_page_with_etag(json_url, use_etag=False)
            if result:
                content, etag = result
                print(f"✅ Successfully fetched JSON ({len(content)} bytes)")
                
                # Parse and check content
                import json
                data = json.loads(content)
                
                # Check for identifiers
                identifier_count = 0
                for section in ['topicSections', 'relationshipsSections', 'seeAlsoSections']:
                    if section in data:
                        for item in data[section]:
                            if 'identifiers' in item:
                                identifier_count += len(item['identifiers'])
                
                print(f"Found {identifier_count} total identifiers to process")
                
                # Check if there are any problematic identifiers
                all_identifiers = []
                for section in ['topicSections', 'relationshipsSections', 'seeAlsoSections']:
                    if section in data:
                        for item in data[section]:
                            if 'identifiers' in item:
                                all_identifiers.extend(item['identifiers'])
                
                print(f"\n4️⃣ Checking identifiers:")
                for i, identifier in enumerate(all_identifiers[:5]):
                    print(f"  {i+1}. {identifier}")
                    
                if len(all_identifiers) > 5:
                    print(f"  ... and {len(all_identifiers) - 5} more")
                
            else:
                print("❌ Failed to fetch JSON")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    # Check if the issue is with the file path
    print("\n5️⃣ Checking file path generation:")
    data = {'title': 'Test', 'symbol_kind': 'func'}
    file_path = scraper._get_organized_file_path(stuck_url, data)
    print(f"Would save to: {file_path}")
    print(f"Path valid: {not any(c in str(file_path) for c in '<>:"|?*')}")

async def main():
    await analyze_stuck_url()

if __name__ == "__main__":
    asyncio.run(main())