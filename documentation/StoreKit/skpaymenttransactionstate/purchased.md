# SKPaymentTransactionState.purchased

**Framework**: StoreKit  
**Kind**: case

A successfully processed transaction.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case purchased
```

## Mentions

- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Processing a transaction](processing-a-transaction.md)
- [Supporting Family Sharing in your app](supporting-family-sharing-in-your-app.md)
- [Testing an interrupted purchase](testing-an-interrupted-purchase.md)
- [Testing resubscribing from the subscriptions page](testing-resubscribing-from-the-subscriptions-page.md)
- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)
- [Implementing offer codes in your app](implementing-offer-codes-in-your-app.md)
- [Testing a successful transaction](testing-a-successful-transaction.md)

#### Discussion

Your application should provide the content the user purchased.

## See Also

- [SKPaymentTransactionState.purchasing](skpaymenttransactionstate/purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.failed](skpaymenttransactionstate/failed.md)
  A failed transaction.
- [SKPaymentTransactionState.restored](skpaymenttransactionstate/restored.md)
  A transaction that restores content previously purchased by the user.
- [SKPaymentTransactionState.deferred](skpaymenttransactionstate/deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchased)*