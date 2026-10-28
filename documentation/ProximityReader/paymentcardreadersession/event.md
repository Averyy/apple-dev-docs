# PaymentCardReaderSession.Event

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

Optional events you can observe during the card-reading process.

**Availability**:
- iOS 15.4+ - Deprecated in 16.0
- iPadOS 15.4+ - Deprecated in 16.0
- Mac Catalyst 17.0+ - Deprecated in 17.0

> **Deprecated**: Use PaymentCardReader.Event

## Declaration

```swift
enum Event
```

## Overview

If you supply an event handler when reading a card, the session delivers appropriate events to your handler. Use them to update your UI or perform other app-specific tasks. You can also use them to provide accessibility-related feedback.

## Topics

### Getting the event type
- [PaymentCardReaderSession.Event.cardDetected](./event/carddetected.md)
  An event that indicates the reader detected the presence of a card.
- [PaymentCardReaderSession.Event.completed](./event/completed.md)
  An event that indicates the reader completed the reading process.
- [PaymentCardReaderSession.Event.readCancelled](./event/readcancelled.md)
  An event that indicates the cancellation of the operation.
- [PaymentCardReaderSession.Event.readNotCompleted](./event/readnotcompleted.md)
  An event that indicates the read operation didn’t finish.
- [PaymentCardReaderSession.Event.readyForTap](./event/readyfortap.md)
  An event that indicates the reader is ready for someone to move their card within range of the iPhone.
- [PaymentCardReaderSession.Event.removeCard](./event/removecard.md)
  An event that indicates the consumer can move the card away from the device.
- [PaymentCardReaderSession.Event.retry](./event/retry.md)
  An event that indicates the UI triggered a retry.
### Getting the event name
- [var name: String](./event/name.md)
  The name of the event.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [func readPaymentCard(PaymentCardTransactionRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](./readpaymentcard%28_,eventhandler%29-2zgwn.md)
  Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.
- [func readPaymentCard(PaymentCardVerificationRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](./readpaymentcard%28_,eventhandler%29-20e1w.md)
  Presents a sheet to verify a contactless payment card, and returns the card data.
- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> (PaymentCardReadResult?, VASReadResult?)](./readpaymentcard%28_,vasrequest,stoponvasresult,eventhandler%29.md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.
- [func readVAS(VASRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> VASReadResult](./readvas%28_,eventhandler%29.md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.
- [let id: String](./id.md)
  A unique identifier for this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/event)*