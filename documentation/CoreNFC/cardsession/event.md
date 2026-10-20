# CardSession.Event

**Framework**: Core NFC  
**Kind**: enum  
**Role**: Enumeration

A type that enumerates events produced by a card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum Event
```

## Topics

### Events
- [CardSession.Event.sessionStarted](./event/sessionstarted.md)
  The card session successfully started.
- [CardSession.Event.readerDetected](./event/readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [case received(CardSession.APDU)](./event/received%28_%29.md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.APDU](./apdu.md)
  An Application Programming Data Unit (APDU) received from the NFC card reader.
- [CardSession.Event.readerDeselected](./event/readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.
- [case sessionInvalidated(reason: CardSession.Error)](./event/sessioninvalidated%28reason%29.md)
  The session became invalid.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling card events
- [var eventStream: CardSession.EventStream](./eventstream-swift.property.md)
  An asynchronous sequence of events from the card session.
- [CardSession.EventStream](./eventstream-swift.class.md)
  An asynchronous sequence of events produced by a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event)*