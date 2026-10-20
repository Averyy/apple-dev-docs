# savingFileType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSString * savingFileType;
```

#### Return Value

A Uniform Type Identifier (UTI) identifying a document type (for example, PDF or HTML).

#### Discussion

The default implementation returns the current file type obtained from the [`fileType`](./filetype.md) property. The default implementation of the [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) method appends an extension to the file URL that’s based on the file type. So if you want to move the document to a new type and extension, you can override this method to supply that file type.

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
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](./fileattributestowrite%28to,for%29.md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](./filenameextension%28fortype,saveoperation%29.md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/savingfiletype)*