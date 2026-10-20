# SKPaymentTransactionState.purchased

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A successfully processed transaction.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use PurchaseResult from Product.purchase(confirmIn:options:).

## Declaration

```swift
case purchased
```

```c
SKPaymentTransactionStatePurchased
```

## Mentions

- [Testing Apple In-App Purchases in Xcode](../testing-in-app-purchases-in-xcode.md)
- [Implementing offer codes in your app](../implementing-offer-codes-in-your-app.md)
- [Implementing promotional offers in your app](../implementing-promotional-offers-in-your-app.md)
- [Processing a transaction](../processing-a-transaction.md)
- [Supporting Family Sharing in your app](../supporting-family-sharing-in-your-app.md)
- [Testing a successful transaction](../testing-a-successful-transaction.md)
- [Testing an interrupted purchase](../testing-an-interrupted-purchase.md)
- [Testing resubscribing from the subscriptions page](../testing-resubscribing-from-the-subscriptions-page.md)

#### Discussion

Your application should provide the content the user purchased.

## See Also

### Constants
- [SKPaymentTransactionState.purchasing](./purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.failed](./failed.md)
  A failed transaction.
- [SKPaymentTransactionState.restored](./restored.md)
  A transaction that restores content previously purchased by the user.
- [SKPaymentTransactionState.deferred](./deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchased)*