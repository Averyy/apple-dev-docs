# dismiss()

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Dismisses the extension and marks it for termination.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func dismiss()
```

```objc
- (void) dismiss;
```

#### Discussion

Call this method to dismiss the extension. The system displays the keyboard if there is any content in the Messages app’s input field. If the input field is empty, the system dismisses the keyboard entirely.

This method also marks the extension as eligible for termination, causing the system to call the view controller’s [`willResignActive(with:)`](./willresignactive%28with%29.md) and [`didResignActive(with:)`](./didresignactive%28with%29.md) methods.

## See Also

### Managing the Extension’s State
- [var activeConversation: MSConversation?](./activeconversation.md)
  The conversation currently displayed in the transcript.
- [func willBecomeActive(with: MSConversation)](./willbecomeactive%28with%29.md)
  Invoked just before the Messages extension becomes active.
- [func didBecomeActive(with: MSConversation)](./didbecomeactive%28with%29.md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](./willresignactive%28with%29.md)
  Invoked just before the message resigns its active status.
- [func didResignActive(with: MSConversation)](./didresignactive%28with%29.md)
  Invoked after the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/dismiss())*