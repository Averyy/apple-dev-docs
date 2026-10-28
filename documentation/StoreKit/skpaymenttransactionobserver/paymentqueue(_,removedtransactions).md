# paymentQueue(_:removedTransactions:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells an observer that one or more transactions have been removed from the queue.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use StoreKit 2 Transaction APIs.

## Declaration

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, removedTransactions transactions: [SKPaymentTransaction])
```

```objc
- (void) paymentQueue:(SKPaymentQueue *) queue removedTransactions:(NSArray<SKPaymentTransaction *> *) transactions;
```

## Mentions

- [Processing a transaction](../processing-a-transaction.md)

## Discussion

Your application does not typically need to implement this method but might implement it to update its own user interface to reflect that a transaction has been completed.

## Parameters

- `queue`: The payment queue that updated the transactions.
- `transactions`: An array of the transactions that were removed.

## See Also

### Handling transactions
- [func paymentQueue(SKPaymentQueue, updatedTransactions: [SKPaymentTransaction])](./paymentqueue%28_,updatedtransactions%29.md)
  Tells an observer that one or more transactions have been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:removedtransactions:))*