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
            if result:
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
            else:
                print("❌ Failed to fetch JSON")
                return
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
    
    # Test 4: Try to scrape and save
    print("\n4️⃣ Testing scrape and save...")
    try:
        scraped = await scraper._scrape_and_save_url(doc_url)
        if scraped:
            print("✅ Successfully scraped and saved")
        else:
            print("❌ Failed to scrape and save")
    except Exception as e:
        print(f"❌ Error during scrape: {e}")
        import traceback
        traceback.print_exc()
    
    # Test 5: Check for infinite loops
    print("\n5️⃣ Checking for potential infinite loops...")
    
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

async def test_memory_usage():
    """Test if it's a memory issue"""
    print("\n🧠 Testing memory usage...")
    
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    print(f"Initial memory: {initial_memory:.2f} MB")
    
    scraper = AppleJSONDocumentationScraper("accelerate", "Accelerate")
    
    # Simulate processing many URLs
    print("Simulating URL processing...")
    for i in range(100):
        url = f"https://developer.apple.com/documentation/accelerate/test{i}"
        scraper.discovered_urls.add(url)
        scraper.processed_urls.add(url)
        
        if i % 20 == 0:
            current_memory = process.memory_info().rss / 1024 / 1024
            print(f"  After {i} URLs: {current_memory:.2f} MB (+{current_memory - initial_memory:.2f} MB)")
    
    # Check if cleanup helps
    print("\nTesting cleanup...")
    scraper._cleanup_url_caches()
    
    final_memory = process.memory_info().rss / 1024 / 1024
    print(f"After cleanup: {final_memory:.2f} MB")

async def main():
    """Run all debug tests"""
    print("🐛 ACCELERATE SCRAPER DEBUG")
    print("=" * 60)
    
    await debug_specific_url()
    await test_memory_usage()
    
    print("\n✅ Debug complete")

if __name__ == "__main__":
    asyncio.run(main())