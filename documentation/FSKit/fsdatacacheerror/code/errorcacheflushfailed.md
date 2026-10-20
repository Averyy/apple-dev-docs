# FSDataCacheError.Code.errorCacheFlushFailed

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

Failed to flush dirty cached data to storage.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case errorCacheFlushFailed
```

```c
FSErrorCacheFlushFailed
```

## See Also

### Error codes
- [FSDataCacheError.Code.errorInvalidCacheModeCoherency](./errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [FSDataCacheError.Code.errorInvalidCacheTransition](./errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [FSDataCacheError.Code.errorCacheInvalidationFailed](./errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [FSDataCacheError.Code.errorCacheOperationConflict](./errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/code/errorcacheflushfailed)*