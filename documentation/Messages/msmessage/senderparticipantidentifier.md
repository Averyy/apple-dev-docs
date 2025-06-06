# senderParticipantIdentifier

**Framework**: Messages  
**Kind**: property

A UUID identifying the participant that sent the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var senderParticipantIdentifier: UUID { get }
```

#### Discussion

The value of this UUID is scoped to the current device. Each device participating in the conversation will have a different UUID for the message’s sender.

By default, the `senderParticipantIdentifier` property is set to `nil` when a new message is first instantiated. It is set to the participant’s UUID as soon as the message is inserted into the conversation.

## See Also

- [var accessibilityLabel: String?](msmessage/accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](msmessage/error.md)
  An error object describing why the system failed to send the message.
- [var isPending: Bool](msmessage/ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](msmessage/layout.md)
  A layout object that defines the message’s appearance.
- [var session: MSSession?](msmessage/session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](msmessage/shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](msmessage/summarytext.md)
  A succinct description of the message.
- [var url: URL?](msmessage/url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/senderparticipantidentifier)*