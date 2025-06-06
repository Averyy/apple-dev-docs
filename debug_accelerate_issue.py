#!/usr/bin/env python3
"""
Debug why Accelerate scraping stops at 1508 files
"""

import asyncio
import httpx
import json

async def check_problematic_url():
    """Check the URL where scraping stops"""
    
    url = "https://developer.apple.com/tutorials/data/documentation/accelerate/sharing-texture-data-between-the-model-io-framework-and-the-vimage-library.json"
    
    print(f"🔍 Checking URL: {url}")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    print(f"✅ Successfully fetched JSON")
    
    # Check all sections for potential issues
    sections_to_check = [
        'topicSections',
        'relationshipsSections', 
        'seeAlsoSections',
        'diffAvailability',
        'variants',
        'references'
    ]
    
    total_identifiers = 0
    problematic_identifiers = []
    
    for section_name in sections_to_check:
        if section_name in data:
            if section_name == 'references':
                # References is a dict
                print(f"\n📚 {section_name}: {len(data[section_name])} items")
                # Check for any unusual references
                for ref_id, ref_data in data[section_name].items():
                    if 'accelerate' not in ref_id.lower() and 'com.apple' not in ref_id:
                        problematic_identifiers.append(f"Reference: {ref_id}")
            elif isinstance(data[section_name], list):
                print(f"\n📋 {section_name}: {len(data[section_name])} sections")
                for section in data[section_name]:
                    if 'identifiers' in section:
                        ids = section.get('identifiers', [])
                        total_identifiers += len(ids)
                        print(f"   - {section.get('title', 'Unknown')}: {len(ids)} identifiers")
                        
                        # Check for problematic identifiers
                        for identifier in ids:
                            if identifier.startswith('doc://'):
                                # Check if it would be skipped by the current logic
                                if 'accelerate' not in identifier.lower():
                                    problematic_identifiers.append(identifier)
    
    print(f"\n📊 Total identifiers found: {total_identifiers}")
    
    if problematic_identifiers:
        print(f"\n⚠️  Found {len(problematic_identifiers)} identifiers that might be skipped:")
        for pid in problematic_identifiers[:10]:
            print(f"   - {pid}")
    else:
        print("\n✅ No obviously problematic identifiers found")
    
    # Check if there are any circular references
    current_url = data.get('identifier', {}).get('url', '')
    if current_url:
        print(f"\n🔄 Current page identifier: {current_url}")
        
        # Check if any references point back to this page
        circular_refs = []
        for section_name in sections_to_check:
            if section_name in data and isinstance(data[section_name], list):
                for section in data[section_name]:
                    if 'identifiers' in section:
                        for identifier in section['identifiers']:
                            if current_url in identifier:
                                circular_refs.append(identifier)
        
        if circular_refs:
            print(f"⚠️  Found {len(circular_refs)} potential circular references!")
        else:
            print("✅ No circular references detected")

if __name__ == "__main__":
    asyncio.run(check_problematic_url())