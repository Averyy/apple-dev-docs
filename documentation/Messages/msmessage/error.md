# error

**Framework**: Messages  
**Kind**: property

An error object describing why the system failed to send the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var error: (any Error)? { get set }
```

#### Discussion

The system sets the `error` property when an error occurs while sending this message. It is set to `nil` if you have not yet sent the message or if you have sent the message successfully.

## See Also

- [var accessibilityLabel: String?](msmessage/accessibilitylabel.md)
  A localized string that describes the message.
- [var isPending: Bool](msmessage/ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](msmessage/layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](msmessage/senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](msmessage/session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](msmessage/shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](msmessage/summarytext.md)
  A succinct description of the message.
- [var url: URL?](msmessage/url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/error)*