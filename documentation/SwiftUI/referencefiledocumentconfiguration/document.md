# document

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The current document model.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use Document protocol and URLDocumentConfiguration instead.

## Declaration

```swift
@ObservedObject
<Document> @MainActor @preconcurrency var document: Document { get set }
```

## Discussion

Changes to the document dirty the document state, indicating that it needs to be saved. SwiftUI doesn’t automatically register undo actions.

## See Also

### Getting and setting the document
- [var $document: ObservedObject<Document>.Wrapper](./dollardocument.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration/document)*