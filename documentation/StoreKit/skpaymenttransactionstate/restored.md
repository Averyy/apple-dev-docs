# SKPaymentTransactionState.restored

**Framework**: StoreKit  
**Kind**: case

A transaction that restores content previously purchased by the user.

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
case restored
```

## Mentions

- [Processing a transaction](processing-a-transaction.md)
- [Restoring purchased products](restoring-purchased-products.md)
- [Supporting Family Sharing in your app](supporting-family-sharing-in-your-app.md)

#### Discussion

Read the [`original`](skpaymenttransaction/original.md) property to obtain information about the original purchase.

## See Also

- [SKPaymentTransactionState.purchasing](skpaymenttransactionstate/purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.purchased](skpaymenttransactionstate/purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.failed](skpaymenttransactionstate/failed.md)
  A failed transaction.
- [SKPaymentTransactionState.deferred](skpaymenttransactionstate/deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/restored)*