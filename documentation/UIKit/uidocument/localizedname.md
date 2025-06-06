# localizedName

**Framework**: UIKit  
**Kind**: property

The localized name of the document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var localizedName: String { get }
```

#### Discussion

By default, UIKit obtains the value from the filename component of [`fileURL`](uidocument/fileurl.md). You can override the getter accessor method of this property to provide a custom name for presentation to the user, such as in error strings. See [`UIDocument`](uidocument.md) for overriding advice.

UIKit sets this property before it calls the completion handlers of the [`open(completionHandler:)`](uidocument/open(completionhandler:).md), [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md), and [`revert(toContentsOf:completionHandler:)`](uidocument/revert(tocontentsof:completionhandler:).md). If, outside of these methods or their completion handlers, you want to wait for any pending file operations to complete before you access this property, you can call [`performAsynchronousFileAccess(_:)`](uidocument/performasynchronousfileaccess(_:).md) and access the property value in the block parameter.

## See Also

- [var fileURL: URL](uidocument/fileurl.md)
  The file URL you use to initialize the document.
- [var fileType: String?](uidocument/filetype.md)
  The file type of the document.
- [var fileModificationDate: Date?](uidocument/filemodificationdate.md)
  The date and time your app last modified the document file.
- [var documentState: UIDocument.State](uidocument/documentstate.md)
  The current state of the document.
- [var progress: Progress?](uidocument/progress.md)
  The upload or download progress of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/localizedname)*