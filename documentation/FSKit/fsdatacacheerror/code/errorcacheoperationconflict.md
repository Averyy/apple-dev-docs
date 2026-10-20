# FSDataCacheError.Code.errorCacheOperationConflict

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

A conflicting cache operation is in progress.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case errorCacheOperationConflict
```

```c
FSErrorCacheOperationConflict
```

#### Discussion

This error occurs when multiple cache operations on the same item conflict, such as attempting to change cache mode while I/O is active.

## See Also

### Error codes
- [FSDataCacheError.Code.errorInvalidCacheModeCoherency](./errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [FSDataCacheError.Code.errorInvalidCacheTransition](./errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [FSDataCacheError.Code.errorCacheFlushFailed](./errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [FSDataCacheError.Code.errorCacheInvalidationFailed](./errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/code/errorcacheoperationconflict)*