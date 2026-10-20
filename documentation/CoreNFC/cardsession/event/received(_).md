# CardSession.Event.received(_:)

**Framework**: Core NFC  
**Kind**: case  
**Role**: Case

The session received an Application Programming Data Unit (ADPU).

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
case received(CardSession.APDU)
```

## Parameters

- `CardSession.APDU`: The ADPU received from the session.

## See Also

### Events
- [CardSession.Event.sessionStarted](./sessionstarted.md)
  The card session successfully started.
- [CardSession.Event.readerDetected](./readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [CardSession.APDU](../apdu.md)
  An Application Programming Data Unit (APDU) received from the NFC card reader.
- [CardSession.Event.readerDeselected](./readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.
- [case sessionInvalidated(reason: CardSession.Error)](./sessioninvalidated%28reason%29.md)
  The session became invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event/received(_:))*