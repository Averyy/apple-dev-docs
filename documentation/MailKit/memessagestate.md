# MEMessageState

**Framework**: MailKit  
**Kind**: enum  
**Role**: Enumeration

The state of a message: sent, unsent, or received.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum MEMessageState
```

```c
enum MEMessageState : NSInteger;
```

## Topics

### Determining Message State
- [MEMessageState.draft](./memessagestate/draft.md)
  A state that indicates the user is composing the message, and hasn’t sent it yet.
- [MEMessageState.received](./memessagestate/received.md)
  A state that indicates the system has received and stored the message.
- [MEMessageState.sending](./memessagestate/sending.md)
  A state that indicates the system is in the process of sending the message.
### Initializers
- [init?(rawValue: Int)](./memessagestate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Message Properties
- [class MEMessage](./memessage.md)
  An object that contains information about a mail message, such as the subject, addressees, date sent, and the message contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagestate)*