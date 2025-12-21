# save(to:for:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Saves document data to the specified location in the application sandbox.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func save(to url: URL, for saveOperation: UIDocument.SaveOperation) async -> Bool
```

#### Discussion

The default implementation of this method first calls the [`contents(forType:)`](uidocument/contents(fortype:).md) method synchronously on the calling queue to get the document data to save. Then it calls the [`writeContents(_:andAttributes:safelyTo:for:)`](uidocument/writecontents(_:andattributes:safelyto:for:).md) method on a background queue to perform the actual writing of the data to disk.

If you override this method, it’s recommended that you first call the superclass implementation of the method (`super`). If you do not call `super`, you must do two things:

- Call [`performAsynchronousFileAccess(_:)`](uidocument/performasynchronousfileaccess(_:).md) to put the save operation on a background queue.
- In the block parameter, implement coordinated writing by using the [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator) class.
- From within the coordinated write, call [`writeContents(_:andAttributes:safelyTo:for:)`](uidocument/writecontents(_:andattributes:safelyto:for:).md).

## Parameters

- `url`: The file URL identifying the location in the application sandbox to write the document data to. Typically, this is the URL obtained from the   property.
- `saveOperation`: A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See   for details.
- `completionHandler`: This block is invoked on the calling queue.

## See Also

- [func close(completionHandler: ((Bool) -> Void)?)](uidocument/close(completionhandler:).md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](uidocument/contents(fortype:).md)
  Returns the document data to be saved.
- [func writeContents(Any, andAttributes: [AnyHashable : Any]?, safelyTo: URL, for: UIDocument.SaveOperation) throws](uidocument/writecontents(_:andattributes:safelyto:for:).md)
  Ensures that document data is written safely to a specified location in the application sandbox.
- [func writeContents(Any, to: URL, for: UIDocument.SaveOperation, originalContentsURL: URL?) throws](uidocument/writecontents(_:to:for:originalcontentsurl:).md)
  Writes the document data to disk at the sandbox location indicated by a file URL.
- [var savingFileType: String?](uidocument/savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](uidocument/fileattributestowrite(to:for:).md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](uidocument/filenameextension(fortype:saveoperation:).md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/save(to:for:completionhandler:))*