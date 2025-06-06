# location

**Framework**: AppKit  
**Kind**: property

The location that indicates the start of the text attachment.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var location: any NSTextLocation { get }
```

#### Discussion

Specify the value of this property at initialization time using the [`init(textAttachment:parentView:textLayoutManager:location:)`](nstextattachmentviewprovider/init(textattachment:parentview:textlayoutmanager:location:).md) initializer.

## See Also

- [var textAttachment: NSTextAttachment?](nstextattachmentviewprovider/textattachment.md)
  The text attachment for this view.
- [var textLayoutManager: NSTextLayoutManager?](nstextattachmentviewprovider/textlayoutmanager.md)
  The text layout manager for this view.
- [var tracksTextAttachmentViewBounds: Bool](nstextattachmentviewprovider/trackstextattachmentviewbounds.md)
  A Boolean value that determines the text attachment’s bounds policy.
- [var view: NSView?](nstextattachmentviewprovider/view.md)
  The text attachment’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentviewprovider/location)*