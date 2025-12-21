# writeContents(_:to:for:originalContentsURL:)

**Framework**: UIKit  
**Kind**: method

Writes the document data to disk at the sandbox location indicated by a file URL.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func writeContents(_ contents: Any, to url: URL, for saveOperation: UIDocument.SaveOperation, originalContentsURL: URL?) throws
```

#### Discussion

This method is called by the [`writeContents(_:andAttributes:safelyTo:for:)`](uidocument/writecontents(_:andattributes:safelyto:for:).md) to write the actual file data. It is passed the contents object returned from your [`contents(forType:)`](uidocument/contents(fortype:).md) implementation. The default implementation of this method supports [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) or [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) contents by asking the contents object to save itself to the corresponding URL.

If you override this method, you may choose to return a different type of data from [`contents(forType:)`](uidocument/contents(fortype:).md) or you may choose to not override [`contents(forType:)`](uidocument/contents(fortype:).md) and generate the writable data directly within this method. If you override this method, you should not invoke the superclass implementation.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `contents`: If the object encapsulating the document data is of some other type, you should override this method or   to perform the actual writing of the data.
- `url`: A file URL specifying the location of the document file in the application sandbox.
- `saveOperation`: A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See   for details.
- `originalContentsURL`: A file URL specifying the previous location of the document file (if not  ).

## See Also

- [func close(completionHandler: ((Bool) -> Void)?)](uidocument/close(completionhandler:).md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](uidocument/contents(fortype:).md)
  Returns the document data to be saved.
- [func save(to: URL, for: UIDocument.SaveOperation, completionHandler: ((Bool) -> Void)?)](uidocument/save(to:for:completionhandler:).md)
  Saves document data to the specified location in the application sandbox.
- [func writeContents(Any, andAttributes: [AnyHashable : Any]?, safelyTo: URL, for: UIDocument.SaveOperation) throws](uidocument/writecontents(_:andattributes:safelyto:for:).md)
  Ensures that document data is written safely to a specified location in the application sandbox.
- [var savingFileType: String?](uidocument/savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](uidocument/fileattributestowrite(to:for:).md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](uidocument/filenameextension(fortype:saveoperation:).md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/writecontents(_:to:for:originalcontentsurl:))*