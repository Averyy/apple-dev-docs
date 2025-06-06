# metadataTypes

**Framework**: AppKit  
**Kind**: property

A set of key paths that represent metadata types that the data detection system identifies.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var metadataTypes: Set<PartialKeyPath<NSPasteboard.DetectedMetadata>> { get }
```

## See Also

- [var contentType: UTType?](nspasteboard/detectedmetadata/contenttype.md)
  The content type of a file that the data detection system identifies when the pasteboard contains a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectedmetadata/metadatatypes)*