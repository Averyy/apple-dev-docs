# location

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The location that indicates the start of the text attachment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var location: any NSTextLocation { get }
```

```objc
@property (strong, readonly) id<NSTextLocation> location;
```

#### Discussion

Specify the value of this property at initialization time using the [`init(textAttachment:parentView:textLayoutManager:location:)`](./init%28textattachment,parentview,textlayoutmanager,location%29.md) initializer.

## See Also

### Defining the contents
- [var textAttachment: NSTextAttachment?](./textattachment.md)
  The text attachment for this view.
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
  The text layout manager for this view.
- [var tracksTextAttachmentViewBounds: Bool](./trackstextattachmentviewbounds.md)
  A Boolean value that determines the text attachment’s bounds policy.
- [var view: UIView?](./view.md)
  The text attachment’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/location)*