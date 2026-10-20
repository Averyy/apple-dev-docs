# unfinished

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A sequence that emits unfinished transactions for the customer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var unfinished: Transaction.Transactions { get }
```

## Mentions

- [Supporting offer codes in your app](../supporting-offer-codes-in-your-app.md)
- [Getting started with Apple In-App Purchase using StoreKit views](../getting-started-with-in-app-purchases-using-storekit-views.md)

#### Discussion

A transaction is unfinished until you call [`finish()`](./finish%28%29.md). Use the [`unfinished`](./unfinished.md) sequence to find the transactions your app needs to process to deliver purchased content or enable service.

## See Also

### Getting transaction history
- [static func latest(for: String) async -> VerificationResult<Transaction>?](./latest%28for%29.md)
  Gets the customer’s most recent transaction for an Apple In-App Purchase.
- [static var all: Transaction.Transactions](./all.md)
  A sequence that emits all the customer’s transactions for your app.
- [SKIncludeConsumableInAppPurchaseHistory](../../BundleResources/information-property-list/skincludeconsumableinapppurchasehistory.md)
  A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/unfinished)*