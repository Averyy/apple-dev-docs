# CardSession.APDU

**Framework**: Core NFC  
**Kind**: class  
**Role**: Class

An Application Programming Data Unit (APDU) received from the NFC card reader.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
final class APDU
```

## Topics

### Receiving data
- [let payload: Data](./apdu/payload.md)
  The APDU data received from the NFC reader.
### Communicating with the card session
- [func respond(response: Data) async throws](./apdu/respond%28response%29.md)
  Respond to the session after receiving and processing an APDU.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Events
- [CardSession.Event.sessionStarted](./event/sessionstarted.md)
  The card session successfully started.
- [CardSession.Event.readerDetected](./event/readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [case received(CardSession.APDU)](./event/received%28_%29.md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.Event.readerDeselected](./event/readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.
- [case sessionInvalidated(reason: CardSession.Error)](./event/sessioninvalidated%28reason%29.md)
  The session became invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/apdu)*