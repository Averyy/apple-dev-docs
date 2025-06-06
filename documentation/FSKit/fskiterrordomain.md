# FSKitErrorDomain

**Framework**: FSKit  
**Kind**: var

An error domain for FSKit errors.

**Availability**:
- macOS 15.4+

## Declaration

```swift
let FSKitErrorDomain: String
```

#### Discussion

See [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) for more information on error domains.

## See Also

- [func fs_errorForCocoaError(Int32) -> any Error](fs_errorforcocoaerror(_:).md)
  Creates an error object for the given Cocoa error code.
- [func fs_errorForMachError(Int32) -> any Error](fs_errorformacherror(_:).md)
  Creates an error object for the given Mach error code.
- [func fs_errorForPOSIXError(Int32) -> any Error](fs_errorforposixerror(_:).md)
  Creates an error object for the given POSIX error code.
- [struct FSError](fserror.md)
  An error encountered when performing an FSKit operation.
- [FSError.Code](fserror/code.md)
  A code that indicates a specific FSKit error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fskiterrordomain)*