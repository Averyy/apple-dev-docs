# UIControl.State

**Framework**: UIKit  
**Kind**: struct

Constants describing the state of a control.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct State
```

#### Overview

A control can have more than one state at a time. Controls can have different configurations according to their state. For example, a [`UIButton`](uibutton.md) object can display one image when it’s in its normal state and a different image when it’s highlighted.

## Topics

### Constants
- [static var normal: UIControl.State](uicontrol/state-swift.struct/normal.md)
  The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [static var highlighted: UIControl.State](uicontrol/state-swift.struct/highlighted.md)
  The highlighted state of a control.
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
### Initializers
- [init(rawValue: UInt)](uicontrol/state-swift.struct/init(rawvalue:).md)
  Creates a control state with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var state: UIControl.State](uicontrol/state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [var isEnabled: Bool](uicontrol/isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isSelected: Bool](uicontrol/isselected.md)
  A Boolean value indicating whether the control is in the selected state.
- [var isHighlighted: Bool](uicontrol/ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct)*