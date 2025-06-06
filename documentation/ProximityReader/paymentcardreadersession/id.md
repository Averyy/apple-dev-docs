# id

**Framework**: ProximityReader  
**Kind**: property

A unique identifier for this object.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
final let id: String
```

## See Also

- [func readPaymentCard(PaymentCardTransactionRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:eventhandler:)-2zgwn.md)
  Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.
- [func readPaymentCard(PaymentCardVerificationRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:eventhandler:)-20e1w.md)
  Presents a sheet to verify a contactless payment card, and returns the card data.
- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> (PaymentCardReadResult?, VASReadResult?)](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:eventhandler:).md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.
- [func readVAS(VASRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> VASReadResult](paymentcardreadersession/readvas(_:eventhandler:).md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.
- [PaymentCardReaderSession.Event](paymentcardreadersession/event.md)
  Optional events you can observe during the card-reading process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/id)*