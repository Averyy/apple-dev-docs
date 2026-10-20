# document(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns, for a given URL, the open document whose file or file package is located by the URL, or `nil` if there is no such open document.

**Availability**:
- macOS

## Declaration

```swift
func document(for url: URL) -> NSDocument?
```

```objc
- (NSDocument *) documentForURL:(NSURL *) url;
```

#### Return Value

The newly created [`NSDocument`](../nsdocument.md) object, or `nil` if the document could not be created.

#### Discussion

The default implementation of this method queries each open document to find one whose URL matches, and returns the first one whose URL does match.

## Parameters

- `url`: The URL of the document you wish to look up.

## See Also

### Creating and Opening Documents
- [func duplicateDocument(withContentsOf: URL, copying: Bool, displayName: String?) throws -> NSDocument](./duplicatedocument%28withcontentsof,copying,displayname%29.md)
  Creates a new document by reading the contents for the document from another URL, presents its user interface, and returns the document if successful.
- [func openDocument(withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](./opendocument%28withcontentsof,display,completionhandler%29.md)
  Opens a document located by a URL, optionally presents its user interface, and calls the passed-in completion handler.
- [func openUntitledDocumentAndDisplay(Bool) throws -> NSDocument](./openuntitleddocumentanddisplay%28_%29.md)
  Creates a new untitled document, presents its user interface if `displayDocument` is `true`, and returns the document if successful.
- [func makeDocument(for: URL?, withContentsOf: URL, ofType: String) throws -> NSDocument](./makedocument%28for,withcontentsof,oftype%29.md)
  Instantiates a document located by a URL, of a specified type, but by reading the contents for the document from another URL, and returns it if successful.
- [func makeDocument(withContentsOf: URL, ofType: String) throws -> NSDocument](./makedocument%28withcontentsof,oftype%29.md)
  Instantiates a document located by a URL, of a specified type, and returns it if successful.
- [func makeUntitledDocument(ofType: String) throws -> NSDocument](./makeuntitleddocument%28oftype%29.md)
  Instantiates a new untitled document of the specified type and returns it if successful.
- [func reopenDocument(for: URL?, withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](./reopendocument%28for,withcontentsof,display,completionhandler%29.md)
  Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/document(for:)-i5zi)*