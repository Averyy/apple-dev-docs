# transactionObservers

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An array of all active payment queue observers.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use Transaction.updates or PurchaseResult from Product.purchase(confirmIn:options:).

## Declaration

```swift
var transactionObservers: [any SKPaymentTransactionObserver] { get }
```

```objc
@property (nonatomic, readonly) NSArray<id<SKPaymentTransactionObserver>> * transactionObservers;
```

## See Also

### Adding, Getting, and Removing Observers
- [func add(any SKPaymentTransactionObserver)](./add%28_%29-5ciz2.md)
  Adds an observer to the payment queue.
- [func remove(any SKPaymentTransactionObserver)](./remove%28_%29.md)
  Removes an observer from the payment queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/transactionobservers)*