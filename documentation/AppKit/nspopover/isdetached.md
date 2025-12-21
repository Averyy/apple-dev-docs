# isDetached

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var isDetached: Bool { get }
```

#### Discussion

When [`isDetached`](nspopover/isdetached.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the detached window is automatically created. This property does not apply when detaching a popover results in a window returned by [`detachableWindow(for:)`](nspopoverdelegate/detachablewindow(for:).md).

## See Also

- [var appearance: NSAppearance?](nspopover/appearance-swift.property.md)
  The appearance of the popover.
- [var effectiveAppearance: NSAppearance](nspopover/effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](nspopover/animates.md)
  Specifies if the popover is to be animated.
- [var contentSize: NSSize](nspopover/contentsize.md)
  The content size of the popover.
- [var isShown: Bool](nspopover/isshown.md)
  The display state of the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/isdetached)*