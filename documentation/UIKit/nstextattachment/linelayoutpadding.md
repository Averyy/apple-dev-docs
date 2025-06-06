# lineLayoutPadding

**Framework**: UIKit  
**Kind**: property

The layout padding before and after the text attachment bounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var lineLayoutPadding: CGFloat { get set }
```

#### Discussion

The layout and rendering bounds X origin is inset by the padding value. This affects the relationship between the text attachment bounds and `NSLayoutManager` glyph metrics methods [`location(forGlyphAt:)`](nslayoutmanager/location(forglyphat:).md) and [`attachmentSize(forGlyphAt:)`](nslayoutmanager/attachmentsize(forglyphat:).md). The default value is `0.0`.

## See Also

- [var bounds: CGRect](nstextattachment/bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var contents: Data?](nstextattachment/contents.md)
  The contents for the text attachment.
- [var fileType: String?](nstextattachment/filetype.md)
  The file type of the contents for the text attachment.
- [var image: UIImage?](nstextattachment/image.md)
  An instance of the relevant image class that represents the contents of the text attachment object.
- [var fileWrapper: FileWrapper?](nstextattachment/filewrapper.md)
  The text attachment’s file wrapper.
- [var allowsTextAttachmentView: Bool](nstextattachment/allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](nstextattachment/usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachment/linelayoutpadding)*