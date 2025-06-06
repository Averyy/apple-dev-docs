# isHighlighted

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the control draws a highlight.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isHighlighted: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the control draws a highlight; otherwise, the control doesn’t draw a highlight. Controls automatically set and clear this state in response to appropriate touch events. You can change the value of this property as needed to apply or remove a highlight programmatically

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false) for a newly created control. You can set a control’s initial selected state in your storyboard file.

## See Also

- [var state: UIControl.State](uicontrol/state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [UIControl.State](uicontrol/state-swift.struct.md)
  Constants describing the state of a control.
- [var isEnabled: Bool](uicontrol/isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isSelected: Bool](uicontrol/isselected.md)
  A Boolean value indicating whether the control is in the selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/ishighlighted)*