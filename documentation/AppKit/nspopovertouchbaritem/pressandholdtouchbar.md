# pressAndHoldTouchBar

**Framework**: AppKit  
**Kind**: property

The bar that is displayed when a user press-and-holds on the popover item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var pressAndHoldTouchBar: NSTouchBar? { get set }
```

#### Discussion

This [`NSTouchBar`](nstouchbar.md) can be the same as the one used for the [`popoverTouchBar`](nspopovertouchbaritem/popovertouchbar.md) property, but does not have to be.

When non-`nil` this touch bar is displayed while the user holds their finger down on the collapsed representation of the popover item. When the user raises their finger, this bar disappears.

## See Also

- [var popoverTouchBar: NSTouchBar](nspopovertouchbaritem/popovertouchbar.md)
  The bar displayed when this item is “popped.”
- [var showsCloseButton: Bool](nspopovertouchbaritem/showsclosebutton.md)
  A Boolean value that determines whether a close button should be shown on the popover bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/pressandholdtouchbar)*