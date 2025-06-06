# fileSystemTypeName

**Framework**: FSKit  
**Kind**: property

A property for the file system type name.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var fileSystemTypeName: String { get }
```

#### Discussion

Match this value to the `FSShortName` attribute within the `EXAppExtensionAttributes` dictionary of the module’s `Info.plist`. The maximum allowed length is `MFSTYPENAMELEN`, including the terminating `NUL` character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsstatfsresult/filesystemtypename)*