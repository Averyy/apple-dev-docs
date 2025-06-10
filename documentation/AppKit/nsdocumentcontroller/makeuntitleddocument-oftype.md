# makeUntitledDocument(ofType:)

**Framework**: AppKit  
**Kind**: method

Instantiates a new untitled document of the specified type and returns it if successful.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func makeUntitledDocument(ofType typeName: String) throws -> NSDocument
```

#### Discussion

The document type is specified by `typeName`. If not successful, the method returns `nil` after setting `outError` to point to an `NSError` object that encapsulates the reason why a new untitled document could not be instantiated. The default implementation of this method calls [`documentClass(forType:)`](nsdocumentcontroller/documentclass(fortype:).md) to find out the class of document to instantiate, then allocates and initializes a document by sending it [`init(type:)`](nsdocument/init(type:).md).

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `typeName`: The type of the document.

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
- [func reopenDocument(for: URL?, withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](nsdocumentcontroller/reopendocument(for:withcontentsof:display:completionhandler:).md)
  Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/makeuntitleddocument(oftype:))*