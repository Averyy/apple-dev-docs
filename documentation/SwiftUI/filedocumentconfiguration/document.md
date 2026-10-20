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
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Conform your type to Document and use URLDocumentConfiguration instead.

## Declaration

```swift
@Binding
var document: Document { get nonmutating set }
```

#### Discussion

Setting a new value marks the document as having changes for later saving and registers an undo action to restore the model to its previous value.

If [`isEditable`](./iseditable.md) is `false`, setting a new value has no effect because the document is in viewing mode.

## See Also

### Getting and setting the document
- [var $document: Binding<Document>](./dollardocument.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocumentconfiguration/document)*