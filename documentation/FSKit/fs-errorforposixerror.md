# fs_errorForPOSIXError(_:)

**Framework**: FSKit  
**Kind**: func

Creates an error object for the given POSIX error code.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func fs_errorForPOSIXError(_: Int32) -> any Error
```

## See Also

- [func fs_errorForCocoaError(Int32) -> any Error](fs_errorforcocoaerror(_:).md)
  Creates an error object for the given Cocoa error code.
- [func fs_errorForMachError(Int32) -> any Error](fs_errorformacherror(_:).md)
  Creates an error object for the given Mach error code.
- [struct FSError](fserror.md)
  An error encountered when performing an FSKit operation.
- [FSError.Code](fserror/code.md)
  A code that indicates a specific FSKit error.
- [let FSKitErrorDomain: String](fskiterrordomain.md)
  An error domain for FSKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fs_errorforposixerror(_:))*