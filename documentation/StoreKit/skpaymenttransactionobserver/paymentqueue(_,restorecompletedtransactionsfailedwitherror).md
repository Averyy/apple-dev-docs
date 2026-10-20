# paymentQueue(_:restoreCompletedTransactionsFailedWithError:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells the observer that an error occurred while restoring transactions.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use AppStore.sync().

## Declaration

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: any Error)
```

```objc
- (void) paymentQueue:(SKPaymentQueue *) queue restoreCompletedTransactionsFailedWithError:(NSError *) error;
```

## Mentions

- [Processing a transaction](../processing-a-transaction.md)

## Parameters

- `queue`: The payment queue that was restoring transactions.
- `error`: The error that occurred.

## See Also

### Restoring transactions
- [func paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue)](./paymentqueuerestorecompletedtransactionsfinished%28_%29.md)
  Tells the observer that the payment queue has finished sending restored transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:))*