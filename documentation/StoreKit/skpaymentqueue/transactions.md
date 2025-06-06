# transactions

**Framework**: StoreKit  
**Kind**: property

Returns an array of pending transactions.

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
var transactions: [SKPaymentTransaction] { get }
```

#### Discussion

The value of this property is undefined when there are no observers attached to the payment queue.

## See Also

- [func add(any SKPaymentTransactionObserver)](skpaymentqueue/add(_:)-5ciz2.md)
  Adds an observer to the payment queue.
- [var delegate: (any SKPaymentQueueDelegate)?](skpaymentqueue/delegate.md)
  A delegate that provides information needed to complete transactions.
- [func add(SKPayment)](skpaymentqueue/add(_:)-4vct1.md)
  Adds a payment request to the queue.
- [func finishTransaction(SKPaymentTransaction)](skpaymentqueue/finishtransaction(_:).md)
  Notifies the App Store that the app finished processing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/transactions)*