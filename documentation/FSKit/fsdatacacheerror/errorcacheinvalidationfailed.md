# errorCacheInvalidationFailed

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

Failed to invalidate (clear) cached data.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static var errorCacheInvalidationFailed: FSDataCacheError.Code { get }
```

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
- [static var errorCacheOperationConflict: FSDataCacheError.Code](./errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/errorcacheinvalidationfailed)*