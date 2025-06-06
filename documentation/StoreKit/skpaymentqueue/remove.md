# remove(_:)

**Framework**: StoreKit  
**Kind**: method

Removes an observer from the payment queue.

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
func remove(_ observer: any SKPaymentTransactionObserver)
```

#### Discussion

If there are no observers attached to the queue, the payment queue does not synchronize its list of pending transactions with the Apple App Store, because there is no observer to respond to updated transactions.

## Parameters

- `observer`: The observer to remove.

## See Also

- [var transactions: [SKPaymentTransaction]](skpaymentqueue/transactions.md)
  Returns an array of pending transactions.
- [func add(any SKPaymentTransactionObserver)](skpaymentqueue/add(_:)-5ciz2.md)
  Adds an observer to the payment queue.
- [var transactionObservers: [any SKPaymentTransactionObserver]](skpaymentqueue/transactionobservers.md)
  An array of all active payment queue observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/remove(_:))*