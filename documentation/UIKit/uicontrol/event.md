# UIControl.Event

**Framework**: UIKit  
**Kind**: struct

Constants describing the types of events possible for controls.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct Event
```

## Mentions

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)

#### Overview

You set up a control so that it sends an action message to a target object by associating both target and action with one or more control events. To do this, send [`addTarget(_:action:for:)`](uicontrol/addtarget(_:action:for:).md) to the control for each target-action pair you want to specify.

## Topics

### Constants
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
- [static var primaryActionTriggered: UIControl.Event](uicontrol/event/primaryactiontriggered.md)
  A semantic action triggered by buttons.
- [static var editingDidBegin: UIControl.Event](uicontrol/event/editingdidbegin.md)
  A touch initiating an editing session in a text field by entering its bounds.
- [static var editingChanged: UIControl.Event](uicontrol/event/editingchanged.md)
  A touch making an editing change in a text field.
- [static var editingDidEnd: UIControl.Event](uicontrol/event/editingdidend.md)
  A touch ending an editing session in a text field by leaving its bounds.
- [static var editingDidEndOnExit: UIControl.Event](uicontrol/event/editingdidendonexit.md)
  A touch ending an editing session in a text field.
- [static var allTouchEvents: UIControl.Event](uicontrol/event/alltouchevents.md)
  All touch events.
- [static var allEditingEvents: UIControl.Event](uicontrol/event/alleditingevents.md)
  All editing touches for text fields.
- [static var applicationReserved: UIControl.Event](uicontrol/event/applicationreserved.md)
  A range of control-event values available for app use.
- [static var systemReserved: UIControl.Event](uicontrol/event/systemreserved.md)
  A range of control-event values reserved for internal framework use.
- [static var allEvents: UIControl.Event](uicontrol/event/allevents.md)
  All events, including system events.
### Initializers
- [init(rawValue: UInt)](uicontrol/event/init(rawvalue:).md)
  Creates a control event with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/event)*