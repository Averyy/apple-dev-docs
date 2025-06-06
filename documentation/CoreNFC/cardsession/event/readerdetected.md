# CardSession.Event.readerDetected

**Framework**: Core NFC  
**Kind**: case

The session detected the RF field of an external NFC reader.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case readerDetected
```

## See Also

- [CardSession.Event.sessionStarted](cardsession/event/sessionstarted.md)
  The card session successfully started.
- [case received(CardSession.APDU)](cardsession/event/received(_:).md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.APDU](cardsession/apdu.md)
  An Application Programming Data Unit (APDU) received from the NFC card reader.
- [CardSession.Event.readerDeselected](cardsession/event/readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.
- [case sessionInvalidated(reason: CardSession.Error)](cardsession/event/sessioninvalidated(reason:).md)
  The session became invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event/readerdetected)*