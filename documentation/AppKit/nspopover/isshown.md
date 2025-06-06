# isShown

**Framework**: AppKit  
**Kind**: property

The display state of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var isShown: Bool { get }
```

#### Discussion

The value is [`true`](https://developer.apple.com/documentation/swift/true) if the popover is being shown, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

The popover is considered to be shown from the point when [`show(relativeTo:of:preferredEdge:)`](nspopover/show(relativeto:of:preferrededge:).md) is invoked. A popover is considered closed in response to an invocation of either [`close()`](nspopover/close().md) or [`performClose(_:)`](nspopover/performclose(_:).md).

## See Also

- [var appearance: NSAppearance?](nspopover/appearance-swift.property.md)
  The appearance of the popover.
- [var effectiveAppearance: NSAppearance](nspopover/effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](nspopover/animates.md)
  Specifies if the popover is to be animated.
- [var contentSize: NSSize](nspopover/contentsize.md)
  The content size of the popover.
- [var isDetached: Bool](nspopover/isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/isshown)*