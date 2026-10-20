# id

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

A unique identifier for this object.

**Availability**:
- iOS 15.4+ - Deprecated in 16.0
- iPadOS 15.4+ - Deprecated in 16.0
- Mac Catalyst 17.0+ - Deprecated in 17.0

> **Deprecated**: Use ObjectIdentifier instead

## Declaration

```swift
final let id: String
```

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
- [PaymentCardReaderSession.Event](./event.md)
  Optional events you can observe during the card-reading process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/id)*