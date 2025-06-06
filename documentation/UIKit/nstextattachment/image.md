# image

**Framework**: UIKit  
**Kind**: property

An instance of the relevant image class that represents the contents of the text attachment object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var image: UIImage? { get set }
```

#### Discussion

For details about using the [`UIImage`](uiimage.md) class to create text attachments that automatically adjust to surrounding font and color attributes, see the [`init(image:)`](nstextattachment/init(image:).md) initializer.

## See Also

- [var bounds: CGRect](nstextattachment/bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var contents: Data?](nstextattachment/contents.md)
  The contents for the text attachment.
- [var fileType: String?](nstextattachment/filetype.md)
  The file type of the contents for the text attachment.
- [var fileWrapper: FileWrapper?](nstextattachment/filewrapper.md)
  The text attachment’s file wrapper.
- [var allowsTextAttachmentView: Bool](nstextattachment/allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](nstextattachment/usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](nstextattachment/linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachment/image)*