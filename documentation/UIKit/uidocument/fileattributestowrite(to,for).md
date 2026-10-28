# fileAttributesToWrite(to:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary of file attributes to associate with the document file when writing or updating it.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func fileAttributesToWrite(to url: URL, for saveOperation: UIDocument.SaveOperation) throws -> [AnyHashable : Any]
```

```objc
- (NSDictionary *) fileAttributesToWriteToURL:(NSURL *) url forSaveOperation:(UIDocumentSaveOperation) saveOperation error:(NSError **) outError;
```

## Return Value

A dictionary of file attributes — for example, level of file protection and creation date. See [`FileManager`](../../Foundation/filemanager.md) for more information about file attributes.

## Discussion

The attributes are associated with a specific file type and save operation. You can override this method to return a dictionary of file attributes that are different than the default file attribute, which for new files is [`extensionHidden`](../../Foundation/fileattributekey/extensionhidden.md).

The [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) calls this method before executing asynchronous writing. It passes the dictionary into [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md) when it calls that method to write the document file.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: A file URL locating the document in the application sandbox.
- `saveOperation`: A constant that indicates whether the document file is being written the first time or whether it’s being overwritten. See [`UIDocument.SaveOperation`](./saveoperation.md) for details.

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
- [func writeContents(Any, to: URL, for: UIDocument.SaveOperation, originalContentsURL: URL?) throws](./writecontents%28_,to,for,originalcontentsurl%29.md)
  Writes the document data to disk at the sandbox location indicated by a file URL.
- [var savingFileType: String?](./savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](./filenameextension%28fortype,saveoperation%29.md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/fileattributestowrite(to:for:))*