# SKPaymentTransactionState.deferred

**Framework**: StoreKit  
**Kind**: case

A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case deferred
```

## Mentions

- [Processing a transaction](processing-a-transaction.md)

#### Discussion

Update your UI to show the deferred state, and wait for another callback that indicates the final status.

## See Also

- [SKPaymentTransactionState.purchasing](skpaymenttransactionstate/purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.purchased](skpaymenttransactionstate/purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.failed](skpaymenttransactionstate/failed.md)
  A failed transaction.
- [SKPaymentTransactionState.restored](skpaymenttransactionstate/restored.md)
  A transaction that restores content previously purchased by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred)*