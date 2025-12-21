# showsCloseButton

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether a close button should be shown on the popover bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var showsCloseButton: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/Swift/true), a close button is automatically displayed when the popover bar is displayed. When [`false`](https://developer.apple.com/documentation/Swift/false), it is your responsibility to dismiss the popover bar.

## See Also

- [var popoverTouchBar: NSTouchBar](nspopovertouchbaritem/popovertouchbar.md)
  The bar displayed when this item is “popped.”
- [var pressAndHoldTouchBar: NSTouchBar?](nspopovertouchbaritem/pressandholdtouchbar.md)
  The bar that is displayed when a user press-and-holds on the popover item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/showsclosebutton)*