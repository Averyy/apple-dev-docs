# documents

**Framework**: AppKit  
**Kind**: property

The document objects managed by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var documents: [NSDocument] { get }
```

#### Discussion

The array contains zero or more [`NSDocument`](nsdocument.md) objects.

## See Also

- [func addDocument(NSDocument)](nsdocumentcontroller/adddocument(_:).md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](nsdocumentcontroller/currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](nsdocumentcontroller/document(for:)-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](nsdocumentcontroller/hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](nsdocumentcontroller/removedocument(_:).md)
  Removes the given document from the list of open documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/documents)*