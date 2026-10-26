# UIControl.Event

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants describing the types of events possible for controls.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct Event
```

```c
enum UIControlEvents : NSUInteger;
```

## Mentions

- [Responding to control-based events using target-action](../responding-to-control-based-events-using-target-action.md)

#### Overview

You set up a control so that it sends an action message to a target object by associating both target and action with one or more control events. To do this, send [`addTarget(_:action:for:)`](./addtarget%28_,action,for%29.md) to the control for each target-action pair you want to specify.

## Topics

### Constants
- [static var touchDown: UIControl.Event](./event/touchdown.md)
  A touch-down event in the control.
- [static var touchDownRepeat: UIControl.Event](./event/touchdownrepeat.md)
  A repeated touch-down event in the control; for this event the value of the UITouch `tapCount` method is greater than one.
- [static var touchDragInside: UIControl.Event](./event/touchdraginside.md)
  An event where a finger is dragged inside the bounds of the control.
- [static var touchDragOutside: UIControl.Event](./event/touchdragoutside.md)
  An event where a finger is dragged just outside the bounds of the control.
- [static var touchDragEnter: UIControl.Event](./event/touchdragenter.md)
  An event where a finger is dragged into the bounds of the control.
- [static var touchDragExit: UIControl.Event](./event/touchdragexit.md)
  An event where a finger is dragged from within a control to outside its bounds.
- [static var touchUpInside: UIControl.Event](./event/touchupinside.md)
  A touch-up event in the control where the finger is inside the bounds of the control.
- [static var touchUpOutside: UIControl.Event](./event/touchupoutside.md)
  A touch-up event in the control where the finger is outside the bounds of the control.
- [static var touchCancel: UIControl.Event](./event/touchcancel.md)
  A system event canceling the current touches for the control.
- [static var valueChanged: UIControl.Event](./event/valuechanged.md)
  A touch dragging or otherwise manipulating a control, causing it to emit a series of different values.
- [static var menuActionTriggered: UIControl.Event](./event/menuactiontriggered.md)
  A menu action has triggered prior to the menu being presented.
- [static var primaryActionTriggered: UIControl.Event](./event/primaryactiontriggered.md)
  A semantic action triggered by buttons.
- [static var editingDidBegin: UIControl.Event](./event/editingdidbegin.md)
  A touch initiating an editing session in a text field by entering its bounds.
- [static var editingChanged: UIControl.Event](./event/editingchanged.md)
  A touch making an editing change in a text field.
- [static var editingDidEnd: UIControl.Event](./event/editingdidend.md)
  A touch ending an editing session in a text field by leaving its bounds.
- [static var editingDidEndOnExit: UIControl.Event](./event/editingdidendonexit.md)
  A touch ending an editing session in a text field.
- [static var allTouchEvents: UIControl.Event](./event/alltouchevents.md)
  All touch events.
- [static var allEditingEvents: UIControl.Event](./event/alleditingevents.md)
  All editing touches for text fields.
- [static var applicationReserved: UIControl.Event](./event/applicationreserved.md)
  A range of control-event values available for app use.
- [static var systemReserved: UIControl.Event](./event/systemreserved.md)
  A range of control-event values reserved for internal framework use.
- [static var allEvents: UIControl.Event](./event/allevents.md)
  All events, including system events.
### Initializers
- [init(rawValue: UInt)](./event/init%28rawvalue%29.md)
  Creates a control event with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing the control’s targets and actions
- [func addTarget(Any?, action: Selector, for: UIControl.Event)](./addtarget%28_,action,for%29.md)
  Associates a target object and action method with the control.
- [func removeTarget(Any?, action: Selector?, for: UIControl.Event)](./removetarget%28_,action,for%29.md)
  Stops the delivery of events to the specified target object.
- [var allTargets: Set<AnyHashable>](./alltargets.md)
  Returns all target objects associated with the control.
- [func addAction(UIAction, for: UIControl.Event)](./addaction%28_,for%29.md)
  Adds the UIAction to a given event. UIActions are uniqued based on their identifier, and subsequent actions with the same identifier replace previously added actions. You may add multiple UIActions for corresponding controlEvents, and you may add the same action to multiple controlEvents.
- [func removeAction(UIAction, for: UIControl.Event)](./removeaction%28_,for%29.md)
  Removes the action from the set of passed control events.
- [func removeAction(identifiedBy: UIAction.Identifier, for: UIControl.Event)](./removeaction%28identifiedby,for%29.md)
  Removes the action with the provided identifier from the set of passed control events.
- [func actions(forTarget: Any?, forControlEvent: UIControl.Event) -> [String]?](./actions%28fortarget,forcontrolevent%29.md)
  Returns the actions performed on a target object when the specified event occurs.
- [var allControlEvents: UIControl.Event](./allcontrolevents.md)
  Returns the events for which the control has associated actions.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](./enumerateeventhandlers%28_%29.md)
- [- enumerateEventHandlers:](./enumerateeventhandlers_.md)
  Iterate over the event handlers installed on this control at the time this method is called. For each call, either actionHandler or action will be non-nil. controlEvents is always non-zero. Setting *stop to YES will terminate the enumeration early. It is legal to manipulate the control’s event handlers within the block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/event)*