# allTargets

**Framework**: UIKit  
**Kind**: property

Returns all target objects associated with the control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allTargets: Set<AnyHashable> { get }
```

#### Return Value

A set of all target objects associated with the control. The returned set may include one or more [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) objects to indicate actions that are dispatched to the responder chain.

## See Also

- [func addTarget(Any?, action: Selector, for: UIControl.Event)](uicontrol/addtarget(_:action:for:).md)
  Associates a target object and action method with the control.
- [func removeTarget(Any?, action: Selector?, for: UIControl.Event)](uicontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.
- [func addAction(UIAction, for: UIControl.Event)](uicontrol/addaction(_:for:).md)
- [func removeAction(UIAction, for: UIControl.Event)](uicontrol/removeaction(_:for:).md)
- [func removeAction(identifiedBy: UIAction.Identifier, for: UIControl.Event)](uicontrol/removeaction(identifiedby:for:).md)
- [func actions(forTarget: Any?, forControlEvent: UIControl.Event) -> [String]?](uicontrol/actions(fortarget:forcontrolevent:).md)
  Returns the actions performed on a target object when the specified event occurs.
- [var allControlEvents: UIControl.Event](uicontrol/allcontrolevents.md)
  Returns the events for which the control has associated actions.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](uicontrol/enumerateeventhandlers(_:).md)
- [UIControl.Event](uicontrol/event.md)
  Constants describing the types of events possible for controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/alltargets)*