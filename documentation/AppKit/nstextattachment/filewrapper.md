# fileWrapper

**Framework**: AppKit  
**Kind**: property

The text attachment’s file wrapper.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var fileWrapper: FileWrapper? { get set }
```

#### Discussion

The file wrapper holds the contents of the attached file. In iOS, modifying this property has a side effect of invalidating the [`image`](nstextattachment/image.md), [`contents`](nstextattachment/contents.md), and [`fileType`](nstextattachment/filetype.md) properties.

## See Also

- [var bounds: CGRect](nstextattachment/bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var contents: Data?](nstextattachment/contents.md)
  The contents for the text attachment.
- [var fileType: String?](nstextattachment/filetype.md)
  The file type of the contents for the text attachment.
- [var image: NSImage?](nstextattachment/image.md)
  An instance of the relevant image class that represents the contents of the text attachment object.
- [var allowsTextAttachmentView: Bool](nstextattachment/allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](nstextattachment/usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](nstextattachment/linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/filewrapper)*