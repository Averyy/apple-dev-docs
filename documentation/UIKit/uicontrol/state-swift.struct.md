# UIControl.State

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants describing the state of a control.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct State
```

```c
enum UIControlState : NSUInteger;
```

#### Overview

A control can have more than one state at a time. Controls can have different configurations according to their state. For example, a [`UIButton`](../uibutton.md) object can display one image when it’s in its normal state and a different image when it’s highlighted.

## Topics

### Constants
- [static var normal: UIControl.State](./state-swift.struct/normal.md)
  The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [static var highlighted: UIControl.State](./state-swift.struct/highlighted.md)
  The highlighted state of a control.
- [static var disabled: UIControl.State](./state-swift.struct/disabled.md)
  The disabled state of a control.
- [static var selected: UIControl.State](./state-swift.struct/selected.md)
  The selected state of a control.
- [static var focused: UIControl.State](./state-swift.struct/focused.md)
  The focused state of a control.
- [static var application: UIControl.State](./state-swift.struct/application.md)
  Additional control-state flags available for app use.
- [static var reserved: UIControl.State](./state-swift.struct/reserved.md)
  Control-state flags reserved for internal framework use.
### Initializers
- [init(rawValue: UInt)](./state-swift.struct/init%28rawvalue%29.md)
  Creates a control state with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing state
- [var state: UIControl.State](./state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isSelected: Bool](./isselected.md)
  A Boolean value indicating whether the control is in the selected state.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct)*