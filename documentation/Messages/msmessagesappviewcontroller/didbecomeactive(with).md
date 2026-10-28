# didBecomeActive(with:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Invoked after the Messages extension becomes active.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func didBecomeActive(with conversation: MSConversation)
```

```objc
- (void) didBecomeActiveWithConversation:(MSConversation *) conversation;
```

## Discussion

Override this method to respond after the Messages extension becomes active. The extension becomes active both when the user selects the extension from the app drawer, and when the user selects a message in the transcript that represents an [`MSMessage`](../msmessage.md) object created by a copy of the extension.

## Parameters

- `conversation`: The conversation that the user is currently viewing in the Messages app.

## See Also

### Managing the Extension’s State
- [var activeConversation: MSConversation?](./activeconversation.md)
  The conversation currently displayed in the transcript.
- [func dismiss()](./dismiss%28%29.md)
  Dismisses the extension and marks it for termination.
- [func willBecomeActive(with: MSConversation)](./willbecomeactive%28with%29.md)
  Invoked just before the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](./willresignactive%28with%29.md)
  Invoked just before the message resigns its active status.
- [func didResignActive(with: MSConversation)](./didresignactive%28with%29.md)
  Invoked after the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didbecomeactive(with:))*