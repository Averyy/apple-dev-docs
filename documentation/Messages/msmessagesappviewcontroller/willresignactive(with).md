# willResignActive(with:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Invoked just before the message resigns its active status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func willResignActive(with conversation: MSConversation)
```

```objc
- (void) willResignActiveWithConversation:(MSConversation *) conversation;
```

#### Discussion

Override this method to perform any cleanup activities just before the Messages extension is dismissed. Avoid doing any time-consuming tasks in your implementation. This method should return as quickly as possible. Also, avoid making asynchronous calls, because the extension might terminate before the asynchronous tasks have completed.

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
- [func didResignActive(with: MSConversation)](./didresignactive%28with%29.md)
  Invoked after the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/willresignactive(with:))*