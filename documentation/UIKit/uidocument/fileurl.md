# fileURL

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The file URL you use to initialize the document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var fileURL: URL { get }
```

```objc
@property (readonly) NSURL * fileURL;
```

#### Discussion

The URL identifies the location of the document in the application sandbox. It includes the file extension, from which the file type is determined.

UIKit sets this property before it calls the completion handlers of the [`open(completionHandler:)`](./open%28completionhandler%29.md), [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md), and [`revert(toContentsOf:completionHandler:)`](./revert%28tocontentsof,completionhandler%29.md). If, outside of these methods or their completion handlers, you want to wait for any pending file operations to complete before you access this property, you can call [`performAsynchronousFileAccess(_:)`](./performasynchronousfileaccess%28_%29.md) and access the property value in the block parameter.

## See Also

### Related Documentation
- [init(fileURL: URL)](./init%28fileurl%29.md)
  Returns a document object initialized with its file-system location.
### Accessing document attributes
- [var localizedName: String](./localizedname.md)
  The localized name of the document.
- [var fileType: String?](./filetype.md)
  The file type of the document.
- [var fileModificationDate: Date?](./filemodificationdate.md)
  The date and time your app last modified the document file.
- [var documentState: UIDocument.State](./documentstate.md)
  The current state of the document.
- [var progress: Progress?](./progress.md)
  The upload or download progress of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/fileurl)*