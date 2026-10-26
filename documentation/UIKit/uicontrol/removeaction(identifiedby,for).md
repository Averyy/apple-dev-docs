# removeAction(identifiedBy:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the action with the provided identifier from the set of passed control events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeAction(identifiedBy actionIdentifier: UIAction.Identifier, for controlEvents: UIControl.Event)
```

```objc
- (void) removeActionForIdentifier:(UIActionIdentifier) actionIdentifier forControlEvents:(UIControlEvents) controlEvents;
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/removeaction(identifiedby:for:))*