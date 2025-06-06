# duplicateDocument(withContentsOf:copying:displayName:)

**Framework**: Appkit  
**Kind**: method

Creates a new document by reading the contents for the document from another URL, presents its user interface, and returns the document if successful.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func duplicateDocument(withContentsOf url: URL, copying duplicateByCopying: Bool, displayName displayNameOrNil: String?) throws -> NSDocument
```

#### Return Value

The newly created [`NSDocument`](nsdocument.md) object, or `nil` if the document could not be created.

#### Discussion

The default implementation of this method copies the file if specified, determines the type of the document, calls [`makeDocument(for:withContentsOf:ofType:)`](nsdocumentcontroller/makedocument(for:withcontentsof:oftype:).md) to instantiate it, sends the document `setDisplayName:` to name it if `displayNameOrNil` is not `nil`, calls [`addDocument(_:)`](nsdocumentcontroller/adddocument(_:).md) to record its opening, and sends the document [`makeWindowControllers()`](nsdocument/makewindowcontrollers().md) and [`showWindows()`](nsdocument/showwindows().md) messages.

The default implementation of this method uses the file coordination mechanism introduced in OS X v10.7. It passes the document to the `NSFileCoordinator` method [`addFilePresenter(_:)`](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1417120-addfilepresenter) immediately after calling the [`addDocument(_:)`](nsdocumentcontroller/adddocument(_:).md) method. (The balancing invocation of the [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator) method [`removeFilePresenter(_:)`](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1414924-removefilepresenter) is in the [`NSDocument`](nsdocument.md) method [`close()`](nsdocument/close().md).)

You can override this method to customize how documents are duplicated. It is called by the [`NSDocument`](nsdocument.md) method [`duplicate()`](nsdocument/duplicate().md). It may also be called from other places in AppKit.

In most cases, an app does not need to call this method directly.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL locating the document from which contents of the new document are copied.
- `duplicateByCopying`: If  , the contents located at the passed-in URL are copied into a file located in the directory used for the autosaved contents of untitled documents.
- `displayNameOrNil`: If not   then this value is used to derive a display name for the new document that does not match one that is already in use by an open document.

## See Also

- [func document(for: URL) -> NSDocument?](nsdocumentcontroller/document(for:)-i5zi.md)
  Returns, for a given URL, the open document whose file or file package is located by the URL, or `nil` if there is no such open document.
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
- [func reopenDocument(for: URL?, withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](nsdocumentcontroller/reopendocument(for:withcontentsof:display:completionhandler:).md)
  Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/duplicatedocument(withcontentsof:copying:displayname:))*