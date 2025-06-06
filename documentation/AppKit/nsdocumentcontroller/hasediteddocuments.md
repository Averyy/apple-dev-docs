# hasEditedDocuments

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver has any documents with unsaved changes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasEditedDocuments: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the document controller contains documents with unsaved changes; otherwise, the value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var documents: [NSDocument]](nsdocumentcontroller/documents.md)
  The document objects managed by the receiver.
- [func addDocument(NSDocument)](nsdocumentcontroller/adddocument(_:).md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](nsdocumentcontroller/currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](nsdocumentcontroller/document(for:)-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [func removeDocument(NSDocument)](nsdocumentcontroller/removedocument(_:).md)
  Removes the given document from the list of open documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/hasediteddocuments)*