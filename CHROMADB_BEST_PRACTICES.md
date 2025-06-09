# ChromaDB Best Practices and Edge Case Handling

Based on Context7 documentation and extensive testing, here are the critical edge cases and best practices for using ChromaDB in production.

## 1. Collection Name Limits and Valid Characters

**Requirements:**
- Must be 3-63 characters long
- Must start and end with alphanumeric characters
- Can only contain alphanumeric characters, underscores, or hyphens
- No spaces or special characters allowed

**Edge Cases:**
- Framework names with periods (e.g., "SwiftUI.Button") need sanitization
- Very long framework names need truncation
- Special characters must be replaced with underscores

**Solution:**
```python
# Implemented in chromadb_utils.py
def sanitize_collection_name(name: str) -> str:
    # Replace invalid chars, ensure proper start/end, handle length
    # See implementation for details
```

## 2. Maximum Document Size Limits

**Limits:**
- Recommended: 5000 bytes per document (not characters!)
- UTF-8 encoding can make multi-byte characters exceed limits

**Edge Cases:**
- Documents with emojis or non-ASCII characters
- Very large API documentation pages
- Truncation at UTF-8 boundaries

**Solution:**
```python
def truncate_document(document: str, max_size: int = 5000) -> str:
    # Properly handles UTF-8 encoding and word boundaries
    # See implementation for details
```

## 3. Batch Size Limitations

**Limits:**
- Conservative limit: 1000 documents per batch
- ChromaDB may have internal limits around 5000

**Edge Cases:**
- Large batch operations failing silently
- Memory issues with very large batches

**Solution:**
- Use batches of 100 for embedding generation (OpenAI rate limits)
- Use batches of 1000 for ChromaDB operations
- Implement sub-batching for extra safety

## 4. ID Collision Handling

**Requirements:**
- IDs must be unique within a collection
- Maximum ID length: 64 characters

**Edge Cases:**
- Running the same script multiple times
- Updating existing documents
- Hash collisions (though unlikely with SHA-256)

**Solution:**
```python
def generate_document_id(source: str, chunk_index: int = 0) -> str:
    # Use content-based hashing for consistency
    # Include chunk index for multi-chunk documents
    id_source = f"{source}:chunk_{chunk_index}"
    return hashlib.sha256(id_source.encode()).hexdigest()[:32]
```

## 5. Metadata Size Limits

**Limits:**
- Approximately 40KB per metadata object
- Must be JSON-serializable

**Edge Cases:**
- Very long file paths
- Large file sizes exceeding int32 range
- Non-serializable Python objects

**Solution:**
```python
def sanitize_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]:
    # Truncate strings, prioritize important fields
    # Remove non-essential fields if too large
    # See implementation for details
```

## 6. Concurrent Access Issues

**ChromaDB uses SQLite by default:**
- SQLite has limited concurrent write support
- "database is locked" errors are common

**Solutions:**
1. Implement retry logic with exponential backoff
2. Use single-writer pattern
3. Consider using ChromaDB's client-server mode for production
4. Add proper error handling and logging

```python
if "database is locked" in str(error):
    time.sleep(2)  # Wait before retry
    # Retry operation
```

## 7. Data Persistence Guarantees

**Concerns:**
- Data may not be immediately persisted
- Client crashes could lose data

**Solutions:**
1. Verify persistence after operations
2. Recreate client to force flush
3. Check document counts match expectations
4. Implement checkpointing for large operations

```python
# Force persistence
del chroma_client

# Verify with new client
verify_client = chromadb.PersistentClient(path=path)
verify_count = verify_client.get_collection(name).count()
```

## 8. Embedding Dimension Validation

**Requirements:**
- All embeddings in a collection must have the same dimensions
- Dimensions must match the configured embedding model

**Edge Cases:**
- Mixing embedding models
- Partial embedding generation failures
- Zero vectors for failed embeddings

**Solution:**
```python
def validate_embeddings(embeddings: List[List[float]], expected_dim: int) -> bool:
    # Check consistency and validity
    # See implementation for details
```

## 9. HNSW Configuration Limits

**Valid Parameters:**
- space: 'l2', 'ip', 'cosine'
- ef_construction: 10-1000 (default: 200)
- ef_search: 10-1000 (default: 100)
- M: 4-64 (default: 16)
- num_threads: 1-32 (default: 4)

**Trade-offs:**
- Higher ef_construction = better recall, slower indexing
- Higher ef_search = better recall, slower queries
- Higher M = better recall, more memory

## 10. Error Recovery Strategies

**Common Errors and Solutions:**

1. **Database Locked**
   - Implement retry with backoff
   - Use single writer pattern

2. **Unique Constraint Failed**
   - Use upsert instead of add
   - Generate unique IDs properly

3. **Dimension Mismatch**
   - Validate before insertion
   - Use consistent embedding model

4. **Collection Not Found**
   - Use get_or_create pattern
   - Validate collection names

5. **Batch Too Large**
   - Implement proper chunking
   - Use conservative batch sizes

## Production Recommendations

1. **Use the utility functions** in `chromadb_utils.py` for all operations
2. **Validate all inputs** before ChromaDB operations
3. **Implement comprehensive error handling** with specific recovery strategies
4. **Use content-based IDs** for consistency across runs
5. **Monitor collection sizes** and implement archiving if needed
6. **Test with your specific data** to find optimal batch sizes
7. **Consider ChromaDB server mode** for production deployments
8. **Implement proper logging** for debugging issues
9. **Use transactions** where possible for atomic operations
10. **Regular backups** of the ChromaDB persistent directory

## Testing

Run the comprehensive edge case tests:
```bash
python3 tests/test_chromadb_edge_cases.py
```

This will validate:
- Collection name handling
- Document size limits
- Metadata constraints
- ID generation
- Batch processing
- Embedding validation
- Error handling
- Safe operations
- HNSW configuration