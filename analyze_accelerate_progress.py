#!/usr/bin/env python3
"""
Analyze Accelerate scraping progress
"""

import json
from pathlib import Path

def analyze_progress():
    """Analyze what's been scraped in Accelerate"""
    
    print("🔍 Analyzing Accelerate framework scraping progress...")
    print("=" * 60)
    
    # Count files
    doc_dir = Path("documentation/Accelerate")
    if not doc_dir.exists():
        print("❌ No Accelerate documentation found")
        return
    
    # Get all markdown files
    md_files = list(doc_dir.rglob("*.md"))
    print(f"\n📊 Total files scraped: {len(md_files)}")
    
    # Analyze directory structure
    subdirs = {}
    for file in md_files:
        # Get relative path
        rel_path = file.relative_to(doc_dir)
        parts = rel_path.parts
        
        if len(parts) > 1:
            # Has subdirectory
            subdir = parts[0]
            subdirs[subdir] = subdirs.get(subdir, 0) + 1
    
    # Sort by count
    sorted_dirs = sorted(subdirs.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n📁 Top subdirectories by file count:")
    for subdir, count in sorted_dirs[:20]:
        print(f"  - {subdir}: {count} files")
    
    # Check main framework JSON to estimate total
    framework_json = Path("documentation/Accelerate/Accelerate.json")
    
    # Recent files
    print(f"\n🕐 Most recently created files:")
    recent_files = sorted(md_files, key=lambda x: x.stat().st_mtime, reverse=True)[:10]
    for file in recent_files:
        rel_path = file.relative_to(doc_dir)
        print(f"  - {rel_path}")
    
    # Check if we're still missing major sections
    print(f"\n🔍 Checking major sections from framework page...")
    framework_md = doc_dir / "Accelerate.md"
    if framework_md.exists():
        content = framework_md.read_text()
        
        # Look for major sections
        major_sections = [
            "BNNS", "vImage", "vDSP", "BLAS", "LAPACK", 
            "Sparse", "LinearAlgebra", "simd"
        ]
        
        for section in major_sections:
            section_lower = section.lower()
            section_dir = doc_dir / section_lower
            
            if section_dir.exists():
                count = len(list(section_dir.rglob("*.md")))
                print(f"  ✅ {section}: {count} files")
            else:
                # Check if files exist without subdirectory
                count = len([f for f in md_files if section_lower in str(f).lower()])
                if count > 0:
                    print(f"  ⚠️  {section}: {count} files (not in subdirectory)")
                else:
                    print(f"  ❌ {section}: Missing or not found")

if __name__ == "__main__":
    analyze_progress()