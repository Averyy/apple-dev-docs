# transactionObservers

**Framework**: StoreKit  
**Kind**: property

An array of all active payment queue observers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var transactionObservers: [any SKPaymentTransactionObserver] { get }
```

## See Also

- [func add(any SKPaymentTransactionObserver)](skpaymentqueue/add(_:)-5ciz2.md)
  Adds an observer to the payment queue.
- [func remove(any SKPaymentTransactionObserver)](skpaymentqueue/remove(_:).md)
  Removes an observer from the payment queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/transactionobservers)*