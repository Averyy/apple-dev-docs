# delegate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A delegate that provides information needed to complete transactions.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- tvOS 13.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: No longer supported.

## Declaration

```swift
weak var delegate: (any SKPaymentQueueDelegate)? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, weak, nullable) id<SKPaymentQueueDelegate> delegate;
```

*macOS*

```objc
@property (atomic, weak, nullable) id<SKPaymentQueueDelegate> delegate;
```

#### Discussion

This delegate implements the [`SKPaymentQueueDelegate`](../skpaymentqueuedelegate.md) protocol.

## See Also

### Managing Transactions
- [var transactions: [SKPaymentTransaction]](./transactions.md)
  Returns an array of pending transactions.
- [func add(SKPayment)](./add%28_%29-4vct1.md)
  Adds a payment request to the queue.
- [func finishTransaction(SKPaymentTransaction)](./finishtransaction%28_%29.md)
  Notifies the App Store that the app finished processing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/delegate)*