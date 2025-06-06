# didResignActive(with:)

**Framework**: Messages  
**Kind**: method

Invoked after the message resigns its active status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func didResignActive(with conversation: MSConversation)
```

#### Discussion

Override this method to perform any cleanup activities after the Messages extension has been dismissed. Avoid doing any time-consuming tasks in your implementation.

## Parameters

- `conversation`: The conversation that the user is currently viewing in the Messages app.

## See Also

- [var activeConversation: MSConversation?](msmessagesappviewcontroller/activeconversation.md)
  The conversation currently displayed in the transcript.
- [func dismiss()](msmessagesappviewcontroller/dismiss.md)
  Dismisses the extension and marks it for termination.
- [func willBecomeActive(with: MSConversation)](msmessagesappviewcontroller/willbecomeactive(with:).md)
  Invoked just before the Messages extension becomes active.
- [func didBecomeActive(with: MSConversation)](msmessagesappviewcontroller/didbecomeactive(with:).md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](msmessagesappviewcontroller/willresignactive(with:).md)
  Invoked just before the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didresignactive(with:))*