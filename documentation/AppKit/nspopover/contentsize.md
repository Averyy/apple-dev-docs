# contentSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The content size of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var contentSize: NSSize { get set }
```

```objc
@property NSSize contentSize;
```

## Discussion

The popover’s content size is set to match the size of the content view when the content view controller is set.

Changes to the content size of the popover will cause the popover to animate while it is shown if the [`animates`](./animates.md) property is [`true`](../../Swift/true.md).

This property is exposed as a read-only binding.

## See Also

### Managing a Popover’s Appearance
- [var appearance: NSAppearance?](./appearance-swift.property.md)
  The appearance of the popover.
- [var effectiveAppearance: NSAppearance](./effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](./animates.md)
  Specifies if the popover is to be animated.
- [var isShown: Bool](./isshown.md)
  The display state of the popover.
- [var isDetached: Bool](./isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/contentsize)*