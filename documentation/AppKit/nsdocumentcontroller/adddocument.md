# addDocument(_:)

**Framework**: AppKit  
**Kind**: method

Adds the given document to the list of open documents.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addDocument(_ document: NSDocument)
```

#### Discussion

The `open...` methods automatically call [`addDocument(_:)`](nsdocumentcontroller/adddocument(_:).md). This method is mostly provided for subclasses that want to know when documents arrive.

## Parameters

- `document`: The document to add.

## See Also

- [var documents: [NSDocument]](nsdocumentcontroller/documents.md)
  The document objects managed by the receiver.
- [var currentDocument: NSDocument?](nsdocumentcontroller/currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](nsdocumentcontroller/document(for:)-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](nsdocumentcontroller/hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](nsdocumentcontroller/removedocument(_:).md)
  Removes the given document from the list of open documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/adddocument(_:))*