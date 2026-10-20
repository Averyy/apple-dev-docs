# activeConversation

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The conversation currently displayed in the transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var activeConversation: MSConversation? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) MSConversation * activeConversation;
```

#### Discussion

This is the conversation that the user is currently viewing in the Messages app.

## See Also

### Managing the Extension’s State
- [func dismiss()](./dismiss%28%29.md)
  Dismisses the extension and marks it for termination.
- [func willBecomeActive(with: MSConversation)](./willbecomeactive%28with%29.md)
  Invoked just before the Messages extension becomes active.
- [func didBecomeActive(with: MSConversation)](./didbecomeactive%28with%29.md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](./willresignactive%28with%29.md)
  Invoked just before the message resigns its active status.
- [func didResignActive(with: MSConversation)](./didresignactive%28with%29.md)
  Invoked after the message resigns its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/activeconversation)*