# actions(forTarget:forControlEvent:)

**Framework**: UIKit  
**Kind**: method

Returns the actions performed on a target object when the specified event occurs.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func actions(forTarget target: Any?, forControlEvent controlEvent: UIControl.Event) -> [String]?
```

#### Return Value

An array [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects containing the selector names of the corresponding action methods, or `nil` if there are no action methods associated with the specified target object and control event.

#### Discussion

Use this method to determine what action methods are called on the specified object in response to a particular control event. You can use the [`NSSelectorFromString(_:)`](https://developer.apple.com/documentation/Foundation/NSSelectorFromString(_:)) function to convert the returned strings to valid selectors, as needed.

## Parameters

- `target`: The target object—that is, an object that has an action method associated with this control. You must pass an explicit object for this method to return a meaningful result. Specifying   always returns  .
- `controlEvent`: A single control event constant representing the event for which you want the list of action methods. For a list of possible constants, see 

## See Also

- [func sendAction(Selector, to: Any?, for: UIEvent?)](uicontrol/sendaction(_:to:for:).md)
  Calls the specified action method.
- [func sendActions(for: UIControl.Event)](uicontrol/sendactions(for:).md)
  Calls the action methods associated with the specified events.
- [func addTarget(Any?, action: Selector, for: UIControl.Event)](uicontrol/addtarget(_:action:for:).md)
  Associates a target object and action method with the control.
- [func removeTarget(Any?, action: Selector?, for: UIControl.Event)](uicontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.
- [var allTargets: Set<AnyHashable>](uicontrol/alltargets.md)
  Returns all target objects associated with the control.
- [func addAction(UIAction, for: UIControl.Event)](uicontrol/addaction(_:for:).md)
  Adds the UIAction to a given event. UIActions are uniqued based on their identifier, and subsequent actions with the same identifier replace previously added actions. You may add multiple UIActions for corresponding controlEvents, and you may add the same action to multiple controlEvents.
- [func removeAction(UIAction, for: UIControl.Event)](uicontrol/removeaction(_:for:).md)
  Removes the action from the set of passed control events.
- [func removeAction(identifiedBy: UIAction.Identifier, for: UIControl.Event)](uicontrol/removeaction(identifiedby:for:).md)
  Removes the action with the provided identifier from the set of passed control events.
- [var allControlEvents: UIControl.Event](uicontrol/allcontrolevents.md)
  Returns the events for which the control has associated actions.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](uicontrol/enumerateeventhandlers(_:).md)
- [UIControl.Event](uicontrol/event.md)
  Constants describing the types of events possible for controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/actions(fortarget:forcontrolevent:))*