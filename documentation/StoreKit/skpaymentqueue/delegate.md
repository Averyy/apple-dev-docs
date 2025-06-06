# delegate

**Framework**: StoreKit  
**Kind**: property

A delegate that provides information needed to complete transactions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
weak var delegate: (any SKPaymentQueueDelegate)? { get set }
```

#### Discussion

This delegate implements the [`SKPaymentQueueDelegate`](skpaymentqueuedelegate.md) protocol.

## See Also

- [var transactions: [SKPaymentTransaction]](skpaymentqueue/transactions.md)
  Returns an array of pending transactions.
- [func add(SKPayment)](skpaymentqueue/add(_:)-4vct1.md)
  Adds a payment request to the queue.
- [func finishTransaction(SKPaymentTransaction)](skpaymentqueue/finishtransaction(_:).md)
  Notifies the App Store that the app finished processing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/delegate)*