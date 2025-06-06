# activeConversation

**Framework**: Messages  
**Kind**: property

The conversation currently displayed in the transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var activeConversation: MSConversation? { get }
```

#### Discussion

This is the conversation that the user is currently viewing in the Messages app.

## See Also

- [func dismiss()](msmessagesappviewcontroller/dismiss.md)
  Dismisses the extension and marks it for termination.
- [func willBecomeActive(with: MSConversation)](msmessagesappviewcontroller/willbecomeactive(with:).md)
  Invoked just before the Messages extension becomes active.
- [func didBecomeActive(with: MSConversation)](msmessagesappviewcontroller/didbecomeactive(with:).md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](msmessagesappviewcontroller/willresignactive(with:).md)
  Invoked just before the message resigns its active status.
- [func didResignActive(with: MSConversation)](msmessagesappviewcontroller/didresignactive(with:).md)
  Invoked after the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/activeconversation)*