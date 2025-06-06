# shouldExpire

**Framework**: Messages  
**Kind**: property

A Boolean value that determines whether the message should expire after being read.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var shouldExpire: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the message should expire after it is read. Expired messages are deleted a short time after being read by the recipient. The recipient may opt to keep the message.

The `shouldExpire` property defaults to [`false`](https://developer.apple.com/documentation/swift/false).

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
- [var session: MSSession?](msmessage/session.md)
  The session that this message belongs to.
- [var summaryText: String?](msmessage/summarytext.md)
  A succinct description of the message.
- [var url: URL?](msmessage/url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/shouldexpire)*