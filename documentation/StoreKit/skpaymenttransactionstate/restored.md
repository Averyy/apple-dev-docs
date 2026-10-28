# SKPaymentTransactionState.restored

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A transaction that restores content previously purchased by the user.

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
case restored
```

```c
SKPaymentTransactionStateRestored
```

## Mentions

- [Processing a transaction](../processing-a-transaction.md)
- [Restoring purchased products](../restoring-purchased-products.md)
- [Supporting Family Sharing in your app](../supporting-family-sharing-in-your-app.md)

## Discussion

Read the [`original`](../skpaymenttransaction/original.md) property to obtain information about the original purchase.

## See Also

### Constants
- [SKPaymentTransactionState.purchasing](./purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.purchased](./purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.failed](./failed.md)
  A failed transaction.
- [SKPaymentTransactionState.deferred](./deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/restored)*