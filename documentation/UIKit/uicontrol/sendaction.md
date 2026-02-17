# sendAction(_:)

**Framework**: UIKit  
**Kind**: method

Like -sendAction:to:forEvent:, this method is called by -sendActionsForControlEvents:. You may override this method to observe or modify behavior. If you override this method, you should call super precisely once to dispatch the action, or not call super to suppress sending that action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func sendAction(_ action: UIAction)
```

## See Also

- [func performPrimaryAction()](uicontrol/performprimaryaction.md)
  Calls the method associated with the control’s primary action.
- [func sendAction(Selector, to: Any?, for: UIEvent?)](uicontrol/sendaction(_:to:for:).md)
  Calls the specified action method.
- [func sendActions(for: UIControl.Event)](uicontrol/sendactions(for:).md)
  Calls the action methods associated with the specified events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/sendaction(_:))*