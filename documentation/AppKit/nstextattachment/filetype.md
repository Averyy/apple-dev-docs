# fileType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The file type of the contents for the text attachment.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var fileType: String? { get set }
```

```objc
@property (copy, nullable) NSString * fileType;
```

#### Discussion

Modifying this property has the side effect of invalidating the [`image`](./image.md) property.

## See Also

### Defining the attachment’s contents
- [var bounds: CGRect](./bounds.md)
  The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [var contents: Data?](./contents.md)
  The contents for the text attachment.
- [var image: NSImage?](./image.md)
  An instance of the relevant image class that represents the contents of the text attachment object.
- [var fileWrapper: FileWrapper?](./filewrapper.md)
  The text attachment’s file wrapper.
- [var allowsTextAttachmentView: Bool](./allowstextattachmentview.md)
  A Boolean value that determines whether the text attachment uses text attachment views.
- [var usesTextAttachmentView: Bool](./usestextattachmentview.md)
  A Boolean value that indicates whether the text attachment uses text attachment views.
- [var lineLayoutPadding: CGFloat](./linelayoutpadding.md)
  The layout padding before and after the text attachment bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/filetype)*