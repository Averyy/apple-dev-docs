# FSKitErrorDomain

**Framework**: FSKit  
**Kind**: var  
**Role**: Global Variable

An error domain for FSKit errors.

**Availability**:
- macOS 15.4+

## Declaration

```swift
let FSKitErrorDomain: String
```

```c
extern NSErrorDomain const FSKitErrorDomain;
```

## Discussion

See [`NSError`](../Foundation/nserror.md) for more information on error domains.

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
- [struct FSDataCacheError](./fsdatacacheerror.md)
  An error encountered when performing an FSKit data caching operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fskiterrordomain)*