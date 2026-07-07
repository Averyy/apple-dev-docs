# all

**Framework**: StoreKit  
**Kind**: property

A sequence that emits all the customer’s transactions for your app.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var all: Transaction.Transactions { get }
```

## Mentions

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)

#### Discussion

This sequence returns the customer’s transaction history current to the moment you access it. The sequence emits a finite number of transactions. If the App Store processes additional transactions for the customer while you’re accessing this sequence, they appear in the transaction listener [`updates`](transaction/updates.md).

The transaction history includes the following in-app purchases:

- Unfinished consumables
- Finished consumables that are refunded or revoked
- Non-consumables
- Auto-renewable subscriptions, including all renewals
- Auto-renewable subscriptions and non-consumables that the customer gets through Family Sharing

By default, when the [`SKIncludeConsumableInAppPurchaseHistory`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory) property list key is `false`, the transaction information excludes finished consumables (unless refunded or revoked).

To get all possible transactions, including all finished consumables, set the [`SKIncludeConsumableInAppPurchaseHistory`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory) property list key to `true`.

## See Also

- [struct Transaction](transaction.md)
  Information that represents the customer’s purchase of a product in your app.
- [static var updates: Transaction.Transactions](transaction/updates.md)
  The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [static var currentEntitlements: Transaction.Transactions](transaction/currententitlements.md)
  A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/all)*