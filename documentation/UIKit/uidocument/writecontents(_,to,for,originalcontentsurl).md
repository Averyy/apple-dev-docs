# writeContents(_:to:for:originalContentsURL:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) writeContents:(id) contents toURL:(NSURL *) url forSaveOperation:(UIDocumentSaveOperation) saveOperation originalContentsURL:(NSURL *) originalContentsURL error:(NSError **) outError;
```

#### Discussion

This method is called by the [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md) to write the actual file data. It is passed the contents object returned from your [`contents(forType:)`](./contents%28fortype%29.md) implementation. The default implementation of this method supports [`NSData`](../../Foundation/nsdata.md) or [`FileWrapper`](../../Foundation/filewrapper.md) contents by asking the contents object to save itself to the corresponding URL.

If you override this method, you may choose to return a different type of data from [`contents(forType:)`](./contents%28fortype%29.md) or you may choose to not override [`contents(forType:)`](./contents%28fortype%29.md) and generate the writable data directly within this method. If you override this method, you should not invoke the superclass implementation.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `contents`: The document data to write to disk. Typically, the data is encapsulated by an [`NSData`](../../Foundation/nsdata.md) object (if a flat file) or an [`FileWrapper`](../../Foundation/filewrapper.md) object (if a file package).

  If the object encapsulating the document data is of some other type, you should override this method or [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md) to perform the actual writing of the data.
- `url`: A file URL specifying the location of the document file in the application sandbox.
- `saveOperation`: A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See [`UIDocument.SaveOperation`](./saveoperation.md) for details.
- `originalContentsURL`: A file URL specifying the previous location of the document file (if not `nil`).

## See Also

### Writing document data
- [func close(completionHandler: ((Bool) -> Void)?)](./close%28completionhandler%29.md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](./contents%28fortype%29.md)
  Returns the document data to be saved.
- [func save(to: URL, for: UIDocument.SaveOperation, completionHandler: ((Bool) -> Void)?)](./save%28to,for,completionhandler%29.md)
  Saves document data to the specified location in the application sandbox.
- [func writeContents(Any, andAttributes: [AnyHashable : Any]?, safelyTo: URL, for: UIDocument.SaveOperation) throws](./writecontents%28_,andattributes,safelyto,for%29.md)
  Ensures that document data is written safely to a specified location in the application sandbox.
- [var savingFileType: String?](./savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](./fileattributestowrite%28to,for%29.md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](./filenameextension%28fortype,saveoperation%29.md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/writecontents(_:to:for:originalcontentsurl:))*