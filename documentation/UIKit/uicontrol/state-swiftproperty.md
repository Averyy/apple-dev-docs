# state

**Framework**: UIKit  
**Kind**: property

The state of the control, specified as a bit mask value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var state: UIControl.State { get }
```

#### Discussion

The value of this property is a bitmask of the constants in the [`UIControl.State`](uicontrol/state-swift.struct.md) type. A control can be in more than one state at a time. For example, it can be focused and highlighted at the same time. You can also get the values for individual states using the properties of this class.

## See Also

- [UIControl.State](uicontrol/state-swift.struct.md)
  Constants describing the state of a control.
- [var isEnabled: Bool](uicontrol/isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isSelected: Bool](uicontrol/isselected.md)
  A Boolean value indicating whether the control is in the selected state.
- [var isHighlighted: Bool](uicontrol/ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.property)*