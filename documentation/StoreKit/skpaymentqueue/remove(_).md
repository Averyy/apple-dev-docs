# remove(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Removes an observer from the payment queue.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func remove(_ observer: any SKPaymentTransactionObserver)
```

```objc
- (void) removeTransactionObserver:(id<SKPaymentTransactionObserver>) observer;
```

#### Discussion

If there are no observers attached to the queue, the payment queue does not synchronize its list of pending transactions with the Apple App Store, because there is no observer to respond to updated transactions.

## Parameters

- `observer`: The observer to remove.

## See Also

### Related Documentation
- [var transactions: [SKPaymentTransaction]](./transactions.md)
  Returns an array of pending transactions.
### Adding, Getting, and Removing Observers
- [func add(any SKPaymentTransactionObserver)](./add%28_%29-5ciz2.md)
  Adds an observer to the payment queue.
- [var transactionObservers: [any SKPaymentTransactionObserver]](./transactionobservers.md)
  An array of all active payment queue observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/remove(_:))*