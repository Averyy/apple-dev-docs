# becomesKeyOnlyIfNeeded

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver becomes the key window only when needed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var becomesKeyOnlyIfNeeded: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the panel becomes the key window only when keyboard input is required; the value is [`false`](https://developer.apple.com/documentation/Swift/false) when the panel becomes key when it’s clicked. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

This behavior is not set by default. You should consider setting it only if most user interface elements in the panel aren’t text fields, and if the choices that can be made by entering text can also be made in another way (such as by clicking an item in a list).

If the panel is a non-activating panel, then it becomes key only if the hit view returns [`true`](https://developer.apple.com/documentation/Swift/true) from [`needsPanelToBecomeKey`](nsview/needspaneltobecomekey.md). This way, a non-activating panel can control whether it takes keyboard focus.

## See Also

- [var needsPanelToBecomeKey: Bool](nsview/needspaneltobecomekey.md)
  A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.
- [var isFloatingPanel: Bool](nspanel/isfloatingpanel.md)
  A Boolean value that indicates whether the receiver is a floating panel.
- [var worksWhenModal: Bool](nspanel/workswhenmodal.md)
  A Boolean value that indicates whether the panel receives keyboard and mouse events even when some other window is being run modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspanel/becomeskeyonlyifneeded)*