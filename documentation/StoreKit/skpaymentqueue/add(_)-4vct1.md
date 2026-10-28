# add(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Adds a payment request to the queue.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.purchase(confirmIn:options:).

## Declaration

```swift
func add(_ payment: SKPayment)
```

```objc
- (void) addPayment:(SKPayment *) payment;
```

## Discussion

An application should always have at least one observer of the payment queue before adding payment requests.

The payment request must have a product identifier registered with the Apple App Store and a quantity greater than `0`. If either property is invalid, [`add(_:)`](./add%28_%29-4vct1.md) throws an exception.

When a payment request is added to the queue, the payment queue processes that request with the Apple App Store and arranges for payment from the user. When that transaction is complete or if a failure occurs, the payment queue sends the [`SKPaymentTransaction`](../skpaymenttransaction.md) object that encapsulates the request to all transaction observers.

## Parameters

- `payment`: A payment request.

## See Also

### Managing Transactions
- [var delegate: (any SKPaymentQueueDelegate)?](./delegate.md)
  A delegate that provides information needed to complete transactions.
- [var transactions: [SKPaymentTransaction]](./transactions.md)
  Returns an array of pending transactions.
- [func finishTransaction(SKPaymentTransaction)](./finishtransaction%28_%29.md)
  Notifies the App Store that the app finished processing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/add(_:)-4vct1)*