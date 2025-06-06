# capturePIN(using:cardReaderTransactionID:)

**Framework**: Proximityreader  
**Kind**: method

Presents a sheet to capture the PIN when required by the payment card issuer, and returns the previously encrypted card data including newly captured PIN data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func capturePIN(using token: PaymentCardReaderSession.PINToken, cardReaderTransactionID: String) async throws -> PaymentCardReadResult
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Return Value

[`PaymentCardReadResult`](paymentcardreadresult.md) if the PIN was successfully captured.

#### Discussion

Call this method when the payment card issuer requests a PIN for the current transaction. When you call this method, the system displays UI with instructions on what the person needs to do. This UI remains onscreen until the system reads the person’s PIN, you cancel the operation, or an error occurs.

> ❗ **Important**: The encrypted payment card data are only kept 55 seconds after previous read if the PIN was not requested by the card. After this delay, this method will return [`PaymentCardReaderSession.ReadError.pinEntryFailed`](paymentcardreadersession/readerror/pinentryfailed.md)

> **Note**: This method throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md) if a person dismisses the sheet or the sheet fails to appear.

## Parameters

- `token`: Valid and signed PIN token from a participating payment service provider.
- `cardReaderTransactionID`: The   of the previous read.

## See Also

- [PaymentCardReaderSession.PINToken](paymentcardreadersession/pintoken.md)
  A secure PIN token that you receive from your participating payment service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/capturepin(using:cardreadertransactionid:))*