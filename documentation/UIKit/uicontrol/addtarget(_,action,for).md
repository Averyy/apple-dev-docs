# addTarget(_:action:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Associates a target object and action method with the control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func addTarget(_ target: Any?, action: Selector, for controlEvents: UIControl.Event)
```

```objc
- (void) addTarget:(id) target action:(SEL) action forControlEvents:(UIControlEvents) controlEvents;
```

## Mentions

- [Responding to control-based events using target-action](../responding-to-control-based-events-using-target-action.md)

## Discussion

You may call this method multiple times to configure multiple targets and actions for the control. It is also safe to call this method multiple times with the same values for the `target` and `action` parameters. The control maintains a list of its attached targets and actions along with the events each supports.

The control does not retain the object in the `target` parameter. It is your responsibility to maintain a strong reference to the target object while it is attached to a control.

Specifying a value of `0` for the `controlEvents` parameter does not prevent events from being sent to a previously registered `target` and `action` method. To stop the delivery of events, always call the [`removeTarget(_:action:for:)`](./removetarget%28_,action,for%29.md) method.

## Parameters

- `target`: The target object—that is, the object whose `action` method is called. If you specify `nil`, UIKit searches the responder chain for an object that responds to the specified action message and delivers the message to that object.
- `action`: A selector identifying the action method to be called. You may specify a selector whose signature matches any of the signatures in the code example in [`UIControl`](../uicontrol.md). This parameter must not be `nil`.
- `controlEvents`: A bitmask specifying the control-specific events for which the action method is called. Always specify at least one constant. For a list of possible constants, see [`UIControl.Event`](./event.md).

## See Also

### Managing the control’s targets and actions
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
- [UIControl.Event](./event.md)
  Constants describing the types of events possible for controls.
- [- enumerateEventHandlers:](./enumerateeventhandlers_.md)
  Iterate over the event handlers installed on this control at the time this method is called. For each call, either actionHandler or action will be non-nil. controlEvents is always non-zero. Setting *stop to YES will terminate the enumeration early. It is legal to manipulate the control’s event handlers within the block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/addtarget(_:action:for:))*