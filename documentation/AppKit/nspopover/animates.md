# animates

**Framework**: AppKit  
**Kind**: property

Specifies if the popover is to be animated.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var animates: Bool { get set }
```

#### Discussion

A popover may be animated when it shows, closes, moves, or appears to transition to a detachable window. This property also controls whether the popover animates when the content view or content size changes.

The system does not guarantee which behaviors will be animated or that this property will be respected; it is regarded as a hint.

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var appearance: NSAppearance?](nspopover/appearance-swift.property.md)
  The appearance of the popover.
- [var effectiveAppearance: NSAppearance](nspopover/effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var contentSize: NSSize](nspopover/contentsize.md)
  The content size of the popover.
- [var isShown: Bool](nspopover/isshown.md)
  The display state of the popover.
- [var isDetached: Bool](nspopover/isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/animates)*