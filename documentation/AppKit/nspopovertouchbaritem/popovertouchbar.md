# popoverTouchBar

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The bar displayed when this item is “popped.”

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var popoverTouchBar: NSTouchBar { get set }
```

```objc
@property (strong) NSTouchBar * popoverTouchBar;
```

#### Discussion

Set this property to a fully configured instance of [`NSTouchBar`](../nstouchbar.md) that is displayed when the user taps on the popover item. By default this is an empty bar.

## See Also

### Configuring the expanded popover
- [var showsCloseButton: Bool](./showsclosebutton.md)
  A Boolean value that determines whether a close button should be shown on the popover bar.
- [var pressAndHoldTouchBar: NSTouchBar?](./pressandholdtouchbar.md)
  The bar that is displayed when a user press-and-holds on the popover item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem/popovertouchbar)*