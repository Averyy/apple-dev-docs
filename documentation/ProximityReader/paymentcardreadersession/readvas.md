# readVAS(_:)

**Framework**: ProximityReader  
**Kind**: method

Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func readVAS(_ request: VASRequest) async throws -> VASReadResult
```

## Mentions

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)

#### Return Value

A [`VASReadResult`](vasreadresult.md) if the read operation was successful.

#### Discussion

Call this method to read the data from a loyalty card. When you call this method, the system displays UI with instructions on what the person needs to do. This UI remains onscreen until the system reads the person’s card, you cancel the operation, or an error occurs.

> **Note**: This method throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md) if a person dismisses the sheet or the sheet fails to appear.

This method throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md) if a person dismisses the sheet or the sheet fails to appear.

## Parameters

- `request`: The object that you use to specify the request details, such   as the list of supported merchants.

## See Also

- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool) async throws -> (PaymentCardReadResult?, VASReadResult?)](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:).md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readvas(_:))*