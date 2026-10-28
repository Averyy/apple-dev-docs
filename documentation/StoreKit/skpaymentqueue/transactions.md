# transactions

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

Returns an array of pending transactions.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Transaction.unfinished.

## Declaration

```swift
var transactions: [SKPaymentTransaction] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SKPaymentTransaction *> * transactions;
```

## Discussion

The value of this property is undefined when there are no observers attached to the payment queue.

## See Also

### Related Documentation
- [func add(any SKPaymentTransactionObserver)](./add%28_%29-5ciz2.md)
  Adds an observer to the payment queue.
### Managing Transactions
- [var delegate: (any SKPaymentQueueDelegate)?](./delegate.md)
  A delegate that provides information needed to complete transactions.
- [func add(SKPayment)](./add%28_%29-4vct1.md)
  Adds a payment request to the queue.
- [func finishTransaction(SKPaymentTransaction)](./finishtransaction%28_%29.md)
  Notifies the App Store that the app finished processing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/transactions)*