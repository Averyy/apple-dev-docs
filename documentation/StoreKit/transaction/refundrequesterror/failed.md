# Transaction.RefundRequestError.failed

**Framework**: StoreKit  
**Kind**: case

The refund request submission failed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case failed
```

#### Discussion

A refund request submission can fail for many reasons, such as having an invalid transaction identifier, or if the App Store can’t process the request for some other reason.

## See Also

- [Transaction.RefundRequestError.duplicateRequest](transaction/refundrequesterror/duplicaterequest.md)
  The App Store has already received a refund request for this in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/refundrequesterror/failed)*