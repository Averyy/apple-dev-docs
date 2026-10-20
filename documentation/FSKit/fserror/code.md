# FSError.Code

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

A code that indicates a specific FSKit error.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum Code
```

```c
enum FSErrorCode : NSInteger;
```

## Topics

### Identifying errors
- [FSError.Code.invalidDirectoryCookie](./code/invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.moduleLoadFailed](./code/moduleloadfailed.md)
  The module failed to load.
- [FSError.Code.resourceDamaged](./code/resourcedamaged.md)
  The resource is damaged.
- [FSError.Code.resourceUnrecognized](./code/resourceunrecognized.md)
  FSKit didn’t recognize the resource, and probing failed to find a match.
- [FSError.Code.resourceUnusable](./code/resourceunusable.md)
  FSKit recognizes the resource, but the resource isn’t usable.
- [FSError.Code.statusOperationInProgress](./code/statusoperationinprogress.md)
  An operation is in progress.
- [FSError.Code.statusOperationPaused](./code/statusoperationpaused.md)
  An operation is paused.
### Working with raw values
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

### Errors and logging
- [func fs_errorForCocoaError(Int32) -> any Error](../fs_errorforcocoaerror%28_%29.md)
  Creates an error object for the given Cocoa error code.
- [func fs_errorForMachError(Int32) -> any Error](../fs_errorformacherror%28_%29.md)
  Creates an error object for the given Mach error code.
- [func fs_errorForPOSIXError(Int32) -> any Error](../fs_errorforposixerror%28_%29.md)
  Creates an error object for the given POSIX error code.
- [struct FSError](../fserror.md)
  An error encountered when performing an FSKit operation.
- [let FSKitErrorDomain: String](../fskiterrordomain.md)
  An error domain for FSKit errors.
- [struct FSDataCacheError](../fsdatacacheerror.md)
  An error encountered when performing an FSKit data caching operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror/code)*