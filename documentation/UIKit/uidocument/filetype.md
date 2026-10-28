# fileType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The file type of the document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var fileType: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * fileType;
```

## Discussion

The file type is a uniform type identifier (UTI). UIKit derives the UTI from the filename-extension component of [`fileURL`](./fileurl.md).

UIKit sets this property before it calls the completion handlers of the [`open(completionHandler:)`](./open%28completionhandler%29.md), [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md), and [`revert(toContentsOf:completionHandler:)`](./revert%28tocontentsof,completionhandler%29.md). If, outside of these methods or their completion handlers, you want to wait for any pending file operations to complete before you access this property, you can call [`performAsynchronousFileAccess(_:)`](./performasynchronousfileaccess%28_%29.md) and access the property value in the block parameter.

## See Also

### Accessing document attributes
- [var fileURL: URL](./fileurl.md)
  The file URL you use to initialize the document.
- [var localizedName: String](./localizedname.md)
  The localized name of the document.
- [var fileModificationDate: Date?](./filemodificationdate.md)
  The date and time your app last modified the document file.
- [var documentState: UIDocument.State](./documentstate.md)
  The current state of the document.
- [var progress: Progress?](./progress.md)
  The upload or download progress of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/filetype)*