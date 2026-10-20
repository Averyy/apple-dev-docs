# sendAction(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) sendAction:(UIAction *) action;
```

## See Also

### Triggering actions
- [func performPrimaryAction()](./performprimaryaction%28%29.md)
  Calls the method associated with the control’s primary action.
- [func sendAction(Selector, to: Any?, for: UIEvent?)](./sendaction%28_,to,for%29.md)
  Calls the specified action method.
- [func sendActions(for: UIControl.Event)](./sendactions%28for%29.md)
  Calls the action methods associated with the specified events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/sendaction(_:))*