# readPaymentCard(_:)

**Framework**: ProximityReader  
**Kind**: method

Presents a sheet to verify a contactless payment card, and returns the card data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func readPaymentCard(_ request: PaymentCardVerificationRequest) async throws -> PaymentCardReadResult
```

#### Return Value

A [`PaymentCardReadResult`](paymentcardreadresult.md) if the read operation was successful.

#### Discussion

Call this method when you want to verify someone’s card with your payment provider. When you call this method, the system displays UI with instructions on what the person needs to do. This UI remains onscreen until the system reads the person’s card, you cancel the operation, or an error occurs.

> **Note**: This method throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md) if a person dismisses the sheet or the sheet fails to appear.

This method throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md) if a person dismisses the sheet or the sheet fails to appear.

## Parameters

- `request`: The object that contains the reason for the verification request.   For example, you might verify the card supports a specific currency.

## See Also

- [func readPaymentCard(PaymentCardTransactionRequest) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:)-8jol5.md)
  Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readpaymentcard(_:)-hr97)*