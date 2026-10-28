# documents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The document objects managed by the receiver.

**Availability**:
- macOS

## Declaration

```swift
var documents: [NSDocument] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSDocument *> * documents;
```

## Discussion

The array contains zero or more [`NSDocument`](../nsdocument.md) objects.

## See Also

### Managing Documents
- [func addDocument(NSDocument)](./adddocument%28_%29.md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](./currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](./document%28for%29-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](./hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](./removedocument%28_%29.md)
  Removes the given document from the list of open documents.
### Related Documentation
- [- documentForFileName:](./documentforfilename_.md)
  Returns the document object for the file in which the document data is stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/documents)*