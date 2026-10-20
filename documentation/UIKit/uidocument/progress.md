# progress

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The upload or download progress of a document.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var progress: Progress? { get }
```

```objc
@property (readonly, nullable) NSProgress * progress;
```

#### Discussion

The value of this property is valid while [`progressAvailable`](./state/progressavailable.md) is set.

## See Also

### Accessing document attributes
- [var fileURL: URL](./fileurl.md)
  The file URL you use to initialize the document.
- [var localizedName: String](./localizedname.md)
  The localized name of the document.
- [var fileType: String?](./filetype.md)
  The file type of the document.
- [var fileModificationDate: Date?](./filemodificationdate.md)
  The date and time your app last modified the document file.
- [var documentState: UIDocument.State](./documentstate.md)
  The current state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/progress)*