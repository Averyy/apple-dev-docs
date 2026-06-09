# errorCacheOperationConflict

**Framework**: FSKit  
**Kind**: property

A conflicting cache operation is in progress.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static var errorCacheOperationConflict: FSDataCacheError.Code { get }
```

#### Discussion

This error occurs when multiple cache operations on the same item conflict, such as attempting to change cache mode while I/O is active.

## See Also

- [FSDataCacheError.Code](fsdatacacheerror/code.md)
  Error codes specific to data cache operations.
- [static var errorInvalidCacheModeCoherency: FSDataCacheError.Code](fsdatacacheerror/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [static var errorInvalidCacheTransition: FSDataCacheError.Code](fsdatacacheerror/errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](fsdatacacheerror/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheInvalidationFailed: FSDataCacheError.Code](fsdatacacheerror/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/errorcacheoperationconflict)*