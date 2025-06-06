#!/usr/bin/env python3
"""Check for any remaining Note duplication in markdown files."""

import os
import re
from pathlib import Path

def check_file_for_duplication(filepath):
    """Check if a file has the Note duplication pattern."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern 1: Blockquote followed by plain text
        pattern1 = r'> \*\*Note\*\*:\s*([^\n]+(?:\n> [^\n]+)*)\n\n\s*\1'
        
        # Pattern 2: Multi-line Note pattern
        pattern2 = r'> \*\*Note\*\*:\s*(.+?)(?=\n\n).*?\n\n\s*\1'
        
        if re.search(pattern1, content, re.MULTILINE | re.DOTALL) or \
           re.search(pattern2, content, re.MULTILINE | re.DOTALL):
            return True
            
        # Also check for partial duplication (where the duplicated part might be slightly different)
        note_match = re.search(r'> \*\*Note\*\*:\s*(.+?)(?=\n\n)', content, re.MULTILINE | re.DOTALL)
        if note_match:
            note_content = note_match.group(1).strip()
            # Clean up the note content
            clean_note = re.sub(r'^> ', '', note_content, flags=re.MULTILINE).strip()
            
            # Look for the same content appearing after the blockquote
            after_note = content[note_match.end():]
            if clean_note in after_note[:500]:  # Check within 500 chars after the note
                # Make sure it's not part of another blockquote
                lines_after = after_note[:500].split('\n')
                for i, line in enumerate(lines_after):
                    if clean_note in line and not line.strip().startswith('>'):
                        return True
        
        return False
        
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

def main():
    """Find all files with Note duplication."""
    docs_dir = Path('documentation')
    duplicated_files = []
    
    # Walk through all markdown files
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if check_file_for_duplication(filepath):
                    duplicated_files.append(filepath)
    
    print(f"\nTotal files checked: {sum(1 for _ in Path('documentation').rglob('*.md'))}")
    print(f"Files with Note duplication: {len(duplicated_files)}")
    
    if duplicated_files:
        print("\nFiles still containing duplication:")
        for file in duplicated_files[:20]:  # Show first 20
            print(f"  {file}")
        if len(duplicated_files) > 20:
            print(f"  ... and {len(duplicated_files) - 20} more")
    else:
        print("\n✅ No files with Note duplication found!")

if __name__ == '__main__':
    main()