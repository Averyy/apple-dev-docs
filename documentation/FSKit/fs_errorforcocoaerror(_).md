# fs_errorForCocoaError(_:)

**Framework**: FSKit  
**Kind**: func  
**Role**: Function

Creates an error object for the given Cocoa error code.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func fs_errorForCocoaError(_ errorCode: Int32) -> any Error
```

```c
extern NSError *fs_errorForCocoaError(int errorCode);
```

## See Also

### Errors and logging
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
- [struct FSDataCacheError](./fsdatacacheerror.md)
  An error encountered when performing an FSKit data caching operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fs_errorforcocoaerror(_:))*