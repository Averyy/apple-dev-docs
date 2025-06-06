# highlighted

**Framework**: UIKit  
**Kind**: property

The highlighted state of a control.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var highlighted: UIControl.State { get }
```

#### Discussion

A control becomes highlighted when a touch event enters the control’s bounds, and it loses that highlight when there’s a touch-up event or when the touch event exits the control’s bounds. You can retrieve and set this value through the [`isHighlighted`](uicontrol/ishighlighted.md) property.

## See Also

- [static var normal: UIControl.State](uicontrol/state-swift.struct/normal.md)
  The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [static var disabled: UIControl.State](uicontrol/state-swift.struct/disabled.md)
  The disabled state of a control.
- [static var selected: UIControl.State](uicontrol/state-swift.struct/selected.md)
  The selected state of a control.
- [static var focused: UIControl.State](uicontrol/state-swift.struct/focused.md)
  The focused state of a control.
- [static var application: UIControl.State](uicontrol/state-swift.struct/application.md)
  Additional control-state flags available for app use.
- [static var reserved: UIControl.State](uicontrol/state-swift.struct/reserved.md)
  Control-state flags reserved for internal framework use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/highlighted)*