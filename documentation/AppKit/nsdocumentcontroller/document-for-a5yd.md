# document(for:)

**Framework**: AppKit  
**Kind**: method

Returns the document object whose window controller owns a specified window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func document(for window: NSWindow) -> NSDocument?
```

#### Return Value

The document object whose window controller owns `window`. Returns `nil` if `window` is `nil`, if `window` has no window controller, or if the window controller does not have an association with an instance of `NSDocument`.

## Parameters

- `window`: The window owned by the window controller.

## See Also

- [var documents: [NSDocument]](nsdocumentcontroller/documents.md)
  The document objects managed by the receiver.
- [func addDocument(NSDocument)](nsdocumentcontroller/adddocument(_:).md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](nsdocumentcontroller/currentdocument.md)
  The document object associated with the main window.
- [var hasEditedDocuments: Bool](nsdocumentcontroller/hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](nsdocumentcontroller/removedocument(_:).md)
  Removes the given document from the list of open documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/document(for:)-a5yd)*