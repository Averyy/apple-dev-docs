# finishTransaction(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Notifies the App Store that the app finished processing the transaction.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Transaction.finish().

## Declaration

```swift
func finishTransaction(_ transaction: SKPaymentTransaction)
```

```objc
- (void) finishTransaction:(SKPaymentTransaction *) transaction;
```

## Mentions

- [Testing Apple In-App Purchases in Xcode](../testing-in-app-purchases-in-xcode.md)
- [Finishing a transaction](../finishing-a-transaction.md)
- [Implementing offer codes in your app](../implementing-offer-codes-in-your-app.md)
- [Testing an interrupted purchase](../testing-an-interrupted-purchase.md)
- [Testing complete transactions](../testing-complete-transactions.md)
- [Choosing a receipt validation technique](../choosing-a-receipt-validation-technique.md)
- [Supporting Family Sharing in your app](../supporting-family-sharing-in-your-app.md)
- [Testing at all stages of development with Xcode and the sandbox](../testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md)
- [Testing resubscribing from the subscriptions page](../testing-resubscribing-from-the-subscriptions-page.md)

#### Discussion

Transactions on the payment queue are persistent until they are completed. StoreKit calls your observer’s [`paymentQueue(_:updatedTransactions:)`](../skpaymenttransactionobserver/paymentqueue%28_,updatedtransactions%29.md) method every time your app launches or resumes from background to tell you about transactions in the queue. After you’ve finished processing a transaction in your app, always call the [`finishTransaction(_:)`](./finishtransaction%28_%29.md) method to finish the transaction and remove it from the queue.

Call [`finishTransaction(_:)`](./finishtransaction%28_%29.md) only after the app has finished all work it performs to complete the transaction. The transaction’s state determines which steps you might take:

- For a failed transaction ([`SKPaymentTransactionState.failed`](../skpaymenttransactionstate/failed.md)), update your user interface, track information in analytics, and perform other similar tasks.
- For a successful transaction ([`SKPaymentTransactionState.purchased`](../skpaymenttransactionstate/purchased.md) or [`SKPaymentTransactionState.restored`](../skpaymenttransactionstate/restored.md)), perform all necessary actions to unlock the functionality the user has purchased before finishing the transaction. For example, if you are downloading content, finish the transaction only after the downloads are complete.

If you validate receipts, validate them before completing the transaction, and take one of the paths described above.

In rare circumstances, this call might fail, and you’ll receive updates for that transaction again. For this reason, you should record information in your app about the transactions it has processed and which steps the app has already completed. That way, you don’t repeat steps that shouldn’t be performed multiple times. For example, if you are processing a consumable transaction, you only want to add the consumable benefit once.

If you call [`finishTransaction(_:)`](./finishtransaction%28_%29.md) on a transaction that is in the [`SKPaymentTransactionState.purchasing`](../skpaymenttransactionstate/purchasing.md) state, StoreKit raises an exception.

## Parameters

- `transaction`: The transaction to finish.

## See Also

### Related Documentation
- [func paymentQueue(SKPaymentQueue, updatedTransactions: [SKPaymentTransaction])](../skpaymenttransactionobserver/paymentqueue%28_,updatedtransactions%29.md)
  Tells an observer that one or more transactions have been updated.
### Managing Transactions
- [var delegate: (any SKPaymentQueueDelegate)?](./delegate.md)
  A delegate that provides information needed to complete transactions.
- [var transactions: [SKPaymentTransaction]](./transactions.md)
  Returns an array of pending transactions.
- [func add(SKPayment)](./add%28_%29-4vct1.md)
  Adds a payment request to the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/finishtransaction(_:))*