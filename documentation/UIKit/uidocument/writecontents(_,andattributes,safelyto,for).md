# writeContents(_:andAttributes:safelyTo:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Ensures that document data is written safely to a specified location in the application sandbox.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func writeContents(_ contents: Any, andAttributes additionalFileAttributes: [AnyHashable : Any]? = nil, safelyTo url: URL, for saveOperation: UIDocument.SaveOperation) throws
```

```objc
- (BOOL) writeContents:(id) contents andAttributes:(NSDictionary *) additionalFileAttributes safelyToURL:(NSURL *) url forSaveOperation:(UIDocumentSaveOperation) saveOperation error:(NSError **) outError;
```

#### Discussion

This method is called by the [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) method to save the file data (and associated attributes in the case of an [`FileWrapper`](../../Foundation/filewrapper.md)). It creates temporary files and directories as necessary so that successful saves can be completed atomically and failed saves can be rolled back cleanly. This method calls [`writeContents(_:to:for:originalContentsURL:)`](./writecontents%28_,to,for,originalcontentsurl%29.md) to save the `contents` object, passing the location for the new saved file in the `toURL` parameter and the location of the previously existing file in the `originalContentsURL` parameter, if this is an overwrite operation.

If you want to change how file data is saved, you generally override the [`writeContents(_:to:for:originalContentsURL:)`](./writecontents%28_,to,for,originalcontentsurl%29.md) method instead of this method. Additionally, you don’t need to call this method directly unless you are overriding the [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) method.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `contents`: The document data to write to disk. Typically, the data is encapsulated by an [`NSData`](../../Foundation/nsdata.md) object (if a flat file) or an [`FileWrapper`](../../Foundation/filewrapper.md) object (if a file package).

  If the object encapsulating the document data is of some other type, you should override this method or [`writeContents(_:to:for:originalContentsURL:)`](./writecontents%28_,to,for,originalcontentsurl%29.md) to perform the actual writing of the data.
- `additionalFileAttributes`: A dictionary of [`FileManager`](../../Foundation/filemanager.md) file attributes to assign to the document file. The default implementation obtains these file attributes by calling [`fileAttributesToWrite(to:for:)`](./fileattributestowrite%28to,for%29.md).
- `url`: The file URL specifying the location of the document file in the application sandbox.
- `saveOperation`: A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See [`UIDocument.SaveOperation`](./saveoperation.md) for details.

## See Also

### Writing document data
- [func close(completionHandler: ((Bool) -> Void)?)](./close%28completionhandler%29.md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](./contents%28fortype%29.md)
  Returns the document data to be saved.
- [func save(to: URL, for: UIDocument.SaveOperation, completionHandler: ((Bool) -> Void)?)](./save%28to,for,completionhandler%29.md)
  Saves document data to the specified location in the application sandbox.
- [func writeContents(Any, to: URL, for: UIDocument.SaveOperation, originalContentsURL: URL?) throws](./writecontents%28_,to,for,originalcontentsurl%29.md)
  Writes the document data to disk at the sandbox location indicated by a file URL.
- [var savingFileType: String?](./savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](./fileattributestowrite%28to,for%29.md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](./filenameextension%28fortype,saveoperation%29.md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/writecontents(_:andattributes:safelyto:for:))*