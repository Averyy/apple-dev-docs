# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the control is in the enabled state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Discussion

Set the value of this property to [`true`](../../Swift/true.md) to enable the control or [`false`](../../Swift/false.md) to disable it. An enabled control is capable of responding to user interactions, whereas a disabled control ignores touch events and may draw itself differently. Setting this property to [`false`](../../Swift/false.md) adds the [`disabled`](./state-swift.struct/disabled.md) flag to the control’s [`state`](./state-swift.property.md) bitmask; enabling the control again removes that flag.

The default value of this property is [`true`](../../Swift/true.md) for a newly created control. You can set a control’s initial enabled state in your storyboard file.

## See Also

### Managing state
- [var state: UIControl.State](./state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [UIControl.State](./state-swift.struct.md)
  Constants describing the state of a control.
- [var isSelected: Bool](./isselected.md)
  A Boolean value indicating whether the control is in the selected state.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/isenabled)*