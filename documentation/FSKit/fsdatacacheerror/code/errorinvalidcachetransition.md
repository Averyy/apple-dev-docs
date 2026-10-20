# FSDataCacheError.Code.errorInvalidCacheTransition

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

The cache transition is not allowed.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case errorInvalidCacheTransition
```

```c
FSErrorInvalidCacheTransition
```

#### Discussion

This error occurs when attempting an invalid transition, such as using an upgrade method for a downgrade operation, or vice versa.

## See Also

### Error codes
- [FSDataCacheError.Code.errorInvalidCacheModeCoherency](./errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [FSDataCacheError.Code.errorCacheFlushFailed](./errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [FSDataCacheError.Code.errorCacheInvalidationFailed](./errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [FSDataCacheError.Code.errorCacheOperationConflict](./errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/code/errorinvalidcachetransition)*