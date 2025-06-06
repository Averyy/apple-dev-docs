# CardSession.Event.sessionInvalidated(reason:)

**Framework**: Core NFC  
**Kind**: case

The session became invalid.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case sessionInvalidated(reason: CardSession.Error)
```

#### Discussion

This is the last event produced by the event stream before the stream finishes. The reason can be any [`CardSession.Error`](cardsession/error.md) except [`CardSession.Error.transmissionError`](cardsession/error/transmissionerror.md).

## Parameters

- `reason`: The reason the session became invalid.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event/sessioninvalidated(reason:))*