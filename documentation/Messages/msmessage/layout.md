# layout

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

A layout object that defines the message’s appearance.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
var layout: MSMessageLayout? { get set }
```

```objc
@property (nonatomic, copy, nullable) MSMessageLayout * layout;
```

#### Discussion

Set this property to a concrete subclass of the abstract [`MSMessageLayout`](../msmessagelayout.md) class.

By default, the `layout` property is set to `nil`.

## See Also

### Message Properties
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](./error.md)
  An error object describing why the system failed to send the message.
- [var isPending: Bool](./ispending.md)
  A Boolean value that indicates whether the message is pending or whether it has been sent or received.
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

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/layout)*