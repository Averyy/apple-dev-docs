# image

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, nullable) UIImage * image;
```

## Discussion

For details about using the [`UIImage`](../uiimage.md) class to create text attachments that automatically adjust to surrounding font and color attributes, see the [`init(image:)`](./init%28image%29.md) initializer.

## See Also

### Defining the attachment’s contents
- [var bounds: CGRect](./bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var contents: Data?](./contents.md)
  The contents for the text attachment.
- [var fileType: String?](./filetype.md)
  The file type of the contents for the text attachment.
- [var fileWrapper: FileWrapper?](./filewrapper.md)
  The text attachment’s file wrapper.
- [var allowsTextAttachmentView: Bool](./allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](./usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](./linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachment/image)*