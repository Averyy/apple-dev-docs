# MessageComposeResult

**Framework**: Message UI  
**Kind**: enum

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

## Topics

### Constants
- [MessageComposeResult.cancelled](messagecomposeresult/cancelled.md)
  The user canceled the composition.
- [MessageComposeResult.sent](messagecomposeresult/sent.md)
  The user successfully queued or sent the message.
- [MessageComposeResult.failed](messagecomposeresult/failed.md)
  The user’s attempt to save or send the message was unsuccessful.
### Initializers
- [init?(rawValue: Int)](messagecomposeresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func messageComposeViewController(MFMessageComposeViewController, didFinishWith: MessageComposeResult)](mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller(_:didfinishwith:).md)
  Tells the delegate that the user finished composing the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/messagecomposeresult)*