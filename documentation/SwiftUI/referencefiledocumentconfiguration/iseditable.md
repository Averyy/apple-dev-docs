# isEditable

**Framework**: SwiftUI  
**Kind**: property

A Boolean that indicates whether you can edit the document.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var isEditable: Bool
```

#### Discussion

The value is `false` if the document is in viewing mode, or if the file is not writable.

## See Also

- [var fileURL: URL?](referencefiledocumentconfiguration/fileurl.md)
  The URL of the open file document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration/iseditable)*