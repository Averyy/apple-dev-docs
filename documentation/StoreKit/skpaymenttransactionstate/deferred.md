# SKPaymentTransactionState.deferred

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.10+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use PurchaseResult.pending from Product.purchase(confirmIn:options:).

## Declaration

```swift
case deferred
```

```c
SKPaymentTransactionStateDeferred
```

## Mentions

- [Processing a transaction](../processing-a-transaction.md)

#### Discussion

Update your UI to show the deferred state, and wait for another callback that indicates the final status.

## See Also

### Constants
- [SKPaymentTransactionState.purchasing](./purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.purchased](./purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.failed](./failed.md)
  A failed transaction.
- [SKPaymentTransactionState.restored](./restored.md)
  A transaction that restores content previously purchased by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred)*