# touchDragOutside

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An event where a finger is dragged just outside the bounds of the control.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
static var touchDragOutside: UIControl.Event { get }
```

```c
UIControlEventTouchDragOutside
```

## See Also

### Constants
- [static var touchDown: UIControl.Event](./touchdown.md)
  A touch-down event in the control.
- [static var touchDownRepeat: UIControl.Event](./touchdownrepeat.md)
  A repeated touch-down event in the control; for this event the value of the UITouch `tapCount` method is greater than one.
- [static var touchDragInside: UIControl.Event](./touchdraginside.md)
  An event where a finger is dragged inside the bounds of the control.
- [static var touchDragEnter: UIControl.Event](./touchdragenter.md)
  An event where a finger is dragged into the bounds of the control.
- [static var touchDragExit: UIControl.Event](./touchdragexit.md)
  An event where a finger is dragged from within a control to outside its bounds.
- [static var touchUpInside: UIControl.Event](./touchupinside.md)
  A touch-up event in the control where the finger is inside the bounds of the control.
- [static var touchUpOutside: UIControl.Event](./touchupoutside.md)
  A touch-up event in the control where the finger is outside the bounds of the control.
- [static var touchCancel: UIControl.Event](./touchcancel.md)
  A system event canceling the current touches for the control.
- [static var valueChanged: UIControl.Event](./valuechanged.md)
  A touch dragging or otherwise manipulating a control, causing it to emit a series of different values.
- [static var menuActionTriggered: UIControl.Event](./menuactiontriggered.md)
  A menu action has triggered prior to the menu being presented.
- [static var primaryActionTriggered: UIControl.Event](./primaryactiontriggered.md)
  A semantic action triggered by buttons.
- [static var editingDidBegin: UIControl.Event](./editingdidbegin.md)
  A touch initiating an editing session in a text field by entering its bounds.
- [static var editingChanged: UIControl.Event](./editingchanged.md)
  A touch making an editing change in a text field.
- [static var editingDidEnd: UIControl.Event](./editingdidend.md)
  A touch ending an editing session in a text field by leaving its bounds.
- [static var editingDidEndOnExit: UIControl.Event](./editingdidendonexit.md)
  A touch ending an editing session in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/event/touchdragoutside)*