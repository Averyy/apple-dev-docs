# openUntitledDocumentAndDisplay(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new untitled document, presents its user interface if `displayDocument` is `true`, and returns the document if successful.

**Availability**:
- macOS

## Declaration

```swift
func openUntitledDocumentAndDisplay(_ displayDocument: Bool) throws -> NSDocument
```

```objc
- (NSDocument *) openUntitledDocumentAndDisplay:(BOOL) displayDocument error:(NSError **) outError;
```

## Return Value

Returns the new [`NSDocument`](../nsdocument.md) object, or `nil` if a new untitled document could not be created. If this method returns `nil`, it also sets the address referenced by `outError` to an `NSError` object that tell why the document could not be created.

## Discussion

The default implementation of this method calls [`defaultType`](./defaulttype.md) to determine the type of new document to create, calls [`makeUntitledDocument(ofType:)`](./makeuntitleddocument%28oftype%29.md) to create it, then calls [`addDocument(_:)`](./adddocument%28_%29.md) to record its opening.

When `displayDocument` is [`true`](../../Swift/true.md), this method sends the new document [`makeWindowControllers()`](../nsdocument/makewindowcontrollers%28%29.md) and [`showWindows()`](../nsdocument/showwindows%28%29.md) messages. In this scenario, [`showWindows()`](../nsdocument/showwindows%28%29.md) shows only the window controllers that have been assigned to the document.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `displayDocument`: [`true`](../../Swift/true.md) if the user interface for the document should be shown, otherwise [`false`](../../Swift/false.md).

## See Also

### Creating and Opening Documents
- [func document(for: URL) -> NSDocument?](./document%28for%29-i5zi.md)
  Returns, for a given URL, the open document whose file or file package is located by the URL, or `nil` if there is no such open document.
- [func duplicateDocument(withContentsOf: URL, copying: Bool, displayName: String?) throws -> NSDocument](./duplicatedocument%28withcontentsof,copying,displayname%29.md)
  Creates a new document by reading the contents for the document from another URL, presents its user interface, and returns the document if successful.
- [func openDocument(withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](./opendocument%28withcontentsof,display,completionhandler%29.md)
  Opens a document located by a URL, optionally presents its user interface, and calls the passed-in completion handler.
- [func makeDocument(for: URL?, withContentsOf: URL, ofType: String) throws -> NSDocument](./makedocument%28for,withcontentsof,oftype%29.md)
  Instantiates a document located by a URL, of a specified type, but by reading the contents for the document from another URL, and returns it if successful.
- [func makeDocument(withContentsOf: URL, ofType: String) throws -> NSDocument](./makedocument%28withcontentsof,oftype%29.md)
  Instantiates a document located by a URL, of a specified type, and returns it if successful.
- [func makeUntitledDocument(ofType: String) throws -> NSDocument](./makeuntitleddocument%28oftype%29.md)
  Instantiates a new untitled document of the specified type and returns it if successful.
- [func reopenDocument(for: URL?, withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](./reopendocument%28for,withcontentsof,display,completionhandler%29.md)
  Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/openuntitleddocumentanddisplay(_:))*