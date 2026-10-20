# fileWrapper

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text attachment’s file wrapper.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var fileWrapper: FileWrapper? { get set }
```

```objc
@property (strong, nullable) NSFileWrapper * fileWrapper;
```

#### Discussion

The file wrapper holds the contents of the attached file. In iOS, modifying this property has a side effect of invalidating the [`image`](./image.md), [`contents`](./contents.md), and [`fileType`](./filetype.md) properties.

## See Also

### Defining the attachment’s contents
- [var bounds: CGRect](./bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var contents: Data?](./contents.md)
  The contents for the text attachment.
- [var fileType: String?](./filetype.md)
  The file type of the contents for the text attachment.
- [var image: NSImage?](./image.md)
  An instance of the relevant image class that represents the contents of the text attachment object.
- [var allowsTextAttachmentView: Bool](./allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](./usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](./linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/filewrapper)*