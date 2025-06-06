# paymentQueue(_:removedTransactions:)

**Framework**: StoreKit  
**Kind**: method

Tells an observer that one or more transactions have been removed from the queue.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, removedTransactions transactions: [SKPaymentTransaction])
```

## Mentions

- [Processing a transaction](processing-a-transaction.md)

#### Discussion

Your application does not typically need to implement this method but might implement it to update its own user interface to reflect that a transaction has been completed.

## Parameters

- `queue`: The payment queue that updated the transactions.
- `transactions`: An array of the transactions that were removed.

## See Also

- [func paymentQueue(SKPaymentQueue, updatedTransactions: [SKPaymentTransaction])](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md)
  Tells an observer that one or more transactions have been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:removedtransactions:))*