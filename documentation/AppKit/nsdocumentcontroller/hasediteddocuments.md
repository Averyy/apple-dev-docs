# hasEditedDocuments

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver has any documents with unsaved changes.

**Availability**:
- macOS

## Declaration

```swift
var hasEditedDocuments: Bool { get }
```

```objc
@property (readonly) BOOL hasEditedDocuments;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the document controller contains documents with unsaved changes; otherwise, the value is [`false`](../../Swift/false.md).

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
- [func removeDocument(NSDocument)](./removedocument%28_%29.md)
  Removes the given document from the list of open documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/hasediteddocuments)*