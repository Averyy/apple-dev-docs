# CardSession.Event.sessionStarted

**Framework**: Core NFC  
**Kind**: case

The card session successfully started.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case sessionStarted
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event/sessionstarted)*