# FSDataCacheError.Code

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

Error codes specific to data cache operations.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum Code
```

```c
enum FSDataCacheErrorCode : NSInteger;
```

## Topics

### Error codes
- [FSDataCacheError.Code.errorInvalidCacheModeCoherency](./code/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [FSDataCacheError.Code.errorInvalidCacheTransition](./code/errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [FSDataCacheError.Code.errorCacheFlushFailed](./code/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [FSDataCacheError.Code.errorCacheInvalidationFailed](./code/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [FSDataCacheError.Code.errorCacheOperationConflict](./code/errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error codes
- [static var errorInvalidCacheModeCoherency: FSDataCacheError.Code](./errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [static var errorInvalidCacheTransition: FSDataCacheError.Code](./errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](./errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheInvalidationFailed: FSDataCacheError.Code](./errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [static var errorCacheOperationConflict: FSDataCacheError.Code](./errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror/code)*