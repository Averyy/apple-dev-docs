# session

**Framework**: Messages  
**Kind**: property

The session that this message belongs to.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var session: MSSession? { get }
```

#### Discussion

The `session` property is set to the session object passed to the [`init(session:)`](msmessage/init(session:).md) initializer; otherwise, it is set to `nil`.

## See Also

- [var accessibilityLabel: String?](msmessage/accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](msmessage/error.md)
  An error object describing why the system failed to send the message.
- [var isPending: Bool](msmessage/ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](msmessage/layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](msmessage/senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var shouldExpire: Bool](msmessage/shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](msmessage/summarytext.md)
  A succinct description of the message.
- [var url: URL?](msmessage/url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/session)*