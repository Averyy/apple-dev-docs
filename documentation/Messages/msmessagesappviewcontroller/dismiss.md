# dismiss()

**Framework**: Messages  
**Kind**: method

Dismisses the extension and marks it for termination.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func dismiss()
```

#### Discussion

Call this method to dismiss the extension. The system displays the keyboard if there is any content in the Messages app’s input field. If the input field is empty, the system dismisses the keyboard entirely.

This method also marks the extension as eligible for termination, causing the system to call the view controller’s [`willResignActive(with:)`](msmessagesappviewcontroller/willresignactive(with:).md) and [`didResignActive(with:)`](msmessagesappviewcontroller/didresignactive(with:).md) methods.

## See Also

- [var activeConversation: MSConversation?](msmessagesappviewcontroller/activeconversation.md)
  The conversation currently displayed in the transcript.
- [func willBecomeActive(with: MSConversation)](msmessagesappviewcontroller/willbecomeactive(with:).md)
  Invoked just before the Messages extension becomes active.
- [func didBecomeActive(with: MSConversation)](msmessagesappviewcontroller/didbecomeactive(with:).md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](msmessagesappviewcontroller/willresignactive(with:).md)
  Invoked just before the message resigns its active status.
- [func didResignActive(with: MSConversation)](msmessagesappviewcontroller/didresignactive(with:).md)
  Invoked after the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/dismiss())*