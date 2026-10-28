# CardSession.Event.sessionInvalidated(reason:)

**Framework**: Core NFC  
**Kind**: case  
**Role**: Case

The session became invalid.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
case sessionInvalidated(reason: CardSession.Error)
```

## Discussion

This is the last event produced by the event stream before the stream finishes. The reason can be any [`CardSession.Error`](../error.md) except [`CardSession.Error.transmissionError`](../error/transmissionerror.md).

## Parameters

- `reason`: The reason the session became invalid.

## See Also

### Events
- [CardSession.Event.sessionStarted](./sessionstarted.md)
  The card session successfully started.
- [CardSession.Event.readerDetected](./readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [case received(CardSession.APDU)](./received%28_%29.md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.APDU](../apdu.md)
  An Application Programming Data Unit (APDU) received from the NFC card reader.
- [CardSession.Event.readerDeselected](./readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event/sessioninvalidated(reason:))*