# didResignActive(with:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Invoked after the message resigns its active status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func didResignActive(with conversation: MSConversation)
```

```objc
- (void) didResignActiveWithConversation:(MSConversation *) conversation;
```

## Discussion

Override this method to perform any cleanup activities after the Messages extension has been dismissed. Avoid doing any time-consuming tasks in your implementation.

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
- [func didBecomeActive(with: MSConversation)](./didbecomeactive%28with%29.md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](./willresignactive%28with%29.md)
  Invoked just before the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didresignactive(with:))*