# FSDataCacheError.Code.errorInvalidCacheTransition

**Framework**: FSKit  
**Kind**: case

The cache transition is not allowed.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
case errorInvalidCacheTransition
```

#### Discussion

This error occurs when attempting an invalid transition, such as using an upgrade method for a downgrade operation, or vice versa.

## See Also

- [FSDataCacheError.Code.errorInvalidCacheModeCoherency](fsdatacacheerror/code/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [FSDataCacheError.Code.errorCacheFlushFailed](fsdatacacheerror/code/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [FSDataCacheError.Code.errorCacheInvalidationFailed](fsdatacacheerror/code/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [FSDataCacheError.Code.errorCacheOperationConflict](fsdatacacheerror/code/errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/code/errorinvalidcachetransition)*