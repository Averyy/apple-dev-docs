# Transaction.RefundRequestError.duplicateRequest

**Framework**: StoreKit  
**Kind**: case

The App Store has already received a refund request for this in-app purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case duplicateRequest
```

#### Discussion

StoreKit returns this error if the App Store has previously received a refund request for this transaction and the refund decision is still pending, has been previously denied, or has been previously approved.

Consider checking the transaction’s [`revocationDate`](transaction/revocationdate.md) or [`revocationReason`](transaction/revocationreason-swift.property.md) before calling [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-65tph.md) to identify whether the App Store has already refunded the transaction.

## See Also

- [Transaction.RefundRequestError.failed](transaction/refundrequesterror/failed.md)
  The refund request submission failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/refundrequesterror/duplicaterequest)*