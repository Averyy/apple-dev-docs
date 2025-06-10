# writeContents(_:andAttributes:safelyTo:for:)

**Framework**: UIKit  
**Kind**: method

Ensures that document data is written safely to a specified location in the application sandbox.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func writeContents(_ contents: Any, andAttributes additionalFileAttributes: [AnyHashable : Any]? = nil, safelyTo url: URL, for saveOperation: UIDocument.SaveOperation) throws
```

#### Discussion

This method is called by the [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) method to save the file data (and associated attributes in the case of an [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper)). It creates temporary files and directories as necessary so that successful saves can be completed atomically and failed saves can be rolled back cleanly. This method calls [`writeContents(_:to:for:originalContentsURL:)`](uidocument/writecontents(_:to:for:originalcontentsurl:).md) to save the `contents` object, passing the location for the new saved file in the `toURL` parameter and the location of the previously existing file in the `originalContentsURL` parameter, if this is an overwrite operation.

If you want to change how file data is saved, you generally override the [`writeContents(_:to:for:originalContentsURL:)`](uidocument/writecontents(_:to:for:originalcontentsurl:).md) method instead of this method. Additionally, you don’t need to call this method directly unless you are overriding the [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) method.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `contents`: If the object encapsulating the document data is of some other type, you should override this method or   to perform the actual writing of the data.
- `additionalFileAttributes`: A dictionary of   file attributes to assign to the document file. The default implementation obtains these file attributes by calling  .
- `url`: The file URL specifying the location of the document file in the application sandbox.
- `saveOperation`: A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See   for details.

## See Also

- [func close(completionHandler: ((Bool) -> Void)?)](uidocument/close(completionhandler:).md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](uidocument/contents(fortype:).md)
  Returns the document data to be saved.
- [func save(to: URL, for: UIDocument.SaveOperation, completionHandler: ((Bool) -> Void)?)](uidocument/save(to:for:completionhandler:).md)
  Saves document data to the specified location in the application sandbox.
- [func writeContents(Any, to: URL, for: UIDocument.SaveOperation, originalContentsURL: URL?) throws](uidocument/writecontents(_:to:for:originalcontentsurl:).md)
  Writes the document data to disk at the sandbox location indicated by a file URL.
- [var savingFileType: String?](uidocument/savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](uidocument/fileattributestowrite(to:for:).md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](uidocument/filenameextension(fortype:saveoperation:).md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/writecontents(_:andattributes:safelyto:for:))*