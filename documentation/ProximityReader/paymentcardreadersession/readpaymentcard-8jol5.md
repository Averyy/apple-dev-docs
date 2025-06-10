# readPaymentCard(_:)

**Framework**: ProximityReader  
**Kind**: method

Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func readPaymentCard(_ request: PaymentCardTransactionRequest) async throws -> PaymentCardReadResult
```

#### Return Value

A [`PaymentCardReadResult`](paymentcardreadresult.md) if the read operation was successful.

#### Discussion

Call this method as the first step in a financial transaction involving Tap to Pay with iPhone. This method displays a system-provided sheet with instructions on what the person needs to do. This UI remains onscreen until the system reads the person’s card, you cancel the operation, or an error occurs. After the read operation concludes successfully, deliver the returned card information to your payment service provider.

> **Note**: This method throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md) if a person dismisses the sheet or the sheet fails to appear.

## Parameters

- `request`: The transaction object you provide with the payment amount and currency details.

## See Also

- [func readPaymentCard(PaymentCardVerificationRequest) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:)-hr97.md)
  Presents a sheet to verify a contactless payment card, and returns the card data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readpaymentcard(_:)-8jol5)*