# appearance

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The appearance of the popover.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var appearance: NSAppearance? { get set }
```

*Mac Catalyst*

```objc
@property NSPopoverAppearance appearance;
```

*macOS*

```objc
@property (strong, nullable) NSAppearance * appearance;
```

#### Discussion

If no appearance is specified, the popover’s effective appearance defaults to [`vibrantLight`](../nsappearance/name-swift.struct/vibrantlight.md).

In apps that run in macOS 10.10 and later, the previous property type of [`NSPopover.Appearance`](./appearance-swift.enum.md) is deprecated. In apps that run in OS X v10.9 and earlier, the [`aqua`](../nsappearance/name-swift.struct/aqua.md) appearance is automatically set on popover content.

## See Also

### Managing a Popover’s Appearance
- [var effectiveAppearance: NSAppearance](./effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](./animates.md)
  Specifies if the popover is to be animated.
- [var contentSize: NSSize](./contentsize.md)
  The content size of the popover.
- [var isShown: Bool](./isshown.md)
  The display state of the popover.
- [var isDetached: Bool](./isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/appearance-swift.property)*