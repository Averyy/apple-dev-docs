# unfinished

**Framework**: StoreKit  
**Kind**: property

A sequence that emits unfinished transactions for the customer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var unfinished: Transaction.Transactions { get }
```

#### Discussion

A transaction is unfinished until you call [`finish()`](transaction/finish().md). Use the [`unfinished`](transaction/unfinished.md) sequence to find the transactions your app needs to process to deliver purchased content or enable service.

## See Also

- [static func latest(for: String) async -> VerificationResult<Transaction>?](transaction/latest(for:).md)
  Gets the customer’s most recent transaction for an In-App Purchase.
- [static var all: Transaction.Transactions](transaction/all.md)
  A sequence that emits all the customer’s transactions for your app.
- [SKIncludeConsumableInAppPurchaseHistory](../BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/unfinished)*