# addDocument(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the given document to the list of open documents.

**Availability**:
- macOS

## Declaration

```swift
func addDocument(_ document: NSDocument)
```

```objc
- (void) addDocument:(NSDocument *) document;
```

#### Discussion

The `open...` methods automatically call [`addDocument(_:)`](./adddocument%28_%29.md). This method is mostly provided for subclasses that want to know when documents arrive.

## Parameters

- `document`: The document to add.

## See Also

### Managing Documents
- [var documents: [NSDocument]](./documents.md)
  The document objects managed by the receiver.
- [var currentDocument: NSDocument?](./currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](./document%28for%29-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](./hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](./removedocument%28_%29.md)
  Removes the given document from the list of open documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/adddocument(_:))*