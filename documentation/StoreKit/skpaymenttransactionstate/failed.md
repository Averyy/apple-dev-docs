# SKPaymentTransactionState.failed

**Framework**: StoreKit  
**Kind**: case

A failed transaction.

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
case failed
```

## Mentions

- [Testing an interrupted purchase](testing-an-interrupted-purchase.md)
- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)
- [Processing a transaction](processing-a-transaction.md)
- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)

#### Discussion

Check the [`error`](skpaymenttransaction/error.md) property to determine what happened.

## See Also

- [SKPaymentTransactionState.purchasing](skpaymenttransactionstate/purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.purchased](skpaymenttransactionstate/purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.restored](skpaymenttransactionstate/restored.md)
  A transaction that restores content previously purchased by the user.
- [SKPaymentTransactionState.deferred](skpaymenttransactionstate/deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/failed)*