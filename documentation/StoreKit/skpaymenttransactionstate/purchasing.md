# SKPaymentTransactionState.purchasing

**Framework**: StoreKit  
**Kind**: case

A transaction that is being processed by the App Store.

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
case purchasing
```

## Mentions

- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Testing an interrupted purchase](testing-an-interrupted-purchase.md)
- [Processing a transaction](processing-a-transaction.md)

## See Also

- [SKPaymentTransactionState.purchased](skpaymenttransactionstate/purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.failed](skpaymenttransactionstate/failed.md)
  A failed transaction.
- [SKPaymentTransactionState.restored](skpaymenttransactionstate/restored.md)
  A transaction that restores content previously purchased by the user.
- [SKPaymentTransactionState.deferred](skpaymenttransactionstate/deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchasing)*