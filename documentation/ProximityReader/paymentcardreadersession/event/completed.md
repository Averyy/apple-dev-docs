# PaymentCardReaderSession.Event.completed

**Framework**: ProximityReader  
**Kind**: case

An event that indicates the reader completed the reading process.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case completed
```

## See Also

- [PaymentCardReaderSession.Event.cardDetected](paymentcardreadersession/event/carddetected.md)
  An event that indicates the reader detected the presence of a card.
- [PaymentCardReaderSession.Event.readCancelled](paymentcardreadersession/event/readcancelled.md)
  An event that indicates the cancellation of the operation.
- [PaymentCardReaderSession.Event.readNotCompleted](paymentcardreadersession/event/readnotcompleted.md)
  An event that indicates the read operation didn’t finish.
- [PaymentCardReaderSession.Event.readyForTap](paymentcardreadersession/event/readyfortap.md)
  An event that indicates the reader is ready for someone to move their card within range of the iPhone.
- [PaymentCardReaderSession.Event.removeCard](paymentcardreadersession/event/removecard.md)
  An event that indicates the consumer can move the card away from the device.
- [PaymentCardReaderSession.Event.retry](paymentcardreadersession/event/retry.md)
  An event that indicates the UI triggered a retry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/event/completed)*