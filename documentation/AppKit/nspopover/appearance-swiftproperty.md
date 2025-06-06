# appearance

**Framework**: AppKit  
**Kind**: property

The appearance of the popover.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var appearance: NSAppearance? { get set }
```

#### Discussion

If no appearance is specified, the popover’s effective appearance defaults to [`vibrantLight`](nsappearance/name-swift.struct/vibrantlight.md).

In apps that run in macOS 10.10 and later, the previous property type of [`NSPopover.Appearance`](nspopover/appearance-swift.enum.md) is deprecated. In apps that run in OS X v10.9 and earlier, the [`aqua`](nsappearance/name-swift.struct/aqua.md) appearance is automatically set on popover content.

## See Also

- [var effectiveAppearance: NSAppearance](nspopover/effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](nspopover/animates.md)
  Specifies if the popover is to be animated.
- [var contentSize: NSSize](nspopover/contentsize.md)
  The content size of the popover.
- [var isShown: Bool](nspopover/isshown.md)
  The display state of the popover.
- [var isDetached: Bool](nspopover/isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/appearance-swift.property)*