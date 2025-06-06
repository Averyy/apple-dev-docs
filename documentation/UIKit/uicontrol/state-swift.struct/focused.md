# focused

**Framework**: UIKit  
**Kind**: property

The focused state of a control.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var focused: UIControl.State { get }
```

#### Discussion

In focus-based navigation systems, a control enters this state when it receives the focus. A focused control changes its appearance to indicate that it has focus, and this appearance differs from the appearance of the control when it’s highlighted or selected. Further interactions with the control can result in it also becoming highlighted or selected.

## See Also

- [static var normal: UIControl.State](uicontrol/state-swift.struct/normal.md)
  The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [static var highlighted: UIControl.State](uicontrol/state-swift.struct/highlighted.md)
  The highlighted state of a control.
- [static var disabled: UIControl.State](uicontrol/state-swift.struct/disabled.md)
  The disabled state of a control.
- [static var selected: UIControl.State](uicontrol/state-swift.struct/selected.md)
  The selected state of a control.
- [static var application: UIControl.State](uicontrol/state-swift.struct/application.md)
  Additional control-state flags available for app use.
- [static var reserved: UIControl.State](uicontrol/state-swift.struct/reserved.md)
  Control-state flags reserved for internal framework use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/focused)*