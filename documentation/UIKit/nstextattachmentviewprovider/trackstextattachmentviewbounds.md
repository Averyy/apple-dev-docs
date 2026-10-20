# tracksTextAttachmentViewBounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines the text attachment’s bounds policy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var tracksTextAttachmentViewBounds: Bool { get set }
```

```objc
@property BOOL tracksTextAttachmentViewBounds;
```

#### Discussion

If `true`, the framework calls the `textAttachment` property’s [`attachmentBounds(for:location:textContainer:proposedLineFragment:position:)`](./attachmentbounds%28for,location,textcontainer,proposedlinefragment,position%29.md) method and examines the text attachment view provider to determine the bounds instead of using the `bounds` property of this instance. Defaults to `false`.

## See Also

### Defining the contents
- [var location: any NSTextLocation](./location.md)
  The location that indicates the start of the text attachment.
- [var textAttachment: NSTextAttachment?](./textattachment.md)
  The text attachment for this view.
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
  The text layout manager for this view.
- [var view: UIView?](./view.md)
  The text attachment’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/trackstextattachmentviewbounds)*