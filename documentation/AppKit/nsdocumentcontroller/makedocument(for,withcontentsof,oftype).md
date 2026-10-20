# makeDocument(for:withContentsOf:ofType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Instantiates a document located by a URL, of a specified type, but by reading the contents for the document from another URL, and returns it if successful.

**Availability**:
- macOS

## Declaration

```swift
func makeDocument(for urlOrNil: URL?, withContentsOf contentsURL: URL, ofType typeName: String) throws -> NSDocument
```

```objc
- (NSDocument *) makeDocumentForURL:(NSURL *) urlOrNil withContentsOfURL:(NSURL *) contentsURL ofType:(NSString *) typeName error:(NSError **) outError;
```

#### Return Value

The newly created [`NSDocument`](../nsdocument.md) object, or `nil` if the document could not be created.

#### Discussion

The URL is specified by `absoluteDocumentURL`, the type by `typeName`, and the other URL providing the contents by `absoluteDocumentContentsURL`. If not successful, the method returns `nil` after setting `outError` to point to an `NSError` object that encapsulates the reason why the document could not be instantiated. The default implementation of this method calls [`documentClass(forType:)`](./documentclass%28fortype%29.md) to find out the class of document to instantiate, allocates a document object, and initializes it by sending it an [`init(for:withContentsOf:ofType:)`](../nsdocument/init%28for,withcontentsof,oftype%29.md) message.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `urlOrNil`: The location of the new document object.
- `contentsURL`: The URL of the file that provides the contents for the new document.
- `typeName`: The type of the document.

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
- [func makeDocument(withContentsOf: URL, ofType: String) throws -> NSDocument](./makedocument%28withcontentsof,oftype%29.md)
  Instantiates a document located by a URL, of a specified type, and returns it if successful.
- [func makeUntitledDocument(ofType: String) throws -> NSDocument](./makeuntitleddocument%28oftype%29.md)
  Instantiates a new untitled document of the specified type and returns it if successful.
- [func reopenDocument(for: URL?, withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](./reopendocument%28for,withcontentsof,display,completionhandler%29.md)
  Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/makedocument(for:withcontentsof:oftype:))*