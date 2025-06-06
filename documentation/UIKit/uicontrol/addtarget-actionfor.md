# addTarget(_:action:for:)

**Framework**: UIKit  
**Kind**: method

Associates a target object and action method with the control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addTarget(_ target: Any?, action: Selector, for controlEvents: UIControl.Event)
```

## Mentions

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)

#### Discussion

You may call this method multiple times to configure multiple targets and actions for the control. It is also safe to call this method multiple times with the same values for the `target` and `action` parameters. The control maintains a list of its attached targets and actions along with the events each supports.

The control does not retain the object in the `target` parameter. It is your responsibility to maintain a strong reference to the target object while it is attached to a control.

Specifying a value of `0` for the `controlEvents` parameter does not prevent events from being sent to a previously registered `target` and `action` method. To stop the delivery of events, always call the [`removeTarget(_:action:for:)`](uicontrol/removetarget(_:action:for:).md) method.

## Parameters

- `target`: The target object—that is, the object whose   method is called. If you specify  , UIKit searches the responder chain for an object that responds to the specified action message and delivers the message to that object.
- `action`: A selector identifying the action method to be called. You may specify a selector whose signature matches any of the signatures in the code example in  . This parameter must not be  .
- `controlEvents`: A bitmask specifying the control-specific events for which the action method is called. Always specify at least one constant. For a list of possible constants, see  .

## See Also

- [func removeTarget(Any?, action: Selector?, for: UIControl.Event)](uicontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.
- [var allTargets: Set<AnyHashable>](uicontrol/alltargets.md)
  Returns all target objects associated with the control.
- [func addAction(UIAction, for: UIControl.Event)](uicontrol/addaction(_:for:).md)
- [func removeAction(UIAction, for: UIControl.Event)](uicontrol/removeaction(_:for:).md)
- [func removeAction(identifiedBy: UIAction.Identifier, for: UIControl.Event)](uicontrol/removeaction(identifiedby:for:).md)
- [func actions(forTarget: Any?, forControlEvent: UIControl.Event) -> [String]?](uicontrol/actions(fortarget:forcontrolevent:).md)
  Returns the actions performed on a target object when the specified event occurs.
- [var allControlEvents: UIControl.Event](uicontrol/allcontrolevents.md)
  Returns the events for which the control has associated actions.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](uicontrol/enumerateeventhandlers(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/addtarget(_:action:for:))*