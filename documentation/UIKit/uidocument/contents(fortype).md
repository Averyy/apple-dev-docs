# contents(forType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the document data to be saved.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func contents(forType typeName: String) throws -> Any
```

```objc
- (id) contentsForType:(NSString *) typeName error:(NSError **) outError;
```

#### Return Value

The document data to be saved, or `nil` if you cannot return document data. The returned object is typically an instance of the [`NSData`](../../Foundation/nsdata.md) class for flat files or the [`FileWrapper`](../../Foundation/filewrapper.md) class for file packages. If you return `nil`, you should also return an error object in `outError`.

If you return an object other than an [`NSData`](../../Foundation/nsdata.md) or [`FileWrapper`](../../Foundation/filewrapper.md) object, you must override the [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md) or [`writeContents(_:to:for:originalContentsURL:)`](./writecontents%28_,to,for,originalcontentsurl%29.md) method to handle the writing of data.

#### Discussion

When you subclass [`UIDocument`](../uidocument.md), override this method to provide UIKit with the document data for saving.

This method is called on the queue that the [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md) method was called on (typically, the main queue). Writing of data occurs on a background queue. The default implementation of this method returns `nil`.

When you return a non-`nil` value in the `outError` parameter, the completion handlers for the following methods don’t get called:

- [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md)
- [`autosave(completionHandler:)`](./autosave%28completionhandler%29.md)
- [`close(completionHandler:)`](./close%28completionhandler%29.md)

Instead, in this case, the error is available to your app in the [`handleError(_:userInteractionPermitted:)`](./handleerror%28_,userinteractionpermitted%29.md) method and in the [`stateChangedNotification`](./statechangednotification.md) notification.

If you want more control over the saving operation than this method provides—for example, if you want to perform incremental writing of data — override, instead, one of the lower-level data-writing methods such as [`writeContents(_:andAttributes:safelyTo:for:)`](./writecontents%28_,andattributes,safelyto,for%29.md) or [`writeContents(_:to:for:originalContentsURL:)`](./writecontents%28_,to,for,originalcontentsurl%29.md). These methods are called on a background thread.

> **Handling Errors in Swift**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `typeName`: The file type of the document, a Uniform Type Identifier (UTI). This string typically derives from the [`fileType`](./filetype.md) property. If you want to save the document under a different UTI, you can override the [`savingFileType`](./savingfiletype.md) method.

## See Also

### Related Documentation
- [func open(completionHandler: ((Bool) -> Void)?)](./open%28completionhandler%29.md)
  Opens a document asynchronously.
- [func revert(toContentsOf: URL, completionHandler: ((Bool) -> Void)?)](./revert%28tocontentsof,completionhandler%29.md)
  Reverts a document to the most recent document data stored on-disk.
### Writing document data
- [func close(completionHandler: ((Bool) -> Void)?)](./close%28completionhandler%29.md)
  Asynchronously closes the document after saving any changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/contents(fortype:))*