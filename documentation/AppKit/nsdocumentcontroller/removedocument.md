# removeDocument(_:)

**Framework**: AppKit  
**Kind**: method

Removes the given document from the list of open documents.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeDocument(_ document: NSDocument)
```

#### Discussion

A document will automatically call [`removeDocument(_:)`](nsdocumentcontroller/removedocument(_:).md) when it closes. This method is mostly provided for subclasses that want to know when documents close.

## Parameters

- `document`: The document to remove.

## See Also

- [var documents: [NSDocument]](nsdocumentcontroller/documents.md)
  The document objects managed by the receiver.
- [func addDocument(NSDocument)](nsdocumentcontroller/adddocument(_:).md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](nsdocumentcontroller/currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](nsdocumentcontroller/document(for:)-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](nsdocumentcontroller/hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/removedocument(_:))*