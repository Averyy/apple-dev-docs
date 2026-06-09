# errorInvalidCacheTransition

**Framework**: FSKit  
**Kind**: property

The cache transition is not allowed.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static var errorInvalidCacheTransition: FSDataCacheError.Code { get }
```

#### Discussion

This error occurs when attempting an invalid transition, such as using an upgrade method for a downgrade operation, or vice versa.

## See Also

- [FSDataCacheError.Code](fsdatacacheerror/code.md)
  Error codes specific to data cache operations.
- [static var errorInvalidCacheModeCoherency: FSDataCacheError.Code](fsdatacacheerror/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](fsdatacacheerror/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheInvalidationFailed: FSDataCacheError.Code](fsdatacacheerror/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [static var errorCacheOperationConflict: FSDataCacheError.Code](fsdatacacheerror/errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/errorinvalidcachetransition)*