# FSDataCacheError

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

An error encountered when performing an FSKit data caching operation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct FSDataCacheError
```

## Topics

### Error codes
- [FSDataCacheError.Code](./fsdatacacheerror/code.md)
  Error codes specific to data cache operations.
- [static var errorInvalidCacheModeCoherency: FSDataCacheError.Code](./fsdatacacheerror/errorinvalidcachemodecoherency.md)
  The requested cache mode and coherency type combination is invalid.
- [static var errorInvalidCacheTransition: FSDataCacheError.Code](./fsdatacacheerror/errorinvalidcachetransition.md)
  The cache transition is not allowed.
- [static var errorCacheFlushFailed: FSDataCacheError.Code](./fsdatacacheerror/errorcacheflushfailed.md)
  Failed to flush dirty cached data to storage.
- [static var errorCacheInvalidationFailed: FSDataCacheError.Code](./fsdatacacheerror/errorcacheinvalidationfailed.md)
  Failed to invalidate (clear) cached data.
- [static var errorCacheOperationConflict: FSDataCacheError.Code](./fsdatacacheerror/errorcacheoperationconflict.md)
  A conflicting cache operation is in progress.
### Identifying the error domain
- [static var errorDomain: String](./fsdatacacheerror/errordomain.md)
  The domain of the data cache error.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors and logging
- [func fs_errorForCocoaError(Int32) -> any Error](./fs_errorforcocoaerror%28_%29.md)
  Creates an error object for the given Cocoa error code.
- [func fs_errorForMachError(Int32) -> any Error](./fs_errorformacherror%28_%29.md)
  Creates an error object for the given Mach error code.
- [func fs_errorForPOSIXError(Int32) -> any Error](./fs_errorforposixerror%28_%29.md)
  Creates an error object for the given POSIX error code.
- [struct FSError](./fserror.md)
  An error encountered when performing an FSKit operation.
- [FSError.Code](./fserror/code.md)
  A code that indicates a specific FSKit error.
- [let FSKitErrorDomain: String](./fskiterrordomain.md)
  An error domain for FSKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdatacacheerror)*