# isShown

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The display state of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isShown: Bool { get }
```

```objc
@property (readonly, getter=isShown) BOOL shown;
```

## Discussion

The value is [`true`](../../Swift/true.md) if the popover is being shown, [`false`](../../Swift/false.md) otherwise.

The popover is considered to be shown from the point when [`show(relativeTo:of:preferredEdge:)`](./show%28relativeto,of,preferrededge%29.md) is invoked. A popover is considered closed in response to an invocation of either [`close()`](./close%28%29.md) or [`performClose(_:)`](./performclose%28_%29.md).

## See Also

### Managing a Popover’s Appearance
- [var appearance: NSAppearance?](./appearance-swift.property.md)
  The appearance of the popover.
- [var effectiveAppearance: NSAppearance](./effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](./animates.md)
  Specifies if the popover is to be animated.
- [var contentSize: NSSize](./contentsize.md)
  The content size of the popover.
- [var isDetached: Bool](./isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/isshown)*