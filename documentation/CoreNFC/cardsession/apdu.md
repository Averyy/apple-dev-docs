# CardSession.APDU

**Framework**: Core NFC  
**Kind**: class

An Application Programming Data Unit (APDU) received from the NFC card reader.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
final class APDU
```

## Topics

### Receiving data
- [let payload: Data](cardsession/apdu/payload.md)
  The APDU data received from the NFC reader.
### Communicating with the card session
- [func respond(response: Data) async throws](cardsession/apdu/respond(response:).md)
  Respond to the session after receiving and processing an APDU.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CardSession.Event.sessionStarted](cardsession/event/sessionstarted.md)
  The card session successfully started.
- [CardSession.Event.readerDetected](cardsession/event/readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [case received(CardSession.APDU)](cardsession/event/received(_:).md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.Event.readerDeselected](cardsession/event/readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.
- [case sessionInvalidated(reason: CardSession.Error)](cardsession/event/sessioninvalidated(reason:).md)
  The session became invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/apdu)*