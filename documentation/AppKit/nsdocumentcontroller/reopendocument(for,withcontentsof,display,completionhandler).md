# reopenDocument(for:withContentsOf:display:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func reopenDocument(for urlOrNil: URL?, withContentsOf contentsURL: URL, display displayDocument: Bool, completionHandler: @escaping (NSDocument?, Bool, (any Error)?) -> Void)
```

```swift
func reopenDocument(for urlOrNil: URL?, withContentsOf contentsURL: URL, display displayDocument: Bool) async throws -> (NSDocument, Bool)
```

```objc
- (void) reopenDocumentForURL:(NSURL *) urlOrNil withContentsOfURL:(NSURL *) contentsURL display:(BOOL) displayDocument completionHandler:(void (^)(NSDocument *document, BOOL documentWasAlreadyOpen, NSError *error)) completionHandler;
```

## Discussion

The default implementation of this method is very similar to [`openDocument(withContentsOf:display:completionHandler:)`](./opendocument%28withcontentsof,display,completionhandler%29.md), the primary difference being that it calls [`makeDocument(for:withContentsOf:ofType:)`](./makedocument%28for,withcontentsof,oftype%29.md) instead of [`makeDocument(withContentsOf:ofType:)`](./makedocument%28withcontentsof,oftype%29.md).

You can override this method to customize how documents are reopened during application launching by the restorable state mechanism introduced in OS X v10.7. Its implementation, however, is somewhat complex, so you should generally investigate overriding one of the methods that it calls instead. However, you can override this method to do additional work before calling the underlying method on `super`. You can also call the underlying method on `super` with a custom completion handler that performs additional work before calling the original completion handler.

Applications probably do not need to call this method directly.

For backward binary compatibility with OS X v10.6 and earlier, the default implementation of this method calls `[self reopenDocumentForURL:url withContentsOfURL:contentsURL error:&anError]` if that method is overridden and this one is not, instead of calling [`makeDocument(for:withContentsOf:ofType:)`](./makedocument%28for,withcontentsof,oftype%29.md) and all the rest.

## Parameters

- `urlOrNil`: The URL locating the reopened document, unless `nil`. A `nil` parameter value indicates that the reopened document is to have no [`fileURL`](../nsdocument/fileurl.md), like an untitled document.
- `contentsURL`: The URL (which may or may not be different from the URL of the reopened document) of the document from which the contents are read.
- `displayDocument`: If [`true`](../../Swift/true.md), displays the document’s user interface.
- `completionHandler`: The completion handler block object passed in to be called at some point in the future, perhaps after the method invocation has returned. The completion handler must be called on the main thread.

  The block takes three arguments:

  - **`document`**: The document that was opened, if successful. Otherwise, `nil`.
  - **`documentWasAlreadyOpen`**: Whether the document was already open or being opened when this method was called.
  - **`error`**: If not successful, an `NSError` object that encapsulates the reason why the document could not be opened.

## See Also

### Creating and Opening Documents
- [func document(for: URL) -> NSDocument?](./document%28for%29-i5zi.md)
  Returns, for a given URL, the open document whose file or file package is located by the URL, or `nil` if there is no such open document.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/reopendocument(for:withcontentsof:display:completionhandler:))*