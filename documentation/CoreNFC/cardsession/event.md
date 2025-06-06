# CardSession.Event

**Framework**: Core NFC  
**Kind**: enum

A type that enumerates events produced by a card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum Event
```

## Topics

### Events
- [CardSession.Event.sessionStarted](cardsession/event/sessionstarted.md)
  The card session successfully started.
- [CardSession.Event.readerDetected](cardsession/event/readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [case received(CardSession.APDU)](cardsession/event/received(_:).md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.APDU](cardsession/apdu.md)
  An Application Programming Data Unit (APDU) received from the NFC card reader.
- [CardSession.Event.readerDeselected](cardsession/event/readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.
- [case sessionInvalidated(reason: CardSession.Error)](cardsession/event/sessioninvalidated(reason:).md)
  The session became invalid.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var eventStream: CardSession.EventStream](cardsession/eventstream-swift.property.md)
  An asynchronous sequence of events from the card session.
- [CardSession.EventStream](cardsession/eventstream-swift.class.md)
  An asynchronous sequence of events produced by a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event)*