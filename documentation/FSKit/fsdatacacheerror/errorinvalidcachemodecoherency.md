# errorInvalidCacheModeCoherency

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

The requested cache mode and coherency type combination is invalid.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static var errorInvalidCacheModeCoherency: FSDataCacheError.Code { get }
```

## See Also

### Error codes
- [FSDataCacheError.Code](./code.md)
  Error codes specific to data cache operations.
- [static var errorInvalidCacheTransition: FSDataCacheError.Code](./errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](./errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheInvalidationFailed: FSDataCacheError.Code](./errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [static var errorCacheOperationConflict: FSDataCacheError.Code](./errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/errorinvalidcachemodecoherency)*