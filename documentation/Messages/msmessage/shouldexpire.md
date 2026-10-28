# shouldExpire

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the message should expire after being read.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var shouldExpire: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL shouldExpire;
```

## Discussion

If [`true`](../../Swift/true.md), the message should expire after it is read. Expired messages are deleted a short time after being read by the recipient. The recipient may opt to keep the message.

The `shouldExpire` property defaults to [`false`](../../Swift/false.md).

## See Also

### Message Properties
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](./error.md)
  An error object describing why the system failed to send the message.
- [var isPending: Bool](./ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](./layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](./senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](./session.md)
  The session that this message belongs to.
- [var summaryText: String?](./summarytext.md)
  A succinct description of the message.
- [var url: URL?](./url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/shouldexpire)*