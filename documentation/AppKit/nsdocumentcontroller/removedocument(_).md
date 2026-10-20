# removeDocument(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the given document from the list of open documents.

**Availability**:
- macOS

## Declaration

```swift
func removeDocument(_ document: NSDocument)
```

```objc
- (void) removeDocument:(NSDocument *) document;
```

#### Discussion

A document will automatically call [`removeDocument(_:)`](./removedocument%28_%29.md) when it closes. This method is mostly provided for subclasses that want to know when documents close.

## Parameters

- `document`: The document to remove.

## See Also

### Managing Documents
- [var documents: [NSDocument]](./documents.md)
  The document objects managed by the receiver.
- [func addDocument(NSDocument)](./adddocument%28_%29.md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](./currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](./document%28for%29-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](./hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/removedocument(_:))*