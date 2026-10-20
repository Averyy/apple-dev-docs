# PaymentCardReaderSession.Event.completed

**Framework**: ProximityReader  
**Kind**: case  
**Role**: Case

An event that indicates the reader completed the reading process.

**Availability**:
- iOS 15.4+ - Deprecated in 16.0
- iPadOS 15.4+ - Deprecated in 16.0
- Mac Catalyst 17.0+ - Deprecated in 17.0

> **Deprecated**: Use PaymentCardReader.Event

## Declaration

```swift
case completed
```

## See Also

### Getting the event type
- [PaymentCardReaderSession.Event.cardDetected](./carddetected.md)
  An event that indicates the reader detected the presence of a card.
- [PaymentCardReaderSession.Event.readCancelled](./readcancelled.md)
  An event that indicates the cancellation of the operation.
- [PaymentCardReaderSession.Event.readNotCompleted](./readnotcompleted.md)
  An event that indicates the read operation didn’t finish.
- [PaymentCardReaderSession.Event.readyForTap](./readyfortap.md)
  An event that indicates the reader is ready for someone to move their card within range of the iPhone.
- [PaymentCardReaderSession.Event.removeCard](./removecard.md)
  An event that indicates the consumer can move the card away from the device.
- [PaymentCardReaderSession.Event.retry](./retry.md)
  An event that indicates the UI triggered a retry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/event/completed)*