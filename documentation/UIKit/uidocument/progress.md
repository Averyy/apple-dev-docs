# progress

**Framework**: UIKit  
**Kind**: property

The upload or download progress of a document.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var progress: Progress? { get }
```

#### Discussion

The value of this property is valid while [`progressAvailable`](uidocument/state/progressavailable.md) is set.

## See Also

- [var fileURL: URL](uidocument/fileurl.md)
  The file URL you use to initialize the document.
- [var localizedName: String](uidocument/localizedname.md)
  The localized name of the document.
- [var fileType: String?](uidocument/filetype.md)
  The file type of the document.
- [var fileModificationDate: Date?](uidocument/filemodificationdate.md)
  The date and time your app last modified the document file.
- [var documentState: UIDocument.State](uidocument/documentstate.md)
  The current state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/progress)*