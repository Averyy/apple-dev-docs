# state

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The state of the control, specified as a bit mask value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var state: UIControl.State { get }
```

```objc
@property (nonatomic, readonly) UIControlState state;
```

## Discussion

The value of this property is a bitmask of the constants in the [`UIControl.State`](./state-swift.struct.md) type. A control can be in more than one state at a time. For example, it can be focused and highlighted at the same time. You can also get the values for individual states using the properties of this class.

## See Also

### Managing state
- [UIControl.State](./state-swift.struct.md)
  Constants describing the state of a control.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isSelected: Bool](./isselected.md)
  A Boolean value indicating whether the control is in the selected state.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.property)*