# PaymentCardReaderSession.Event

**Framework**: ProximityReader  
**Kind**: enum

Optional events you can observe during the card-reading process.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum Event
```

#### Overview

If you supply an event handler when reading a card, the session delivers appropriate events to your handler. Use them to update your UI or perform other app-specific tasks. You can also use them to provide accessibility-related feedback.

## Topics

### Getting the event type
- [PaymentCardReaderSession.Event.cardDetected](paymentcardreadersession/event/carddetected.md)
  An event that indicates the reader detected the presence of a card.
- [PaymentCardReaderSession.Event.completed](paymentcardreadersession/event/completed.md)
  An event that indicates the reader completed the reading process.
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
### Getting the event name
- [var name: String](paymentcardreadersession/event/name.md)
  The name of the event.
### Operators
- [static func == (PaymentCardReaderSession.Event, PaymentCardReaderSession.Event) -> Bool](paymentcardreadersession/event/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](paymentcardreadersession/event/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](paymentcardreadersession/event/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](paymentcardreadersession/event/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func readPaymentCard(PaymentCardTransactionRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:eventhandler:)-2zgwn.md)
  Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.
- [func readPaymentCard(PaymentCardVerificationRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:eventhandler:)-20e1w.md)
  Presents a sheet to verify a contactless payment card, and returns the card data.
- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> (PaymentCardReadResult?, VASReadResult?)](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:eventhandler:).md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.
- [func readVAS(VASRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> VASReadResult](paymentcardreadersession/readvas(_:eventhandler:).md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.
- [let id: String](paymentcardreadersession/id.md)
  A unique identifier for this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/event)*