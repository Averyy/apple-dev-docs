# documentState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current state of the document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var documentState: UIDocument.State { get }
```

```objc
@property (readonly) UIDocumentState documentState;
```

## Discussion

When document state changes, the [`UIDocument`](../uidocument.md) object stores a constant identifying the new state in this property. See the [`UIDocument.State`](./state.md) enum for descriptions of these constants. To receive notifications about changes in document state, observe the [`stateChangedNotification`](./statechangednotification.md) notification.

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
- [var progress: Progress?](./progress.md)
  The upload or download progress of a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/documentstate)*