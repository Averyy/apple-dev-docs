# collapsedRepresentation

**Framework**: AppKit  
**Kind**: property

The view displayed when this item is displayed in its parent bar.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var collapsedRepresentation: NSView { get set }
```

#### Discussion

By default, this is an [`NSButton`](nsbutton.md) whose target is this popover item, whose action is [`showPopover(_:)`](nspopovertouchbaritem/showpopover(_:).md), and whose image and title are bound to this item’s [`collapsedRepresentationImage`](nspopovertouchbaritem/collapsedrepresentationimage.md) and [`collapsedRepresentationImage`](nspopovertouchbaritem/collapsedrepresentationimage.md) respectively.

## See Also

- [var collapsedRepresentationImage: UIImage?](nspopovertouchbaritem/collapsedrepresentationimage.md)
  The image displayed by the button for the default collapsed representation.
- [var collapsedRepresentationLabel: String](nspopovertouchbaritem/collapsedrepresentationlabel.md)
  The localized string displayed by the button for the default collapsed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/collapsedrepresentation)*