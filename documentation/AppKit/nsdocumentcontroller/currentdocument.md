# currentDocument

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The document object associated with the main window.

**Availability**:
- macOS

## Declaration

```swift
var currentDocument: NSDocument? { get }
```

```objc
@property (strong, readonly, nullable) NSDocument * currentDocument;
```

#### Discussion

The value of this property is `nil` if it is called when the app is not active. This can occur during processing of a drag-and-drop operation, for example, in an implementation of `readSelectionFromPasteboard:`. In such a case, send the following message instead from an `NSView` subclass associated with the document:

```objc
[[[self window] windowController] document];
```

## See Also

### Managing Documents
- [var documents: [NSDocument]](./documents.md)
  The document objects managed by the receiver.
- [func addDocument(NSDocument)](./adddocument%28_%29.md)
  Adds the given document to the list of open documents.
- [func document(for: NSWindow) -> NSDocument?](./document%28for%29-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](./hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](./removedocument%28_%29.md)
  Removes the given document from the list of open documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/currentdocument)*