# removeTarget(_:action:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Stops the delivery of events to the specified target object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeTarget(_ target: Any?, action: Selector?, for controlEvents: UIControl.Event)
```

```objc
- (void) removeTarget:(id) target action:(SEL) action forControlEvents:(UIControlEvents) controlEvents;
```

#### Discussion

Use this method to prevent the delivery of control events to target objects associated with control. If you specify a valid object in the `target` parameter, this method stops the delivery of the specified events to all action methods associated with that object. If you specify `nil` for the `target` parameter, this method prevents the delivery of those events to all action methods of all target objects.

Although the `action` parameter is not considered when stopping the delivery of events, you should specify an appropriate value anyway. If the specified target/action combination no longer has any valid control events associated with it, the control cleans up its corresponding internal data structures. Doing so can affect the set of objects returned by the [`allTargets`](./alltargets.md) method.

## Parameters

- `target`: A target object registered with the control. Specify `nil` to remove the specified control events for all target objects.
- `action`: A selector identifying a registered action method. You may specify `nil` for this parameter.
- `controlEvents`: A bitmask specifying the control events that you want to remove for the specified `target` object. For a list of possible constants, see [`UIControl.Event`](./event.md).

## See Also

### Managing the control’s targets and actions
- [func addTarget(Any?, action: Selector, for: UIControl.Event)](./addtarget%28_,action,for%29.md)
  Associates a target object and action method with the control.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/removetarget(_:action:for:))*