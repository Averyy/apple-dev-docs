# PaymentCardReader.Event

**Framework**: ProximityReader  
**Kind**: enum

An event you receive indicating the state or activity of the payment card reader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum Event
```

## Topics

### Getting the event type
- [PaymentCardReader.Event.cardDetected](paymentcardreader/event/carddetected.md)
  An event that indicates the reader detected the presence of a card.
- [PaymentCardReader.Event.pinEntryCompleted](paymentcardreader/event/pinentrycompleted.md)
  An event that indicates the reader captured the card PIN successfully.
- [PaymentCardReader.Event.pinEntryRequested](paymentcardreader/event/pinentryrequested.md)
  An event that indicates the reader requested the card PIN.
- [PaymentCardReader.Event.readCancelled](paymentcardreader/event/readcancelled.md)
  An event that indicates the cancellation of the operation.
- [PaymentCardReader.Event.readCompleted](paymentcardreader/event/readcompleted.md)
  An event that indicates the reader completed the reading process.
- [PaymentCardReader.Event.readNotCompleted](paymentcardreader/event/readnotcompleted.md)
  An event that indicates the read operation didn’t finish.
- [PaymentCardReader.Event.readRetry](paymentcardreader/event/readretry.md)
  An event that indicates the UI triggered a retry.
- [PaymentCardReader.Event.readyForTap](paymentcardreader/event/readyfortap.md)
  An event that indicates the reader is ready for someone to move their card within range of the iPhone.
- [PaymentCardReader.Event.removeCard](paymentcardreader/event/removecard.md)
  An event that indicates the consumer can move the card away from the device.
- [PaymentCardReader.Event.updateProgress(_:)](paymentcardreader/event/updateprogress(_:).md)
  The current update progress, specified as an integer value from 1 to 100.
- [PaymentCardReader.Event.userInterfaceDismissed](paymentcardreader/event/userinterfacedismissed.md)
  An event that indicates the UI has been closed.
- [PaymentCardReader.Event.notReady](paymentcardreader/event/notready.md)
  A reader that is not ready to perform transactions.
### Getting the event name
- [var name: String](paymentcardreader/event/name.md)
  The name of the event.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [let events: AsyncStream<PaymentCardReader.Event>](paymentcardreader/events.md)
  A stream of events you receive indicating the activities of the payment card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/event)*