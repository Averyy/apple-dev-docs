# savingFileType

**Framework**: UIKit  
**Kind**: property

Returns the file type to use for saving a document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var savingFileType: String? { get }
```

#### Return Value

A Uniform Type Identifier (UTI) identifying a document type (for example, PDF or HTML).

#### Discussion

The default implementation returns the current file type obtained from the [`fileType`](uidocument/filetype.md) property. The default implementation of the [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) method appends an extension to the file URL that’s based on the file type. So if you want to move the document to a new type and extension, you can override this method to supply that file type.

## See Also

- [func close(completionHandler: ((Bool) -> Void)?)](uidocument/close(completionhandler:).md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](uidocument/contents(fortype:).md)
  Returns the document data to be saved.
- [func save(to: URL, for: UIDocument.SaveOperation, completionHandler: ((Bool) -> Void)?)](uidocument/save(to:for:completionhandler:).md)
  Saves document data to the specified location in the application sandbox.
- [func writeContents(Any, andAttributes: [AnyHashable : Any]?, safelyTo: URL, for: UIDocument.SaveOperation) throws](uidocument/writecontents(_:andattributes:safelyto:for:).md)
  Ensures that document data is written safely to a specified location in the application sandbox.
- [func writeContents(Any, to: URL, for: UIDocument.SaveOperation, originalContentsURL: URL?) throws](uidocument/writecontents(_:to:for:originalcontentsurl:).md)
  Writes the document data to disk at the sandbox location indicated by a file URL.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](uidocument/fileattributestowrite(to:for:).md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](uidocument/filenameextension(fortype:saveoperation:).md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/savingfiletype)*