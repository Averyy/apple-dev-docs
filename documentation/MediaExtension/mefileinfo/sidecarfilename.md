# sidecarFileName

**Framework**: MediaExtension  
**Kind**: property

**Availability**:
- macOS 26.0+

## Declaration

```swift
var sidecarFileName: String? { get set }
```

#### Discussion

The sidecar filename used by the MediaExtension.

Represents a new or existing sidecar file located in the same directory as the primary media file. The filename should include the file extension, and should not contain the file path, or contain any slashes. The file extension should be supported by the format reader, and present in the EXAppExtensionAttributes and UTExportedTypeDeclarations dictionaries in the MediaExtension format reader Info.plist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/sidecarfilename)*