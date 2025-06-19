# TODO: Improve Embeddings for Better Search Quality

## Overview

This document outlines improvements to make during the next re-embedding of the Apple documentation. These changes would significantly improve search quality, especially for partial matches and camelCase APIs.

## 1. Dual CamelCase Embedding

### Problem
- Currently documents are embedded with camelCase intact (e.g., "UITableView")
- Queries for "table" or "table view" have poor vector similarity
- We search with both split and non-split versions, but only embed documents one way

### Solution
Embed each document chunk TWICE:
1. Original: "UITableView is a class that displays..."
2. Split: "UI Table View is a class that displays..."

### Implementation
```python
def create_embedding_variants(content, metadata):
    """Create multiple versions of content for better matching"""
    variants = [content]  # Original
    
    # Extract camelCase terms from the content
    api_name = metadata.get('api_name', '')
    
    # If API name is camelCase, create split version
    if has_camelcase(api_name):
        split_name = split_camelcase(api_name)  # UITableView -> UI Table View
        split_content = content.replace(api_name, split_name)
        variants.append(split_content)
    
    # Also handle camelCase in the content itself
    camelcase_terms = extract_camelcase_terms(content)
    if camelcase_terms:
        split_content = content
        for term in camelcase_terms:
            split_content = split_content.replace(term, split_camelcase(term))
        variants.append(split_content)
    
    return variants
```

## 2. Enhanced Metadata in Embeddings

### Current State
We embed the markdown content but may not include all searchable metadata in the embedded text.

### Improvement
Prepend key metadata to the embedded content:
```python
def create_enhanced_content(content, metadata):
    """Add searchable metadata to content"""
    parts = []
    
    # Add API name prominently
    if metadata.get('api_name'):
        parts.append(f"API: {metadata['api_name']}")
    
    # Add framework
    if metadata.get('framework'):
        parts.append(f"Framework: {metadata['framework']}")
    
    # Add method signatures or key terms
    if metadata.get('type') == 'method':
        parts.append("Method Function")
    elif metadata.get('type') == 'property':
        parts.append("Property Attribute")
    
    # Add the actual content
    parts.append(content)
    
    return "\n".join(parts)
```

## 3. Chunk Size Optimization

### Current State
Unknown current chunk size and overlap strategy.

### Recommendations
- Use 512-1024 token chunks (not too small, not too large)
- 20-30% overlap between chunks
- Keep semantic boundaries (don't split mid-sentence)

## 4. Include Alternative Names

### Add Common Variations
For each API, include common variations in the embedded text:
- Abbreviations: "ViewController" → also include "VC"
- Natural language: "UIButton" → also include "button control"
- Common typos: "TextField" → also include "TextFeild" (common typo)

### Implementation
```python
COMMON_VARIATIONS = {
    'viewcontroller': ['vc', 'view controller'],
    'navigationcontroller': ['nav controller', 'navigation'],
    'tableview': ['table', 'table view'],
    'textfield': ['text field', 'text input'],
    'imageview': ['image view', 'image'],
}

def add_variations(content, api_name):
    """Add common variations for better matching"""
    api_lower = api_name.lower()
    variations = COMMON_VARIATIONS.get(api_lower, [])
    
    if variations:
        # Add as hidden searchable text
        variation_text = f"Also known as: {', '.join(variations)}"
        return f"{content}\n\n{variation_text}"
    return content
```

## 5. Better Handling of Code Samples

### Problem
Code samples might dominate embeddings with syntax rather than concepts.

### Solution
- Extract and summarize code samples
- Embed the summary alongside the code
- Weight descriptive text higher than code

## 6. Platform-Specific Embeddings

### Current State
Same embedding regardless of platform.

### Improvement
For APIs available on multiple platforms, create platform-specific contexts:
```python
if 'ios' in platforms:
    variants.append(f"iOS: {content}")
if 'macos' in platforms:
    variants.append(f"macOS: {content}")
```

## 7. Hierarchical Context

### Include Parent Context
For nested APIs like `AsyncImagePhase.Failure`, include parent context:
```python
if '.' in api_name:
    parent, child = api_name.rsplit('.', 1)
    enhanced_content = f"Parent: {parent}\nChild: {child}\n{content}"
```

## 8. Testing Strategy

### Before Re-embedding
1. Create a test set of problematic queries:
   - Single words: "table", "button", "view"
   - Partial matches: "nav", "ctrl", "img"
   - Typos: "tabel", "navigtion"
   - Natural language: "table view controller"

2. Record current performance metrics

### After Re-embedding
1. Run same test set
2. Compare metrics
3. Ensure no regression on exact matches

## 9. Implementation Order

1. **Phase 1**: Dual camelCase embedding (biggest impact)
2. **Phase 2**: Enhanced metadata prepending
3. **Phase 3**: Common variations and abbreviations
4. **Phase 4**: Other optimizations

## 10. Cost Considerations

### Estimates
- Current: ~340,000 documents
- With dual camelCase: ~680,000 embeddings
- With all improvements: ~1,000,000 embeddings

### Cost Optimization
- Only apply dual embedding to documents with camelCase APIs
- Skip very short documents
- Batch API calls efficiently

## 11. Backwards Compatibility

Ensure new embedding strategy:
- Maintains same collection schema
- Works with existing search code
- Can be rolled back if needed

## Example: Full Enhancement

Original document:
```markdown
# UITableView
A view that displays data in rows.
```

Enhanced embeddings:
1. "API: UITableView Framework: UIKit A view that displays data in rows. Also known as: table view, table"
2. "API: UI Table View Framework: UIKit A view that displays data in rows. Also known as: table view, table"

This would make searches for "table", "table view", or "UITableView" all find this document with high relevance.

## Notes

- This requires a full re-scrape and re-embed
- Estimated time: 12-24 hours
- Estimated cost: ~$50-100 for OpenAI embeddings
- Would significantly improve search quality for partial matches
- Should maintain current performance for exact matches