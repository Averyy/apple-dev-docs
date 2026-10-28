# collapsedRepresentation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view displayed when this item is displayed in its parent bar.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var collapsedRepresentation: NSView { get set }
```

```objc
@property (strong) NSView * collapsedRepresentation;
```

## Discussion

By default, this is an [`NSButton`](../nsbutton.md) whose target is this popover item, whose action is [`showPopover(_:)`](./showpopover%28_%29.md), and whose image and title are bound to this item’s [`collapsedRepresentationImage`](./collapsedrepresentationimage.md) and [`collapsedRepresentationImage`](./collapsedrepresentationimage.md) respectively.

## See Also

### Configuring the collapsed popover
- [var collapsedRepresentationImage: UIImage?](./collapsedrepresentationimage.md)
  The image displayed by the button for the default collapsed representation.
- [var collapsedRepresentationLabel: String](./collapsedrepresentationlabel.md)
  The localized string displayed by the button for the default collapsed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/collapsedrepresentation)*