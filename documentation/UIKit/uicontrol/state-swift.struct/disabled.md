# disabled

**Framework**: UIKit  
**Kind**: property

The disabled state of a control.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var disabled: UIControl.State { get }
```

#### Discussion

User interactions with disabled control have no effect and the control draws itself with a dimmed appearance to reflect that it’s disabled. You can retrieve and set this value through the [`isEnabled`](uicontrol/isenabled.md) property.

## See Also

- [static var normal: UIControl.State](uicontrol/state-swift.struct/normal.md)
  The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [static var highlighted: UIControl.State](uicontrol/state-swift.struct/highlighted.md)
  The highlighted state of a control.
- [static var selected: UIControl.State](uicontrol/state-swift.struct/selected.md)
  The selected state of a control.
- [static var focused: UIControl.State](uicontrol/state-swift.struct/focused.md)
  The focused state of a control.
- [static var application: UIControl.State](uicontrol/state-swift.struct/application.md)
  Additional control-state flags available for app use.
- [static var reserved: UIControl.State](uicontrol/state-swift.struct/reserved.md)
  Control-state flags reserved for internal framework use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/disabled)*