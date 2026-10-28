# save(to:for:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Saves document data to the specified location in the application sandbox.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func save(to url: URL, for saveOperation: UIDocument.SaveOperation, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func save(to url: URL, for saveOperation: UIDocument.SaveOperation) async -> Bool
```

```objc
- (void) saveToURL:(NSURL *) url forSaveOperation:(UIDocumentSaveOperation) saveOperation completionHandler:(void (^)(BOOL success)) completionHandler;
```

## Discussion

The default implementation of this method first calls the [`contents(forType:)`](./contents%28fortype%29.md) method synchronously on the calling queue to get the document data to save. Then it calls the [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md) method on a background queue to perform the actual writing of the data to disk.

If you override this method, it’s recommended that you first call the superclass implementation of the method (`super`). If you do not call `super`, you must do two things:

- Call [`performAsynchronousFileAccess(_:)`](./performasynchronousfileaccess%28_%29.md) to put the save operation on a background queue.
- In the block parameter, implement coordinated writing by using the [`NSFileCoordinator`](../../Foundation/nsfilecoordinator.md) class.
- From within the coordinated write, call [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md).

## Parameters

- `url`: The file URL identifying the location in the application sandbox to write the document data to. Typically, this is the URL obtained from the [`fileURL`](./fileurl.md) property.
- `saveOperation`: A constant that indicates whether the document file is being written the first time or whether it is being overwritten. See [`UIDocument.SaveOperation`](./saveoperation.md) for details.
- `completionHandler`: A block with code that is executed when the save operation concludes. The block returns no value and has one parameter:

  - **`success`**: [`true`](../../Swift/true.md) if the save operation succeeds, otherwise [`false`](../../Swift/false.md).

  This block is invoked on the calling queue.

## See Also

### Writing document data
- [func close(completionHandler: ((Bool) -> Void)?)](./close%28completionhandler%29.md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](./contents%28fortype%29.md)
  Returns the document data to be saved.
- [func writeContents(Any, andAttributes: [AnyHashable : Any]?, safelyTo: URL, for: UIDocument.SaveOperation) throws](./writecontents%28_,andattributes,safelyto,for%29.md)
  Ensures that document data is written safely to a specified location in the application sandbox.
- [func writeContents(Any, to: URL, for: UIDocument.SaveOperation, originalContentsURL: URL?) throws](./writecontents%28_,to,for,originalcontentsurl%29.md)
  Writes the document data to disk at the sandbox location indicated by a file URL.
- [var savingFileType: String?](./savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](./fileattributestowrite%28to,for%29.md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](./filenameextension%28fortype,saveoperation%29.md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/save(to:for:completionhandler:))*