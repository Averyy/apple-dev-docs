# fileModificationDate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The date and time your app last modified the document file.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var fileModificationDate: Date? { get set }
```

```objc
@property (copy, nullable) NSDate * fileModificationDate;
```

#### Discussion

The modification date is updated by the [`open(completionHandler:)`](./open%28completionhandler%29.md), [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md), and [`revert(toContentsOf:completionHandler:)`](./revert%28tocontentsof,completionhandler%29.md) methods. Its value is `nil` if none of these methods has completed successfully at least once. If you override any of these methods, you should be sure to set this property in your implementation.

UIKit sets this property before it calls the completion handlers of the [`open(completionHandler:)`](./open%28completionhandler%29.md), [`save(to:for:completionHandler:)`](./save%28to,for,completionhandler%29.md), and [`revert(toContentsOf:completionHandler:)`](./revert%28tocontentsof,completionhandler%29.md). If, outside of these methods or their completion handlers, you want to wait for any pending file operations to complete before you access this property, you can call [`performAsynchronousFileAccess(_:)`](./performasynchronousfileaccess%28_%29.md) and access the property value in the block parameter.

> ❗ **Important**:  This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [Describing use of required reason API](../../BundleResources/describing-use-of-required-reason-api.md).

## See Also

### Accessing document attributes
- [var fileURL: URL](./fileurl.md)
  The file URL you use to initialize the document.
- [var localizedName: String](./localizedname.md)
  The localized name of the document.
- [var fileType: String?](./filetype.md)
  The file type of the document.
- [var documentState: UIDocument.State](./documentstate.md)
  The current state of the document.
- [var progress: Progress?](./progress.md)
  The upload or download progress of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/filemodificationdate)*