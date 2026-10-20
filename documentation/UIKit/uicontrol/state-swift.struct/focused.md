# focused

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```c
UIControlStateFocused
```

#### Discussion

In focus-based navigation systems, a control enters this state when it receives the focus. A focused control changes its appearance to indicate that it has focus, and this appearance differs from the appearance of the control when it’s highlighted or selected. Further interactions with the control can result in it also becoming highlighted or selected.

## See Also

### Constants
- [static var normal: UIControl.State](./normal.md)
  The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [static var highlighted: UIControl.State](./highlighted.md)
  The highlighted state of a control.
- [static var disabled: UIControl.State](./disabled.md)
  The disabled state of a control.
- [static var selected: UIControl.State](./selected.md)
  The selected state of a control.
- [static var application: UIControl.State](./application.md)
  Additional control-state flags available for app use.
- [static var reserved: UIControl.State](./reserved.md)
  Control-state flags reserved for internal framework use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/focused)*