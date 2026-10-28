# document(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the document object whose window controller owns a specified window.

**Availability**:
- macOS

## Declaration

```swift
func document(for window: NSWindow) -> NSDocument?
```

```objc
- (NSDocument *) documentForWindow:(NSWindow *) window;
```

## Return Value

The document object whose window controller owns `window`. Returns `nil` if `window` is `nil`, if `window` has no window controller, or if the window controller does not have an association with an instance of `NSDocument`.

## Parameters

- `window`: The window owned by the window controller.

## See Also

### Managing Documents
- [var documents: [NSDocument]](./documents.md)
  The document objects managed by the receiver.
- [func addDocument(NSDocument)](./adddocument%28_%29.md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](./currentdocument.md)
  The document object associated with the main window.
- [var hasEditedDocuments: Bool](./hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](./removedocument%28_%29.md)
  Removes the given document from the list of open documents.
### Related Documentation
- [- documentForFileName:](./documentforfilename_.md)
  Returns the document object for the file in which the document data is stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/document(for:)-a5yd)*