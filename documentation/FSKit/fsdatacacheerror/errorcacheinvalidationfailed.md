# errorCacheInvalidationFailed

**Framework**: FSKit  
**Kind**: property

Failed to invalidate (clear) cached data.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static var errorCacheInvalidationFailed: FSDataCacheError.Code { get }
```

## See Also

- [FSDataCacheError.Code](fsdatacacheerror/code.md)
  Error codes specific to data cache operations.
- [static var errorInvalidCacheModeCoherency: FSDataCacheError.Code](fsdatacacheerror/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [static var errorInvalidCacheTransition: FSDataCacheError.Code](fsdatacacheerror/errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](fsdatacacheerror/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheOperationConflict: FSDataCacheError.Code](fsdatacacheerror/errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/errorcacheinvalidationfailed)*