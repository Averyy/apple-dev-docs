# FSError

**Framework**: FSKit  
**Kind**: struct

An error encountered when performing an FSKit operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSError
```

## Topics

### Identifying errors
- [static var invalidDirectoryCookie: FSError.Code](fserror/invaliddirectorycookie.md)
- [static var moduleLoadFailed: FSError.Code](fserror/moduleloadfailed.md)
- [static var resourceDamaged: FSError.Code](fserror/resourcedamaged.md)
- [static var resourceUnrecognized: FSError.Code](fserror/resourceunrecognized.md)
- [static var resourceUnusable: FSError.Code](fserror/resourceunusable.md)
- [static var statusOperationInProgress: FSError.Code](fserror/statusoperationinprogress.md)
- [static var statusOperationPaused: FSError.Code](fserror/statusoperationpaused.md)
### Identifying the error domain
- [static var errorDomain: String](fserror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fs_errorForCocoaError(Int32) -> any Error](fs_errorforcocoaerror(_:).md)
  Creates an error object for the given Cocoa error code.
- [func fs_errorForMachError(Int32) -> any Error](fs_errorformacherror(_:).md)
  Creates an error object for the given Mach error code.
- [func fs_errorForPOSIXError(Int32) -> any Error](fs_errorforposixerror(_:).md)
  Creates an error object for the given POSIX error code.
- [FSError.Code](fserror/code.md)
  A code that indicates a specific FSKit error.
- [let FSKitErrorDomain: String](fskiterrordomain.md)
  An error domain for FSKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fserror)*