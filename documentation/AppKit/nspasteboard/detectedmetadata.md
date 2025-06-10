# NSPasteboard.DetectedMetadata

**Framework**: AppKit  
**Kind**: struct

An object that contains common types of metadata that the data detection system matches for a pasteboard.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct DetectedMetadata
```

## Topics

### Instance Properties
- [var contentType: UTType?](nspasteboard/detectedmetadata/contenttype.md)
  The content type of a file that the data detection system identifies when the pasteboard contains a file URL.
- [var metadataTypes: Set<PartialKeyPath<NSPasteboard.DetectedMetadata>>](nspasteboard/detectedmetadata/metadatatypes.md)
  A set of key paths that represent metadata types that the data detection system identifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectedmetadata)*