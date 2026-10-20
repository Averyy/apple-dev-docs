# isEditable

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether you can edit the document.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use Document protocol and URLDocumentConfiguration instead.

## Declaration

```swift
@MainActor
@preconcurrency var isEditable: Bool
```

#### Discussion

The value is `false` if the document is in viewing mode, or if the file is not writable.

## See Also

### Getting document properties
- [var fileURL: URL?](./fileurl.md)
  The URL of the open file document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration/iseditable)*