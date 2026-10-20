# selected

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The selected state of a control.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
static var selected: UIControl.State { get }
```

```c
UIControlStateSelected
```

#### Discussion

For many controls, this state has no effect on behavior or appearance. Some subclasses, like the [`UISegmentedControl`](../../uisegmentedcontrol.md) class, use this state to change their appearance. You can retrieve and set this value through the [`isSelected`](../isselected.md) property.

## See Also

### Constants
- [static var normal: UIControl.State](./normal.md)
  The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [static var highlighted: UIControl.State](./highlighted.md)
  The highlighted state of a control.
- [static var disabled: UIControl.State](./disabled.md)
  The disabled state of a control.
- [static var focused: UIControl.State](./focused.md)
  The focused state of a control.
- [static var application: UIControl.State](./application.md)
  Additional control-state flags available for app use.
- [static var reserved: UIControl.State](./reserved.md)
  Control-state flags reserved for internal framework use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/selected)*