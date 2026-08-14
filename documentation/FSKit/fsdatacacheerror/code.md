# FSDataCacheError.Code

**Framework**: FSKit  
**Kind**: enum

Error codes specific to data cache operations.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [FSDataCacheError.Code.errorInvalidCacheModeCoherency](fsdatacacheerror/code/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [FSDataCacheError.Code.errorInvalidCacheTransition](fsdatacacheerror/code/errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [FSDataCacheError.Code.errorCacheFlushFailed](fsdatacacheerror/code/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [FSDataCacheError.Code.errorCacheInvalidationFailed](fsdatacacheerror/code/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [FSDataCacheError.Code.errorCacheOperationConflict](fsdatacacheerror/code/errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.
### Initializers
- [init?(rawValue: Int)](fsdatacacheerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static var errorInvalidCacheModeCoherency: FSDataCacheError.Code](fsdatacacheerror/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [static var errorInvalidCacheTransition: FSDataCacheError.Code](fsdatacacheerror/errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](fsdatacacheerror/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheInvalidationFailed: FSDataCacheError.Code](fsdatacacheerror/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [static var errorCacheOperationConflict: FSDataCacheError.Code](fsdatacacheerror/errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/code)*