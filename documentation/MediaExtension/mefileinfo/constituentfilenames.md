# constituentFileNames

**Framework**: MediaExtension  
**Kind**: property

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var constituentFileNames: [String] { get set }
```

#### Discussion

List of media files that collectively represent the media asset.

Represents a list of media files that constitute the media asset. All files must be located in the same directory. The returned filenames should include just the file name and file extension, omitting any file path or directory slashes. The file extensions should all be explicitly supported by the format reader as declared in the EXAppExtensionAttributes and UTExportedTypeDeclarations dictionaries in the MediaExtension format reader Info.plist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/constituentfilenames)*