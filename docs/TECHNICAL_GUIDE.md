# Technical Implementation Guide

## 🏗️ System Architecture

### Core Components
1. **Scraping System** - Complete (278,778 files scraped)
   - Uses Apple's JSON API endpoints
   - ETag-based change detection
   - SHA-256 content hashing
   
2. **Embedding System** - Production Ready
   - OpenAI text-embedding-3-small (1536 dimensions)
   - ChromaDB vector storage
   - Incremental processing with checkpointing
   
3. **Document Processing**
   - Automatic splitting for files >30KB
   - Preserves context with title inclusion
   - Chunk metadata tracking

## ⚠️ CRITICAL: ChromaDB Configuration

### Always Use OpenAI Embeddings

**IMPORTANT**: Always use OpenAI embeddings (text-embedding-3-small, 1536 dimensions) for consistency:

```python
from chromadb.utils import embedding_functions

# ALWAYS use this configuration:
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv('OPENAI_API_KEY'),
    model_name='text-embedding-3-small',
    dimensions=1536
)

# When creating collections:
collection = client.create_collection(
    name='apple_docs_{framework}',
    embedding_function=embedding_function
)

# When getting collections (must specify same function):
collection = client.get_collection(
    name='apple_docs_{framework}',
    embedding_function=embedding_function
)
```

**Why this is critical:**
- ChromaDB's default creates 384-dimension vectors
- OpenAI creates 1536-dimension vectors
- Mixing causes: `Collection expecting embedding with dimension of 1536, got 384`
- Once created with one function, cannot query with another

## 📄 Document Splitting Strategy

### Implementation
```python
def split_by_headers(content: str, max_tokens: int = 7000) -> List[str]:
    """Split large markdown documents by ## headers"""
    # Check if splitting needed
    if len(content) > 30000:  # ~7.5k tokens
        chunks = split_by_headers(content, max_tokens=7000)
        # Each chunk gets its own embedding with metadata
```

### Key Points
- **Source files are NEVER modified** - splitting only during embedding
- **Threshold**: Files >30KB (approximately 7,500 tokens)
- **Method**: Split by `## ` headers while preserving title
- **Impact**: 70 files → ~230 chunks (0.03% of total)
- **Benefits**: 
  - Saves 17GB storage (4GB vs 21GB)
  - Better search relevance
  - Focused context for LLMs

### Chunk Metadata Structure
```python
{
    "framework": "HomeKit",
    "api_name": "mtrattributeidtype",
    "file_path": "documentation/HomeKit/mtrattributeidtype.md",
    "file_size": 461235,
    "chunk_index": 0,
    "total_chunks": 3,
    "chunk_hash": "abc123..."
}
```

## 🔧 ChromaDB Best Practices

### 1. Collection Name Requirements
- Must be 3-63 characters long
- Start/end with alphanumeric characters
- Only alphanumeric, underscores, or hyphens
- Pattern: `apple_docs_{framework}`

### 2. Document ID Format
```python
# Standard document
"{filename}_{path_hash}_{content_hash}"

# Chunked document
"{filename}_{path_hash}_{content_hash}_part{index}"
```

### 3. Metadata Constraints
- Keys must be strings
- Values: strings, integers, floats, or booleans
- No nested objects or arrays
- Reserved keys: `id`, `embedding`, `document`

### 4. Batch Processing
- Maximum batch size: 41,666 documents
- Recommended: 100-1000 per batch
- Cost calculation per batch for safety

## 🔄 Incremental Update System

### Change Detection Flow
1. **Check ETag** (HTTP header from Apple)
2. **Compare content hash** if ETag unavailable
3. **Process only changed files**
4. **Update hash registry**

### Hash Storage Structure
```
.hashes/
├── {framework}_hashes.json  # Per-framework hashes
├── embedding_hashes.json    # Processed file tracking
└── embedding_checkpoint.json # Resume capability
```

### Deletion Handling
```python
# Pattern matching for chunks
base_pattern = f"{file.stem}_{path_hash}_"
old_ids = [id for id in existing_ids 
          if id.startswith(base_pattern) and id not in new_ids]
```

## 🚀 Production Configuration

### Environment Variables
```bash
# Required
OPENAI_API_KEY="sk-..."

# Optional (with defaults)
MAX_EMBEDDING_COST="10.00"      # Hard cost limit
MAX_FILES_TO_EMBED="300000"      # File limit
MAX_FILE_SIZE_MB="10"            # Individual file size
MAX_TOKENS_PER_DOC="8000"        # Before splitting
OPENAI_RPM="3000"                # Rate limit
EMBEDDING_BATCH_SIZE="100"       # Batch size
```

### Rate Limiting
- Default: 3000 requests/minute
- Automatic backoff on 429 errors
- Configurable delays between requests

### Error Recovery
1. **Network errors**: Exponential backoff with retry
2. **API errors**: Checkpoint and resume
3. **File errors**: Skip and log, continue processing
4. **Cost overrun**: Immediate abort with checkpoint

## 📊 Vector Search Integration

### Query Example
```python
results = collection.query(
    query_texts=["how to implement SwiftUI navigation"],
    n_results=5,
    where={"framework": "SwiftUI"}  # Optional filtering
)

# Results structure
{
    'ids': [['doc_id_1', 'doc_id_2', ...]],
    'distances': [[0.572, 0.981, ...]],  # Lower = more similar
    'metadatas': [[{...}, {...}, ...]],
    'documents': [['full text', ...]]
}
```

### Distance Interpretation
- `< 0.8`: Highly relevant
- `0.8-1.2`: Relevant
- `> 1.2`: Somewhat related
- `> 1.5`: Likely not relevant

## 🎯 Optimization Tips

1. **Memory Management**
   - Process frameworks separately
   - Clear collections between large batches
   - Monitor vectorstore size

2. **Performance Tuning**
   - Adjust batch size based on document size
   - Use framework-specific collections for faster queries
   - Enable where-clause filtering when possible

3. **Storage Efficiency**
   - Regular cleanup of orphaned embeddings
   - Compress backup files
   - Monitor chunk distribution

## 🐛 Common Issues and Solutions

### "Dimension Mismatch" Error
**Cause**: Mixing ChromaDB default with OpenAI embeddings  
**Solution**: Always specify OpenAI embedding function

### "Collection Name Invalid" Error
**Cause**: Framework name with special characters  
**Solution**: Use `validate_collection_name()` function

### "Rate Limit Exceeded" Error
**Cause**: Too many OpenAI API requests  
**Solution**: Reduce batch size or increase delays

### "Checkpoint Resume Failed"
**Cause**: Corrupted checkpoint file  
**Solution**: Delete checkpoint and restart (safe with hash tracking)