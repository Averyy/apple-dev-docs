#!/usr/bin/env python3
"""Check the status of all scraped frameworks"""

from pathlib import Path
import json

def check_all_frameworks():
    """Check status of all frameworks"""
    doc_dir = Path("documentation")
    
    completed = []
    incomplete = []
    no_progress = []
    
    for framework_dir in sorted(doc_dir.iterdir()):
        if not framework_dir.is_dir():
            continue
            
        framework_id = framework_dir.name
        progress_file = framework_dir / "scraping_progress.txt"
        md_files = list(framework_dir.glob("*.md"))
        
        if progress_file.exists():
            content = progress_file.read_text()
            if "Completed scraping" in content:
                # Extract stats
                lines = content.split('\n')
                scraped = 0
                skipped = 0
                failed = 0
                for line in lines:
                    if "Total pages scraped:" in line:
                        scraped = int(line.split(":")[1].strip())
                    elif "Pages skipped" in line:
                        skipped = int(line.split(":")[1].strip())
                    elif "Pages failed" in line:
                        failed = int(line.split(":")[1].strip())
                
                completed.append({
                    'framework': framework_id,
                    'scraped': scraped,
                    'skipped': skipped,
                    'failed': failed,
                    'files': len(md_files)
                })
            else:
                # Extract progress info
                scraped = 0
                if "Progress:" in content:
                    for line in content.split('\n'):
                        if "Progress:" in line:
                            parts = line.split()
                            for i, part in enumerate(parts):
                                if part == "scraped,":
                                    scraped = int(parts[i-1])
                                    break
                
                incomplete.append({
                    'framework': framework_id,
                    'scraped': scraped,
                    'files': len(md_files),
                    'last_line': content.split('\n')[1] if len(content.split('\n')) > 1 else ""
                })
        else:
            if md_files:
                no_progress.append({
                    'framework': framework_id,
                    'files': len(md_files)
                })
    
    # Print summary
    print("🍎 APPLE DOCUMENTATION SCRAPING STATUS REPORT")
    print("=" * 60)
    
    print(f"\n✅ COMPLETED FRAMEWORKS: {len(completed)}")
    total_scraped = sum(f['scraped'] for f in completed)
    total_skipped = sum(f['skipped'] for f in completed)
    print(f"Total pages: {total_scraped} scraped, {total_skipped} skipped")
    print("\nFramework                    Scraped  Skipped  Failed  Files")
    print("-" * 60)
    for f in sorted(completed, key=lambda x: x['scraped'], reverse=True)[:10]:
        print(f"{f['framework']:<28} {f['scraped']:>7} {f['skipped']:>8} {f['failed']:>7} {f['files']:>6}")
    if len(completed) > 10:
        print(f"... and {len(completed) - 10} more completed frameworks")
    
    print(f"\n⚠️  INCOMPLETE FRAMEWORKS: {len(incomplete)}")
    if incomplete:
        print("\nFramework                    Scraped  Files  Status")
        print("-" * 60)
        for f in sorted(incomplete, key=lambda x: x['scraped'], reverse=True)[:10]:
            last_url = f['last_line'].split(': ')[-1] if ': ' in f['last_line'] else ''
            if len(last_url) > 40:
                last_url = '...' + last_url[-37:]
            print(f"{f['framework']:<28} {f['scraped']:>7} {f['files']:>6}  {last_url}")
        if len(incomplete) > 10:
            print(f"... and {len(incomplete) - 10} more incomplete frameworks")
    
    print(f"\n❓ NO PROGRESS FILE: {len(no_progress)}")
    if no_progress:
        print("These have files but no progress tracking:")
        for f in no_progress[:5]:
            print(f"  - {f['framework']} ({f['files']} files)")
    
    # Save detailed report
    report = {
        'completed': completed,
        'incomplete': incomplete,
        'no_progress': no_progress,
        'summary': {
            'total_frameworks': len(completed) + len(incomplete) + len(no_progress),
            'completed': len(completed),
            'incomplete': len(incomplete),
            'no_progress': len(no_progress),
            'total_pages_scraped': total_scraped,
            'total_pages_skipped': total_skipped
        }
    }
    
    with open('scraping_status_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Detailed report saved to: scraping_status_report.json")

if __name__ == "__main__":
    check_all_frameworks()