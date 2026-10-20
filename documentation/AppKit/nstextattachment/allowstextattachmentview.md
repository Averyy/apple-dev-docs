# allowsTextAttachmentView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the text attachment uses text attachment views.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var allowsTextAttachmentView: Bool { get set }
```

```objc
@property BOOL allowsTextAttachmentView;
```

#### Discussion

When `true`, the text attachment tries to use a text attachment view returned by [`viewProvider(for:location:textContainer:)`](../nstextattachmentlayout/viewprovider%28for,location,textcontainer%29.md). Default is `true`.

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
- [var fileWrapper: FileWrapper?](./filewrapper.md)
  The text attachment’s file wrapper.
- [var usesTextAttachmentView: Bool](./usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](./linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/allowstextattachmentview)*