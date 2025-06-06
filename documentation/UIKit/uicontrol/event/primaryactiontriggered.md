# primaryActionTriggered

**Framework**: UIKit  
**Kind**: property

A semantic action triggered by buttons.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var primaryActionTriggered: UIControl.Event { get }
```

## See Also

- [static var touchDown: UIControl.Event](uicontrol/event/touchdown.md)
  A touch-down event in the control.
- [static var touchDownRepeat: UIControl.Event](uicontrol/event/touchdownrepeat.md)
  A repeated touch-down event in the control; for this event the value of the UITouch `tapCount` method is greater than one.
- [static var touchDragInside: UIControl.Event](uicontrol/event/touchdraginside.md)
  An event where a finger is dragged inside the bounds of the control.
- [static var touchDragOutside: UIControl.Event](uicontrol/event/touchdragoutside.md)
  An event where a finger is dragged just outside the bounds of the control.
- [static var touchDragEnter: UIControl.Event](uicontrol/event/touchdragenter.md)
  An event where a finger is dragged into the bounds of the control.
- [static var touchDragExit: UIControl.Event](uicontrol/event/touchdragexit.md)
  An event where a finger is dragged from within a control to outside its bounds.
- [static var touchUpInside: UIControl.Event](uicontrol/event/touchupinside.md)
  A touch-up event in the control where the finger is inside the bounds of the control.
- [static var touchUpOutside: UIControl.Event](uicontrol/event/touchupoutside.md)
  A touch-up event in the control where the finger is outside the bounds of the control.
- [static var touchCancel: UIControl.Event](uicontrol/event/touchcancel.md)
  A system event canceling the current touches for the control.
- [static var valueChanged: UIControl.Event](uicontrol/event/valuechanged.md)
  A touch dragging or otherwise manipulating a control, causing it to emit a series of different values.
- [static var menuActionTriggered: UIControl.Event](uicontrol/event/menuactiontriggered.md)
  A menu action has triggered prior to the menu being presented.
- [static var editingDidBegin: UIControl.Event](uicontrol/event/editingdidbegin.md)
  A touch initiating an editing session in a text field by entering its bounds.
- [static var editingChanged: UIControl.Event](uicontrol/event/editingchanged.md)
  A touch making an editing change in a text field.
- [static var editingDidEnd: UIControl.Event](uicontrol/event/editingdidend.md)
  A touch ending an editing session in a text field by leaving its bounds.
- [static var editingDidEndOnExit: UIControl.Event](uicontrol/event/editingdidendonexit.md)
  A touch ending an editing session in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/event/primaryactiontriggered)*