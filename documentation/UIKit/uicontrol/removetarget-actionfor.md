# removeTarget(_:action:for:)

**Framework**: UIKit  
**Kind**: method

Stops the delivery of events to the specified target object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeTarget(_ target: Any?, action: Selector?, for controlEvents: UIControl.Event)
```

#### Discussion

Use this method to prevent the delivery of control events to target objects associated with control. If you specify a valid object in the `target` parameter, this method stops the delivery of the specified events to all action methods associated with that object. If you specify `nil` for the `target` parameter, this method prevents the delivery of those events to all action methods of all target objects.

Although the `action` parameter is not considered when stopping the delivery of events, you should specify an appropriate value anyway. If the specified target/action combination no longer has any valid control events associated with it, the control cleans up its corresponding internal data structures. Doing so can affect the set of objects returned by the [`allTargets`](uicontrol/alltargets.md) method.

## Parameters

- `target`: A target object registered with the control. Specify   to remove the specified control events for all target objects.
- `action`: A selector identifying a registered action method. You may specify   for this parameter.
- `controlEvents`: A bitmask specifying the control events that you want to remove for the specified   object. For a list of possible constants, see  .

## See Also

- [func addTarget(Any?, action: Selector, for: UIControl.Event)](uicontrol/addtarget(_:action:for:).md)
  Associates a target object and action method with the control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/removetarget(_:action:for:))*