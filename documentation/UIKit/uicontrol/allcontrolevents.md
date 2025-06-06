# allControlEvents

**Framework**: UIKit  
**Kind**: property

Returns the events for which the control has associated actions.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allControlEvents: UIControl.Event { get }
```

#### Return Value

A bitmask of constants indicating the events for which this control has associated actions. For a list of possible constants, see the [`UIControl.Event`](uicontrol/event.md) type.

#### Discussion

You can use this method to ascertain which control events trigger actions. More than one action method may be called for a given event.

## See Also

- [func addTarget(Any?, action: Selector, for: UIControl.Event)](uicontrol/addtarget(_:action:for:).md)
  Associates a target object and action method with the control.
- [func removeTarget(Any?, action: Selector?, for: UIControl.Event)](uicontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.
- [var allTargets: Set<AnyHashable>](uicontrol/alltargets.md)
  Returns all target objects associated with the control.
- [func addAction(UIAction, for: UIControl.Event)](uicontrol/addaction(_:for:).md)
- [func removeAction(UIAction, for: UIControl.Event)](uicontrol/removeaction(_:for:).md)
- [func removeAction(identifiedBy: UIAction.Identifier, for: UIControl.Event)](uicontrol/removeaction(identifiedby:for:).md)
- [func actions(forTarget: Any?, forControlEvent: UIControl.Event) -> [String]?](uicontrol/actions(fortarget:forcontrolevent:).md)
  Returns the actions performed on a target object when the specified event occurs.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](uicontrol/enumerateeventhandlers(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/allcontrolevents)*