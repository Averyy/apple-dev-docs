# readPaymentCard(_:eventHandler:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

Presents a sheet to verify a contactless payment card, and returns the card data.

**Availability**:
- iOS 15.4+ - Deprecated in 16.0
- iPadOS 15.4+ - Deprecated in 16.0
- Mac Catalyst 17.0+ - Deprecated in 17.0

> **Deprecated**: Use PaymentCardReader events instead of eventHandler

## Declaration

```swift
func readPaymentCard(_ request: PaymentCardVerificationRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)? = nil) async throws -> PaymentCardReadResult
```

## Return Value

A [`PaymentCardReadResult`](../paymentcardreadresult.md) if the read operation was successful.

## Discussion

Call this method when you want to verify someone’s card with your payment provider. When you call this method, the system displays UI with instructions on what the person needs to do. This UI remains onscreen until the system reads the person’s card, you cancel the operation, or an error occurs.

> **Throws**: This method throws a [`PaymentCardReaderSession.ReadError`](./readerror.md) if a person dismisses the sheet or the sheet fails to appear.

## Parameters

- `request`: The object that contains the reason for the verification request. For example, you might verify the card supports a specific currency.
- `eventHandler`: A handler you use to receive request-related updates while the system has control of the screen. The handler has no return value and takes a [`PaymentCardReaderSession.Event`](./event.md) as a parameter. Use the event parameter to determine what happened.

## See Also

### Deprecated
- [func readPaymentCard(PaymentCardTransactionRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](./readpaymentcard%28_,eventhandler%29-2zgwn.md)
  Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.
- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> (PaymentCardReadResult?, VASReadResult?)](./readpaymentcard%28_,vasrequest,stoponvasresult,eventhandler%29.md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.
- [func readVAS(VASRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> VASReadResult](./readvas%28_,eventhandler%29.md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.
- [let id: String](./id.md)
  A unique identifier for this object.
- [PaymentCardReaderSession.Event](./event.md)
  Optional events you can observe during the card-reading process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readpaymentcard(_:eventhandler:)-20e1w)*