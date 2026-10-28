# isDetached

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isDetached: Bool { get }
```

```objc
@property (readonly, getter=isDetached) BOOL detached;
```

## Discussion

When [`isDetached`](./isdetached.md) is [`true`](../../Swift/true.md), the detached window is automatically created. This property does not apply when detaching a popover results in a window returned by [`detachableWindow(for:)`](../nspopoverdelegate/detachablewindow%28for%29.md).

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
- [var isShown: Bool](./isshown.md)
  The display state of the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/isdetached)*