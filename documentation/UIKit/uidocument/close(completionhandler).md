# close(completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously closes the document after saving any changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func close(completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func close() async -> Bool
```

```objc
- (void) closeWithCompletionHandler:(void (^)(BOOL success)) completionHandler;
```

#### Discussion

You call this method to begin the sequence of method calls that saves a document safely and asynchronously. The file-system location of the document derives from the [`fileURL`](./fileurl.md) property. After the save operation concludes, the code in `completionHandler` is executed. In this code, you can close the document — for example, by removing the document’s view from the screen. Additionally, if the save operation didn’t succeed (`success` is [`false`](../../Swift/false.md)), you can respond in an appropriate manner.

You typically wouldn’t override this method. The default implementation calls the [`autosave(completionHandler:)`](./autosave%28completionhandler%29.md) method.

## Parameters

- `completionHandler`: A block with code to execute after the save-and-close operation concludes. The block returns no value and has one parameter:

  - **`success`**: [`true`](../../Swift/true.md) if any save operation succeeds, otherwise [`false`](../../Swift/false.md).

  The block is invoked on the main queue.

## See Also

### Writing document data
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
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](./filenameextension%28fortype,saveoperation%29.md)
  Returns a file extension to append to the file URL of the document file being written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/close(completionhandler:))*