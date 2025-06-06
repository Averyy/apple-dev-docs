# reopenDocument(for:withContentsOf:display:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func reopenDocument(for urlOrNil: URL?, withContentsOf contentsURL: URL, display displayDocument: Bool) async throws -> (NSDocument, Bool)
```

#### Discussion

The default implementation of this method is very similar to [`openDocument(withContentsOf:display:completionHandler:)`](nsdocumentcontroller/opendocument(withcontentsof:display:completionhandler:).md), the primary difference being that it calls [`makeDocument(for:withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(for:withcontentsof:oftype:).md) instead of [`makeDocument(withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(withcontentsof:oftype:).md).

You can override this method to customize how documents are reopened during application launching by the restorable state mechanism introduced in OS X v10.7. Its implementation, however, is somewhat complex, so you should generally investigate overriding one of the methods that it calls instead. However, you can override this method to do additional work before calling the underlying method on `super`. You can also call the underlying method on `super` with a custom completion handler that performs additional work before calling the original completion handler.

Applications probably do not need to call this method directly.

For backward binary compatibility with OS X v10.6 and earlier, the default implementation of this method calls `[self reopenDocumentForURL:url withContentsOfURL:contentsURL error:&anError]` if that method is overridden and this one is not, instead of calling [`makeDocument(for:withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(for:withcontentsof:oftype:).md) and all the rest.

## Parameters

- `urlOrNil`: The URL locating the reopened document, unless  . A   parameter value indicates that the reopened document is to have no  , like an untitled document.
- `contentsURL`: The URL (which may or may not be different from the URL of the reopened document) of the document from which the contents are read.
- `displayDocument`: If  , displays the document’s user interface.
- `completionHandler`: The block takes three arguments:

## See Also

- [func document(for: URL) -> NSDocument?](nsdocumentcontroller/document(for:)-i5zi.md)
  Returns, for a given URL, the open document whose file or file package is located by the URL, or `nil` if there is no such open document.
- [func duplicateDocument(withContentsOf: URL, copying: Bool, displayName: String?) throws -> NSDocument](nsdocumentcontroller/duplicatedocument(withcontentsof:copying:displayname:).md)
  Creates a new document by reading the contents for the document from another URL, presents its user interface, and returns the document if successful.
- [func openDocument(withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](nsdocumentcontroller/opendocument(withcontentsof:display:completionhandler:).md)
  Opens a document located by a URL, optionally presents its user interface, and calls the passed-in completion handler.
- [func openUntitledDocumentAndDisplay(Bool) throws -> NSDocument](nsdocumentcontroller/openuntitleddocumentanddisplay(_:).md)
  Creates a new untitled document, presents its user interface if `displayDocument` is [`true`](https://developer.apple.com/documentation/swift/true), and returns the document if successful.
- [func makeDocument(for: URL?, withContentsOf: URL, ofType: String) throws -> NSDocument](nsdocumentcontroller/makedocument(for:withcontentsof:oftype:).md)
  Instantiates a document located by a URL, of a specified type, but by reading the contents for the document from another URL, and returns it if successful.
- [func makeDocument(withContentsOf: URL, ofType: String) throws -> NSDocument](nsdocumentcontroller/makedocument(withcontentsof:oftype:).md)
  Instantiates a document located by a URL, of a specified type, and returns it if successful.
- [func makeUntitledDocument(ofType: String) throws -> NSDocument](nsdocumentcontroller/makeuntitleddocument(oftype:).md)
  Instantiates a new untitled document of the specified type and returns it if successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/reopendocument(for:withcontentsof:display:completionhandler:))*