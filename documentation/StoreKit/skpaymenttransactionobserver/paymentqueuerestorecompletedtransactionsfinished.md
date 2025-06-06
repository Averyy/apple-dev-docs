# paymentQueueRestoreCompletedTransactionsFinished(_:)

**Framework**: StoreKit  
**Kind**: method

Tells the observer that the payment queue has finished sending restored transactions.

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
optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue)
```

## Mentions

- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Processing a transaction](processing-a-transaction.md)

#### Discussion

This method is called after all restorable transactions have been processed by the payment queue. Your application is not required to do anything in this method.

## Parameters

- `queue`: The payment queue that restored the transactions.

## See Also

- [func paymentQueue(SKPaymentQueue, restoreCompletedTransactionsFailedWithError: any Error)](skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:).md)
  Tells the observer that an error occurred while restoring transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:))*