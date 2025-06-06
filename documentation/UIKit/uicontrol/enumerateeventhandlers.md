# enumerateEventHandlers(_:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func enumerateEventHandlers(_ iterator: (UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)
```

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
- [var allControlEvents: UIControl.Event](uicontrol/allcontrolevents.md)
  Returns the events for which the control has associated actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/enumerateeventhandlers(_:))*