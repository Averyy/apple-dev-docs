# sendActions(for:)

**Framework**: UIKit  
**Kind**: method

Calls the action methods associated with the specified events.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func sendActions(for controlEvents: UIControl.Event)
```

#### Discussion

You call this method when you want the control to perform the actions associated with the specified events. This method iterates over the control’s registered targets and action methods and calls the [`sendAction(_:to:for:)`](uicontrol/sendaction(_:to:for:).md) method for each one that is associated with an event in the `controlEvents` parameter.

## Parameters

- `controlEvents`: A bitmask with flags that specify the control events for which the control sends action messages. See [`UIControl.Event`](uicontrol/event.md) for bitmask constants.

## See Also

- [func addTarget(Any?, action: Selector, for: UIControl.Event)](uicontrol/addtarget(_:action:for:).md)
  Associates a target object and action method with the control.
- [func performPrimaryAction()](uicontrol/performprimaryaction.md)
  Calls the method associated with the control’s primary action.
- [func sendAction(UIAction)](uicontrol/sendaction(_:).md)
  Like -sendAction:to:forEvent:, this method is called by -sendActionsForControlEvents:. You may override this method to observe or modify behavior. If you override this method, you should call super precisely once to dispatch the action, or not call super to suppress sending that action.
- [func sendAction(Selector, to: Any?, for: UIEvent?)](uicontrol/sendaction(_:to:for:).md)
  Calls the specified action method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/sendactions(for:))*