# actions(forTarget:forControlEvent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the actions performed on a target object when the specified event occurs.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func actions(forTarget target: Any?, forControlEvent controlEvent: UIControl.Event) -> [String]?
```

```objc
- (NSArray<NSString *> *) actionsForTarget:(id) target forControlEvent:(UIControlEvents) controlEvent;
```

## Return Value

An array [`NSString`](../../Foundation/nsstring.md) objects containing the selector names of the corresponding action methods, or `nil` if there are no action methods associated with the specified target object and control event.

## Discussion

Use this method to determine what action methods are called on the specified object in response to a particular control event. You can use the [`NSSelectorFromString(_:)`](../../Foundation/nsselectorfromstring%28_%29.md) function to convert the returned strings to valid selectors, as needed.

## Parameters

- `target`: The target object—that is, an object that has an action method associated with this control. You must pass an explicit object for this method to return a meaningful result. Specifying `nil` always returns `nil`.
- `controlEvent`: A single control event constant representing the event for which you want the list of action methods. For a list of possible constants, see [`UIControl.Event`](./event.md)

## See Also

### Related Documentation
- [func sendAction(Selector, to: Any?, for: UIEvent?)](./sendaction%28_,to,for%29.md)
  Calls the specified action method.
- [func sendActions(for: UIControl.Event)](./sendactions%28for%29.md)
  Calls the action methods associated with the specified events.
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
- [var allControlEvents: UIControl.Event](./allcontrolevents.md)
  Returns the events for which the control has associated actions.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](./enumerateeventhandlers%28_%29.md)
- [UIControl.Event](./event.md)
  Constants describing the types of events possible for controls.
- [- enumerateEventHandlers:](./enumerateeventhandlers_.md)
  Iterate over the event handlers installed on this control at the time this method is called. For each call, either actionHandler or action will be non-nil. controlEvents is always non-zero. Setting *stop to YES will terminate the enumeration early. It is legal to manipulate the control’s event handlers within the block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/actions(fortarget:forcontrolevent:))*