# fileNameExtension(forType:saveOperation:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a file extension to append to the file URL of the document file being written.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func fileNameExtension(forType typeName: String?, saveOperation: UIDocument.SaveOperation) -> String
```

```objc
- (NSString *) fileNameExtensionForType:(NSString *) typeName saveOperation:(UIDocumentSaveOperation) saveOperation;
```

#### Return Value

A string to use as the file extension of the document file.

#### Discussion

The default implementation queries Launch Services to obtain the file extension matching the file (document) type. You can override this method to return a file extension that’s different from the default extension. The default implementation of the [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) method calls this method before it gets the document content and writes the document file to disk.

## Parameters

- `typeName`: A Uniform Type Identifier (UTI) that indicates the type of document (for example, PDF or HTML).
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
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](./fileattributestowrite%28to,for%29.md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/filenameextension(fortype:saveoperation:))*