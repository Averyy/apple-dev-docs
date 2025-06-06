# fs_errorForCocoaError(_:)

**Framework**: FSKit  
**Kind**: func

Creates an error object for the given Cocoa error code.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func fs_errorForCocoaError(_ errorCode: Int32) -> any Error
```

## See Also

- [func fs_errorForMachError(Int32) -> any Error](fs_errorformacherror(_:).md)
  Creates an error object for the given Mach error code.
- [func fs_errorForPOSIXError(Int32) -> any Error](fs_errorforposixerror(_:).md)
  Creates an error object for the given POSIX error code.
- [struct FSError](fserror.md)
  An error encountered when performing an FSKit operation.
- [FSError.Code](fserror/code.md)
  A code that indicates a specific FSKit error.
- [let FSKitErrorDomain: String](fskiterrordomain.md)
  An error domain for FSKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fs_errorforcocoaerror(_:))*