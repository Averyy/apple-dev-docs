# error

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

An error object describing why the system failed to send the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var error: (any Error)? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSError * error;
```

#### Discussion

The system sets the `error` property when an error occurs while sending this message. It is set to `nil` if you have not yet sent the message or if you have sent the message successfully.

## See Also

### Message Properties
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A localized string that describes the message.
- [var isPending: Bool](./ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
- [var layout: MSMessageLayout?](./layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](./senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](./session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](./shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](./summarytext.md)
  A succinct description of the message.
- [var url: URL?](./url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/error)*