# paymentQueueRestoreCompletedTransactionsFinished(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells the observer that the payment queue has finished sending restored transactions.

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
optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue)
```

```objc
- (void) paymentQueueRestoreCompletedTransactionsFinished:(SKPaymentQueue *) queue;
```

## Mentions

- [Processing a transaction](../processing-a-transaction.md)
- [Testing Apple In-App Purchases in Xcode](../testing-in-app-purchases-in-xcode.md)

#### Discussion

This method is called after all restorable transactions have been processed by the payment queue. Your application is not required to do anything in this method.

## Parameters

- `queue`: The payment queue that restored the transactions.

## See Also

### Restoring transactions
- [func paymentQueue(SKPaymentQueue, restoreCompletedTransactionsFailedWithError: any Error)](./paymentqueue%28_,restorecompletedtransactionsfailedwitherror%29.md)
  Tells the observer that an error occurred while restoring transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:))*