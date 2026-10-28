# errorCacheOperationConflict

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

A conflicting cache operation is in progress.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static var errorCacheOperationConflict: FSDataCacheError.Code { get }
```

## Discussion

This error occurs when multiple cache operations on the same item conflict, such as attempting to change cache mode while I/O is active.

## See Also

### Error codes
- [FSDataCacheError.Code](./code.md)
  Error codes specific to data cache operations.
- [static var errorInvalidCacheModeCoherency: FSDataCacheError.Code](./errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [static var errorInvalidCacheTransition: FSDataCacheError.Code](./errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](./errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheInvalidationFailed: FSDataCacheError.Code](./errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/errorcacheoperationconflict)*