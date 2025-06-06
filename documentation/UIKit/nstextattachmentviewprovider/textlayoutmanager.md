# textLayoutManager

**Framework**: UIKit  
**Kind**: property

The text layout manager for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var textLayoutManager: NSTextLayoutManager? { get }
```

#### Discussion

Specify the value of this property at initialization time using the [`init(textAttachment:parentView:textLayoutManager:location:)`](nstextattachmentviewprovider/init(textattachment:parentview:textlayoutmanager:location:).md) initializer.

## See Also

- [var location: any NSTextLocation](nstextattachmentviewprovider/location.md)
  The location that indicates the start of the text attachment.
- [var textAttachment: NSTextAttachment?](nstextattachmentviewprovider/textattachment.md)
  The text attachment for this view.
- [var tracksTextAttachmentViewBounds: Bool](nstextattachmentviewprovider/trackstextattachmentviewbounds.md)
  A Boolean value that determines the text attachment’s bounds policy.
- [var view: UIView?](nstextattachmentviewprovider/view.md)
  The text attachment’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/textlayoutmanager)*