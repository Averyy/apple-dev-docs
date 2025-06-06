#!/usr/bin/env python3
"""
Debug why scraper hangs at specific URLs
"""

import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

async def debug_specific_url():
    """Debug the specific URL where scraping stops"""
    
    # The problematic URL
    doc_url = "https://developer.apple.com/documentation/accelerate/sharing-texture-data-between-the-model-io-framework-and-the-vimage-library"
    json_url = "https://developer.apple.com/tutorials/data/documentation/accelerate/sharing-texture-data-between-the-model-io-framework-and-the-vimage-library.json"
    
    print(f"🔍 Testing specific URL processing...")
    print(f"📄 Doc URL: {doc_url}")
    print(f"📦 JSON URL: {json_url}")
    
    # Create scraper and use as context manager
    scraper = AppleJSONDocumentationScraper("accelerate", "Accelerate")
    
    async with scraper:
        # Test 1: Fetch the JSON data
        print("\n1️⃣ Fetching JSON data...")
        try:
            result = await scraper.fetch_page_with_etag(json_url, use_etag=False)
            if not result:
                print("❌ Failed to fetch JSON")
                return
                
            response_text, etag = result
            data = json.loads(response_text)
            print(f"✅ Successfully fetched JSON ({len(response_text)} bytes)")
            
            # Check sections
            sections_to_check = [
                'topicSections',
                'relationshipsSections', 
                'seeAlsoSections',
                'diffAvailability',
                'variants',
                'primaryContentSections'
            ]
            
            for section in sections_to_check:
                if section in data:
                    if isinstance(data[section], list):
                        print(f"  - {section}: {len(data[section])} items")
                    else:
                        print(f"  - {section}: present")
                        
        except Exception as e:
            print(f"❌ Error fetching JSON: {e}")
            import traceback
            traceback.print_exc()
            return
        
        # Test 2: Extract and process identifiers
        print("\n2️⃣ Processing identifiers...")
        all_identifiers = []
        
        for section_name in ['topicSections', 'relationshipsSections', 'seeAlsoSections']:
            if section_name in data and isinstance(data[section_name], list):
                for section in data[section_name]:
                    if 'identifiers' in section:
                        identifiers = section.get('identifiers', [])
                        all_identifiers.extend(identifiers)
                        print(f"  - {section.get('title', 'Unknown')}: {len(identifiers)} identifiers")
        
        print(f"\nTotal identifiers: {len(all_identifiers)}")
        
        # Test 3: Check if identifiers would cause issues
        print("\n3️⃣ Checking identifier processing...")
        problematic = []
        
        for identifier in all_identifiers[:10]:  # Check first 10
            print(f"\n  Identifier: {identifier}")
            
            # Simulate the processing logic
            if identifier.startswith('doc://'):
                try:
                    # Process like the scraper does
                    path = identifier.replace('doc://', '')
                    if '/documentation/' in path:
                        parts = path.split('/documentation/', 1)
                        if len(parts) == 2:
                            path = parts[1]
                            print(f"    → Path: {path}")
                            
                            # Check case sensitivity
                            path_lower = path.lower()
                            if not path_lower.startswith("accelerate/"):
                                print(f"    ⚠️  Would be skipped (doesn't start with accelerate/)")
                                problematic.append(identifier)
                            else:
                                print(f"    ✅ Would be processed")
                except Exception as e:
                    print(f"    ❌ Error processing: {e}")
                    problematic.append(identifier)
        
        if problematic:
            print(f"\n⚠️  Found {len(problematic)} problematic identifiers")
        
        # Test 4: Check for infinite loops
        print("\n4️⃣ Checking for potential infinite loops...")
        
        # Track how many times each URL appears
        url_counts = {}
        for identifier in all_identifiers:
            if identifier in url_counts:
                url_counts[identifier] += 1
            else:
                url_counts[identifier] = 1
        
        duplicates = [(url, count) for url, count in url_counts.items() if count > 1]
        if duplicates:
            print(f"⚠️  Found {len(duplicates)} duplicate identifiers:")
            for url, count in duplicates[:5]:
                print(f"  - {url} appears {count} times")
        else:
            print("✅ No duplicate identifiers")
        
        # Test 5: Check processed URLs set
        print("\n5️⃣ Checking scraper state...")
        print(f"  - Discovered URLs: {len(scraper.discovered_urls)}")
        print(f"  - Processed URLs: {len(scraper.processed_urls)}")
        
        # Check if this URL is already processed
        if json_url in scraper.processed_urls:
            print(f"  ⚠️  JSON URL already in processed set!")
        if doc_url in scraper.processed_urls:
            print(f"  ⚠️  Doc URL already in processed set!")

async def check_next_urls():
    """Check what happens after the problematic URL"""
    print("\n🔎 Checking subsequent URLs...")
    
    scraper = AppleJSONDocumentationScraper("accelerate", "Accelerate")
    
    async with scraper:
        # Get the data from the problematic URL
        json_url = "https://developer.apple.com/tutorials/data/documentation/accelerate/sharing-texture-data-between-the-model-io-framework-and-the-vimage-library.json"
        
        result = await scraper.fetch_page_with_etag(json_url, use_etag=False)
        if not result:
            print("❌ Failed to fetch JSON")
            return
            
        response_text, etag = result
        data = json.loads(response_text)
        
        # Get all identifiers that would be processed next
        next_urls = []
        
        for section in data.get('topicSections', []):
            for identifier in section.get('identifiers', []):
                if identifier.startswith('doc://') and 'accelerate' in identifier.lower():
                    # Convert to JSON URL
                    path = identifier.replace('doc://', '')
                    if '/documentation/' in path:
                        parts = path.split('/documentation/', 1)
                        if len(parts) == 2:
                            path = parts[1].lower()
                            json_url = f"https://developer.apple.com/tutorials/data/documentation/{path}.json"
                            next_urls.append(json_url)
        
        print(f"\nFound {len(next_urls)} URLs that would be processed next:")
        for url in next_urls[:5]:
            print(f"  - {url}")
        
        # Try fetching the first one
        if next_urls:
            print(f"\n🧪 Testing first next URL...")
            try:
                test_result = await scraper.fetch_page_with_etag(next_urls[0], use_etag=False)
                if test_result:
                    print("✅ Successfully fetched next URL")
                else:
                    print("❌ Failed to fetch next URL")
            except Exception as e:
                print(f"❌ Error fetching next URL: {e}")

async def main():
    """Run all debug tests"""
    print("🐛 ACCELERATE SCRAPER DEBUG")
    print("=" * 60)
    
    await debug_specific_url()
    await check_next_urls()
    
    print("\n✅ Debug complete")

if __name__ == "__main__":
    asyncio.run(main())