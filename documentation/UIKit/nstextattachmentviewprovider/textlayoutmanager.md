# textLayoutManager

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (weak, readonly, nullable) NSTextLayoutManager * textLayoutManager;
```

## Discussion

Specify the value of this property at initialization time using the [`init(textAttachment:parentView:textLayoutManager:location:)`](./init%28textattachment,parentview,textlayoutmanager,location%29.md) initializer.

## See Also

### Defining the contents
- [var location: any NSTextLocation](./location.md)
  The location that indicates the start of the text attachment.
- [var textAttachment: NSTextAttachment?](./textattachment.md)
  The text attachment for this view.
- [var tracksTextAttachmentViewBounds: Bool](./trackstextattachmentviewbounds.md)
  A Boolean value that determines the text attachment’s bounds policy.
- [var view: UIView?](./view.md)
  The text attachment’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/textlayoutmanager)*