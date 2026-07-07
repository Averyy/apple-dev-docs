# CardSession.Event.readerDeselected

**Framework**: Core NFC  
**Kind**: case

The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case readerDeselected
```

## See Also

- [CardSession.Event.sessionStarted](cardsession/event/sessionstarted.md)
  The card session successfully started.
- [CardSession.Event.readerDetected](cardsession/event/readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [case received(CardSession.APDU)](cardsession/event/received(_:).md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.APDU](cardsession/apdu.md)
  An Application Programming Data Unit (APDU) received from the NFC card reader.
- [case sessionInvalidated(reason: CardSession.Error)](cardsession/event/sessioninvalidated(reason:).md)
  The session became invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event/readerdeselected)*