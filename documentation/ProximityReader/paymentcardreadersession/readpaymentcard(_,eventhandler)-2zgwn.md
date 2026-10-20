# readPaymentCard(_:eventHandler:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.

**Availability**:
- iOS 15.4+ - Deprecated in 16.0
- iPadOS 15.4+ - Deprecated in 16.0
- Mac Catalyst 17.0+ - Deprecated in 17.0

> **Deprecated**: Use PaymentCardReader events instead of eventHandler

## Declaration

```swift
func readPaymentCard(_ request: PaymentCardTransactionRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)? = nil) async throws -> PaymentCardReadResult
```

#### Return Value

A [`PaymentCardReadResult`](../paymentcardreadresult.md) if the read operation was successful.

#### Discussion

Call this method as the first step in a financial transaction involving Tap to Pay with iPhone. This method displays a system-provided sheet with instructions on what the person needs to do. This UI remains onscreen until the system reads the person’s card, you cancel the operation, or an error occurs. After the read operation concludes successfully, deliver the returned card information to your payment service provider.

> **Throws**: This method throws a [`PaymentCardReaderSession.ReadError`](./readerror.md) if a person dismisses the sheet or the sheet fails to appear.

## Parameters

- `request`: The transaction object you provide with the payment amount and currency details.

## See Also

### Deprecated
- [func readPaymentCard(PaymentCardVerificationRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](./readpaymentcard%28_,eventhandler%29-20e1w.md)
  Presents a sheet to verify a contactless payment card, and returns the card data.
- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> (PaymentCardReadResult?, VASReadResult?)](./readpaymentcard%28_,vasrequest,stoponvasresult,eventhandler%29.md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.
- [func readVAS(VASRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> VASReadResult](./readvas%28_,eventhandler%29.md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.
- [let id: String](./id.md)
  A unique identifier for this object.
- [PaymentCardReaderSession.Event](./event.md)
  Optional events you can observe during the card-reading process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readpaymentcard(_:eventhandler:)-2zgwn)*