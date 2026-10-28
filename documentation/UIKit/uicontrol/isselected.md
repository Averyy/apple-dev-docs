# isSelected

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the control is in the selected state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isSelected: Bool { get set }
```

```objc
@property (nonatomic, getter=isSelected) BOOL selected;
```

## Discussion

Set the value of this property to [`true`](../../Swift/true.md) to select it or [`false`](../../Swift/false.md) to deselect it. Most controls don’t modify their appearance or behavior when selected, but some do. For example, the [`UISegmentedControl`](../uisegmentedcontrol.md) class tracks whether a segment is selected and draws it differently when it is.

The default value of this property is [`false`](../../Swift/false.md) for a newly created control. You can set a control’s initial selected state in your storyboard file.

## See Also

### Managing state
- [var state: UIControl.State](./state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [UIControl.State](./state-swift.struct.md)
  Constants describing the state of a control.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/isselected)*