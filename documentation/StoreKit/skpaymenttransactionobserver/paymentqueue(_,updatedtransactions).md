# paymentQueue(_:updatedTransactions:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells an observer that one or more transactions have been updated.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use StoreKit 2 Transaction APIs.

## Declaration

```swift
func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])
```

```objc
- (void) paymentQueue:(SKPaymentQueue *) queue updatedTransactions:(NSArray<SKPaymentTransaction *> *) transactions;
```

## Mentions

- [Testing Apple In-App Purchases in Xcode](../testing-in-app-purchases-in-xcode.md)
- [Implementing offer codes in your app](../implementing-offer-codes-in-your-app.md)
- [Processing a transaction](../processing-a-transaction.md)
- [Testing a payment request](../testing-a-payment-request.md)
- [Testing a successful transaction](../testing-a-successful-transaction.md)
- [Testing resubscribing from the subscriptions page](../testing-resubscribing-from-the-subscriptions-page.md)

## Discussion

The application should process each transaction by examining the transaction’s [`transactionState`](../skpaymenttransaction/transactionstate.md) property. If [`transactionState`](../skpaymenttransaction/transactionstate.md) is [`SKPaymentTransactionState.purchased`](../skpaymenttransactionstate/purchased.md), payment was successfully received for the desired functionality. The application should make the functionality available to the user. If [`transactionState`](../skpaymenttransaction/transactionstate.md) is [`SKPaymentTransactionState.failed`](../skpaymenttransactionstate/failed.md), the application can read the transaction’s error property to return a meaningful error to the user.

Once a transaction is processed, it should be removed from the payment queue by calling the payment queue’s [`finishTransaction(_:)`](../skpaymentqueue/finishtransaction%28_%29.md) method, passing the transaction as a parameter.

> ❗ **Important**:  Once the transaction is finished, StoreKit can’t tell you that this item is already purchased. It is important that applications process the transaction completely before calling [`finishTransaction(_:)`](../skpaymentqueue/finishtransaction%28_%29.md).

## Parameters

- `queue`: The payment queue that updated the transactions.
- `transactions`: An array of the transactions that were updated.

## See Also

### Related Documentation
- [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
### Handling transactions
- [func paymentQueue(SKPaymentQueue, removedTransactions: [SKPaymentTransaction])](./paymentqueue%28_,removedtransactions%29.md)
  Tells an observer that one or more transactions have been removed from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:))*