# contents

**Framework**: AppKit  
**Kind**: property

The contents for the text attachment.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var contents: Data? { get set }
```

#### Discussion

Modifying this property has the side effect of invalidating the [`image`](nstextattachment/image.md) property.

## See Also

- [var bounds: CGRect](nstextattachment/bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var fileType: String?](nstextattachment/filetype.md)
  The file type of the contents for the text attachment.
- [var image: NSImage?](nstextattachment/image.md)
  An instance of the relevant image class that represents the contents of the text attachment object.
- [var fileWrapper: FileWrapper?](nstextattachment/filewrapper.md)
  The text attachment’s file wrapper.
- [var allowsTextAttachmentView: Bool](nstextattachment/allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](nstextattachment/usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](nstextattachment/linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/contents)*