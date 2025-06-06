# performPrimaryAction()

**Framework**: UIKit  
**Kind**: method

Calls the method associated with the control’s primary action.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func performPrimaryAction()
```

#### Discussion

This method invokes the primary action for the control, whether it’s a direct action, for example, a button tap, or presents further UI, for example, a contextual menu.

## See Also

- [func sendAction(UIAction)](uicontrol/sendaction(_:).md)
- [func sendAction(Selector, to: Any?, for: UIEvent?)](uicontrol/sendaction(_:to:for:).md)
  Calls the specified action method.
- [func sendActions(for: UIControl.Event)](uicontrol/sendactions(for:).md)
  Calls the action methods associated with the specified events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/performprimaryaction())*