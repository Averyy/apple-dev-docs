# FSError.Code

**Framework**: FSKit  
**Kind**: enum

A code that indicates a specific FSKit error.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum Code
```

## Topics

### Identifying errors
- [FSError.Code.invalidDirectoryCookie](fserror/code/invaliddirectorycookie.md)
  While enumerating a directory, the given cookie didn’t resolve to a valid directory entry.
- [FSError.Code.moduleLoadFailed](fserror/code/moduleloadfailed.md)
  The module failed to load.
- [FSError.Code.resourceDamaged](fserror/code/resourcedamaged.md)
  The resource is damaged.
- [FSError.Code.resourceUnrecognized](fserror/code/resourceunrecognized.md)
  FSKit didn’t recognize the resource, and probing failed to find a match.
- [FSError.Code.resourceUnusable](fserror/code/resourceunusable.md)
  FSKit recognizes the resource, but the resource isn’t usable.
- [FSError.Code.statusOperationInProgress](fserror/code/statusoperationinprogress.md)
  An operation is in progress.
- [FSError.Code.statusOperationPaused](fserror/code/statusoperationpaused.md)
  An operation is paused.
### Working with raw values
- [init?(rawValue: Int)](fserror/code/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fserror/code/equatable-implementations.md)
- [RawRepresentable Implementations](fserror/code/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func fs_errorForCocoaError(Int32) -> any Error](fs_errorforcocoaerror(_:).md)
  Creates an error object for the given Cocoa error code.
- [func fs_errorForMachError(Int32) -> any Error](fs_errorformacherror(_:).md)
  Creates an error object for the given Mach error code.
- [func fs_errorForPOSIXError(Int32) -> any Error](fs_errorforposixerror(_:).md)
  Creates an error object for the given POSIX error code.
- [struct FSError](fserror.md)
  An error encountered when performing an FSKit operation.
- [let FSKitErrorDomain: String](fskiterrordomain.md)
  An error domain for FSKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror/code)*