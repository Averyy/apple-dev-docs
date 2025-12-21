# Product.PurchaseResult.pending

**Framework**: StoreKit  
**Kind**: case

The purchase is pending, and requires action from the customer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case pending
```

## Mentions

- [Testing Ask to Buy in Xcode](testing-ask-to-buy-in-xcode.md)

#### Discussion

If a pending purchase succeeds, StoreKit delivers the resulting [`Transaction`](transaction.md) in the transaction [`updates`](transaction/updates.md).

## See Also

- [case success(VerificationResult<Transaction>)](product/purchaseresult/success(_:).md)
  The purchase succeeded and results in a transaction.
- [Product.PurchaseResult.userCancelled](product/purchaseresult/usercancelled.md)
  The user canceled the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseresult/pending)*