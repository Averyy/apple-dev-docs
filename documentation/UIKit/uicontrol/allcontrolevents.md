# allControlEvents

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the events for which the control has associated actions.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allControlEvents: UIControl.Event { get }
```

```objc
@property (nonatomic, readonly) UIControlEvents allControlEvents;
```

#### Return Value

A bitmask of constants indicating the events for which this control has associated actions. For a list of possible constants, see the [`UIControl.Event`](./event.md) type.

#### Discussion

You can use this method to ascertain which control events trigger actions. More than one action method may be called for a given event.

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
- [func removeAction(identifiedBy: UIAction.Identifier, for: UIControl.Event)](./removeaction%28identifiedby,for%29.md)
  Removes the action with the provided identifier from the set of passed control events.
- [func actions(forTarget: Any?, forControlEvent: UIControl.Event) -> [String]?](./actions%28fortarget,forcontrolevent%29.md)
  Returns the actions performed on a target object when the specified event occurs.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](./enumerateeventhandlers%28_%29.md)
- [UIControl.Event](./event.md)
  Constants describing the types of events possible for controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/allcontrolevents)*