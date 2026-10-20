# MessageComposeResult

**Framework**: Message UI  
**Kind**: enum  
**Role**: Enumeration

These constants describe the result of the message-composition interface.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum MessageComposeResult
```

```c
enum MessageComposeResult : NSInteger;
```

## Topics

### Constants
- [MessageComposeResult.cancelled](./messagecomposeresult/cancelled.md)
  The user canceled the composition.
- [MessageComposeResult.sent](./messagecomposeresult/sent.md)
  The user successfully queued or sent the message.
- [MessageComposeResult.failed](./messagecomposeresult/failed.md)
  The user’s attempt to save or send the message was unsuccessful.
### Initializers
- [init?(rawValue: Int)](./messagecomposeresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to the Message Completion
- [func messageComposeViewController(MFMessageComposeViewController, didFinishWith: MessageComposeResult)](./mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller%28_,didfinishwith%29.md)
  Tells the delegate that the user finished composing the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/messagecomposeresult)*