# becomesKeyOnlyIfNeeded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver becomes the key window only when needed.

**Availability**:
- macOS

## Declaration

```swift
var becomesKeyOnlyIfNeeded: Bool { get set }
```

```objc
@property BOOL becomesKeyOnlyIfNeeded;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the panel becomes the key window only when keyboard input is required; the value is [`false`](../../Swift/false.md) when the panel becomes key when it’s clicked. The default value is [`false`](../../Swift/false.md).

This behavior is not set by default. You should consider setting it only if most user interface elements in the panel aren’t text fields, and if the choices that can be made by entering text can also be made in another way (such as by clicking an item in a list).

If the panel is a non-activating panel, then it becomes key only if the hit view returns [`true`](../../Swift/true.md) from [`needsPanelToBecomeKey`](../nsview/needspaneltobecomekey.md). This way, a non-activating panel can control whether it takes keyboard focus.

## See Also

### Related Documentation
- [var needsPanelToBecomeKey: Bool](../nsview/needspaneltobecomekey.md)
  A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.
### Configuring Panels
- [var isFloatingPanel: Bool](./isfloatingpanel.md)
  A Boolean value that indicates whether the receiver is a floating panel.
- [var worksWhenModal: Bool](./workswhenmodal.md)
  A Boolean value that indicates whether the panel receives keyboard and mouse events even when some other window is being run modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspanel/becomeskeyonlyifneeded)*