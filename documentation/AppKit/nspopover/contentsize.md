# contentSize

**Framework**: AppKit  
**Kind**: property

The content size of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var contentSize: NSSize { get set }
```

#### Discussion

The popover’s content size is set to match the size of the content view when the content view controller is set.

Changes to the content size of the popover will cause the popover to animate while it is shown if the [`animates`](nspopover/animates.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

This property is exposed as a read-only binding.

## See Also

- [var appearance: NSAppearance?](nspopover/appearance-swift.property.md)
  The appearance of the popover.
- [var effectiveAppearance: NSAppearance](nspopover/effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](nspopover/animates.md)
  Specifies if the popover is to be animated.
- [var isShown: Bool](nspopover/isshown.md)
  The display state of the popover.
- [var isDetached: Bool](nspopover/isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/contentsize)*