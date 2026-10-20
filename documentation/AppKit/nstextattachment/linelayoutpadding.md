# lineLayoutPadding

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layout padding before and after the text attachment bounds.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var lineLayoutPadding: CGFloat { get set }
```

```objc
@property CGFloat lineLayoutPadding;
```

#### Discussion

The layout and rendering bounds X origin is inset by the padding value. This affects the relationship between the text attachment bounds and `NSLayoutManager` glyph metrics methods [`location(forGlyphAt:)`](../nslayoutmanager/location%28forglyphat%29.md) and [`attachmentSize(forGlyphAt:)`](../nslayoutmanager/attachmentsize%28forglyphat%29.md). The default value is `0.0`.

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
- [var allowsTextAttachmentView: Bool](./allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](./usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/linelayoutpadding)*