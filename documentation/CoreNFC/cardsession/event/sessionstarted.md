# CardSession.Event.sessionStarted

**Framework**: Core NFC  
**Kind**: case  
**Role**: Case

The card session successfully started.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
case sessionStarted
```

## See Also

### Events
- [CardSession.Event.readerDetected](./readerdetected.md)
  The session detected the RF field of an external NFC reader.
- [case received(CardSession.APDU)](./received%28_%29.md)
  The session received an Application Programming Data Unit (ADPU).
- [CardSession.APDU](../apdu.md)
  An Application Programming Data Unit (APDU) received from the NFC card reader.
- [CardSession.Event.readerDeselected](./readerdeselected.md)
  The session lost the RF link or the currently-selected Application Identifier (AID) became deselected.
- [case sessionInvalidated(reason: CardSession.Error)](./sessioninvalidated%28reason%29.md)
  The session became invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/event/sessionstarted)*