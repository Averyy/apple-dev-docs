# add(_:)

**Framework**: StoreKit  
**Kind**: method

Adds an observer to the payment queue.

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
func add(_ observer: any SKPaymentTransactionObserver)
```

## Mentions

- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)
- [Testing transaction observer code](testing-transaction-observer-code.md)

#### Discussion

Your application should add an observer to the payment queue during application initialization. If there are no observers attached to the queue, the payment queue does not synchronize its list of pending transactions with the Apple App Store, because there is no observer to respond to updated transactions.

If an application quits when transactions are still being processed, those transactions are not lost. The next time the application launches, the payment queue resumes processing the transactions. Your application should always expect to be notified of completed transactions.

If more than one transaction observer is attached to the payment queue, no guarantees are made as to the order which they will be called. It is safe for multiple observers to call [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md), but not recommended. It is recommended that you use a single observer to process and finish the transaction.

## Parameters

- `observer`: The observer to add to the queue.

## See Also

- [var transactions: [SKPaymentTransaction]](skpaymentqueue/transactions.md)
  Returns an array of pending transactions.
- [var transactionObservers: [any SKPaymentTransactionObserver]](skpaymentqueue/transactionobservers.md)
  An array of all active payment queue observers.
- [func remove(any SKPaymentTransactionObserver)](skpaymentqueue/remove(_:).md)
  Removes an observer from the payment queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/add(_:)-5ciz2)*