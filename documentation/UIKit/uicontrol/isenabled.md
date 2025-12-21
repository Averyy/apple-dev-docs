# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the control is in the enabled state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

Set the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true) to enable the control or [`false`](https://developer.apple.com/documentation/Swift/false) to disable it. An enabled control is capable of responding to user interactions, whereas a disabled control ignores touch events and may draw itself differently. Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) adds the [`disabled`](uicontrol/state-swift.struct/disabled.md) flag to the control’s [`state`](uicontrol/state-swift.property.md) bitmask; enabling the control again removes that flag.

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) for a newly created control. You can set a control’s initial enabled state in your storyboard file.

## See Also

- [var state: UIControl.State](uicontrol/state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [UIControl.State](uicontrol/state-swift.struct.md)
  Constants describing the state of a control.
- [var isSelected: Bool](uicontrol/isselected.md)
  A Boolean value indicating whether the control is in the selected state.
- [var isHighlighted: Bool](uicontrol/ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/isenabled)*