# FSDataCacheError.Code.errorCacheOperationConflict

**Framework**: FSKit  
**Kind**: case

A conflicting cache operation is in progress.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case errorCacheOperationConflict
```

#### Discussion

This error occurs when multiple cache operations on the same item conflict, such as attempting to change cache mode while I/O is active.

## See Also

- [FSDataCacheError.Code.errorInvalidCacheModeCoherency](fsdatacacheerror/code/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [FSDataCacheError.Code.errorInvalidCacheTransition](fsdatacacheerror/code/errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [FSDataCacheError.Code.errorCacheFlushFailed](fsdatacacheerror/code/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [FSDataCacheError.Code.errorCacheInvalidationFailed](fsdatacacheerror/code/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/code/errorcacheoperationconflict)*