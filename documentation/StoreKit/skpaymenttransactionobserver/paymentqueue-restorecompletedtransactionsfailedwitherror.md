# paymentQueue(_:restoreCompletedTransactionsFailedWithError:)

**Framework**: StoreKit  
**Kind**: method

Tells the observer that an error occurred while restoring transactions.

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
optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: any Error)
```

## Mentions

- [Processing a transaction](processing-a-transaction.md)

## Parameters

- `queue`: The payment queue that was restoring transactions.
- `error`: The error that occurred.

## See Also

- [func paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue)](skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:).md)
  Tells the observer that the payment queue has finished sending restored transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:))*