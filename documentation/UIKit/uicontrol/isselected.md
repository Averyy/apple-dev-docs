# isSelected

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the control is in the selected state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isSelected: Bool { get set }
```

#### Discussion

Set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) to select it or [`false`](https://developer.apple.com/documentation/swift/false) to deselect it. Most controls don’t modify their appearance or behavior when selected, but some do. For example, the [`UISegmentedControl`](uisegmentedcontrol.md) class tracks whether a segment is selected and draws it differently when it is.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false) for a newly created control. You can set a control’s initial selected state in your storyboard file.

## See Also

- [var state: UIControl.State](uicontrol/state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [UIControl.State](uicontrol/state-swift.struct.md)
  Constants describing the state of a control.
- [var isEnabled: Bool](uicontrol/isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isHighlighted: Bool](uicontrol/ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/isselected)*