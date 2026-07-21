# DocumentCreationContext

**Framework**: SwiftUI  
**Kind**: struct

Context about how a document was created.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DocumentCreationContext
```

#### Overview

SwiftUI passes this to the `makeDocument` closure of [`DocumentGroup`](documentgroup.md). Use [`creationSource`](documentcreationcontext/creationsource.md) to determine which [`NewDocumentButton`](newdocumentbutton.md) the person tapped and configure the document accordingly:

```swift
DocumentGroup { document in
    EditorView(document: document)
} makeDocument: { configuration, context in
    let document = NotesDocument()
    if context.creationSource == .checklist {
        document.template = .checklist
    }
    return document
}
```

## Topics

### Accessing creation properties
- [var creationSource: DocumentCreationSource?](documentcreationcontext/creationsource.md)
  The source associated with the button that created this document.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol Document](document.md)
  A document that supports both reading and writing.
- [protocol ReadableDocument](readabledocument.md)
  A document type that supports reading from file.
- [protocol WritableDocument](writabledocument.md)
  A document type that supports writing to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  The configuration of an open document that stores its file URL, last modification date, and related metadata.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentcreationcontext)*