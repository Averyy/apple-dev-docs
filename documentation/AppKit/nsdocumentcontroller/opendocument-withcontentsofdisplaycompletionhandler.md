# openDocument(withContentsOf:display:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Opens a document located by a URL, optionally presents its user interface, and calls the passed-in completion handler.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func openDocument(withContentsOf url: URL, display displayDocument: Bool) async throws -> (NSDocument, Bool)
```

#### Discussion

The default implementation of this method checks to see if the document is already open or being opened, and if it is not determines the type of the document, calls [`makeDocument(withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(withcontentsof:oftype:).md) to instantiate it, and calls [`addDocument(_:)`](nsdocumentcontroller/adddocument(_:).md) to record its opening. If `displayDocument` is [`true`](https://developer.apple.com/documentation/swift/true) and the document is not already open, the default implementation calls [`makeWindowControllers()`](nsdocument/makewindowcontrollers().md) and [`showWindows()`](nsdocument/showwindows().md). If the document is already open, the implementation just calls [`showWindows()`](nsdocument/showwindows().md) if `displayDocument` is [`true`](https://developer.apple.com/documentation/swift/true). If the relevant document class returns [`true`](https://developer.apple.com/documentation/swift/true) when sent [`canConcurrentlyReadDocuments(ofType:)`](nsdocument/canconcurrentlyreaddocuments(oftype:).md) then the invocation of [`makeDocument(withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(withcontentsof:oftype:).md) is done on a thread other than the main one, and when that has returned, the rest of the operation is done on the main thread.

The default implementation of this method uses the file coordination mechanism that was added to the Foundation framework in OS X v10.7. All of the work it does is one big coordinated read, and it passes the document to the `NSFileCoordinator` method [`addFilePresenter(_:)`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator/addFilePresenter(_:)) right after calling [`addDocument(_:)`](nsdocumentcontroller/adddocument(_:).md). (The balancing invocation of the `NSFileCoordinator` method [`removeFilePresenter(_:)`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator/removeFilePresenter(_:)) is in the `NSDocument` method [`close()`](nsdocument/close().md).)

You can override this method to customize how documents are opened. Its implementation, however, is somewhat complex, so you should generally investigate overriding one of the methods that it calls instead. However, you can override this method to do additional work before calling the underlying method on `super`. You can also call the underlying method on `super` with a custom completion handler that performs additional work before calling the original completion handler. If you do override this method you should investigate whether you should also override [`reopenDocument(for:withContentsOf:display:completionHandler:)`](nsdocumentcontroller/reopendocument(for:withcontentsof:display:completionhandler:).md) to apply the same customization. In either case, take care to always call the completion handler on the main thread.

You can call this method to open a document.

##### Special Considerations

For backward binary compatibility with OS X v10.6 and earlier, the default implementation of this method calls `[self openDocumentWithContentsOfURL:url display:displayDocument error:&anError]` if that method or the even older [`openDocumentWithContentsOfFile:display:`](nsdocumentcontroller/opendocumentwithcontentsoffile:display:.md) method is overridden and this one is not, instead of calling [`makeDocument(withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(withcontentsof:oftype:).md) and all the rest.

## Parameters

- `url`: The URL locating the document to open.
- `displayDocument`: If  , displays the document’s user interface.
- `completionHandler`: The block takes three arguments:

## See Also

- [func document(for: URL) -> NSDocument?](nsdocumentcontroller/document(for:)-i5zi.md)
  Returns, for a given URL, the open document whose file or file package is located by the URL, or `nil` if there is no such open document.
- [func duplicateDocument(withContentsOf: URL, copying: Bool, displayName: String?) throws -> NSDocument](nsdocumentcontroller/duplicatedocument(withcontentsof:copying:displayname:).md)
  Creates a new document by reading the contents for the document from another URL, presents its user interface, and returns the document if successful.
- [func openUntitledDocumentAndDisplay(Bool) throws -> NSDocument](nsdocumentcontroller/openuntitleddocumentanddisplay(_:).md)
  Creates a new untitled document, presents its user interface if `displayDocument` is [`true`](https://developer.apple.com/documentation/swift/true), and returns the document if successful.
- [func makeDocument(for: URL?, withContentsOf: URL, ofType: String) throws -> NSDocument](nsdocumentcontroller/makedocument(for:withcontentsof:oftype:).md)
  Instantiates a document located by a URL, of a specified type, but by reading the contents for the document from another URL, and returns it if successful.
- [func makeDocument(withContentsOf: URL, ofType: String) throws -> NSDocument](nsdocumentcontroller/makedocument(withcontentsof:oftype:).md)
  Instantiates a document located by a URL, of a specified type, and returns it if successful.
- [func makeUntitledDocument(ofType: String) throws -> NSDocument](nsdocumentcontroller/makeuntitleddocument(oftype:).md)
  Instantiates a new untitled document of the specified type and returns it if successful.
- [func reopenDocument(for: URL?, withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](nsdocumentcontroller/reopendocument(for:withcontentsof:display:completionhandler:).md)
  Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/opendocument(withcontentsof:display:completionhandler:))*