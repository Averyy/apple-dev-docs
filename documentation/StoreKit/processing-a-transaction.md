# Processing a transaction

**Framework**: StoreKit

Register a transaction queue observer to get and handle transaction updates from the App Store.

#### Overview

Implementing an in-app purchase flow consists of three stages. In the first stage, your app retrieves product information. Then your app requests payment when the user selects a product in your app’s store. Finally, your app delivers the product.

The App Store calls the transaction queue observer after it processes the payment request. Your app then records information about the purchase for future launches, downloads the purchased content, and marks the transaction as finished.

![A flowchart depicting the three stages of the in-app purchase process between your app and the App Store. First, your app makes a request for a product, the App Store provides that product information, and your app displays it. Next, the user selects a product, your app makes a payment request, and the App Store processes the payment. Finally, the App Store calls your app’s transaction queue observer, and your app delivers the purchased product. The third stage, delivering products, is highlighted.](https://docs-assets.developer.apple.com/published/5b88efb67bd1deaf5cc7b0e2c373d310/media-3314631%402x.png)

##### Monitor Transactions in the Queue

The transaction queue plays a central role in letting your app communicate with the App Store through the StoreKit framework. You add work to the queue that the App Store needs to act on, such as a payment request for processing. When the transaction’s state changes, such as when a payment request succeeds, StoreKit calls the app’s transaction queue observer. You decide which class acts as the observer. In very small apps, you might handle all the StoreKit logic in the app delegate, including observing the transaction queue. In most apps, however, you create a separate class that handles this observer logic, along with the rest of your app’s store logic. The observer needs to conform to the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol.

By adding an observer, your app doesn’t need to constantly poll the status of its active transactions. Your app uses the transaction queue for payment requests, to download Apple-hosted content, and to determine when subscriptions renew.

It’s important to register a transaction queue observer as soon as your app launches, as the code shows below. For more guidance, see [`Setting up the transaction observer for the payment queue`](setting-up-the-transaction-observer-for-the-payment-queue.md).

Make sure that the observer is ready to handle a transaction at any time, not only after you add a transaction to the queue. For example, if a user buys something in your app just before entering a tunnel, your app may not be able to deliver the purchased content if there isn’t a network connection. The next time your app launches, StoreKit calls your transaction queue observer again so your app can handle the transaction and deliver the purchased content. Similarly, if your app fails to mark a transaction as finished, StoreKit calls the observer every time your app launches until the transaction finishes.

Implement the [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) method on your transaction queue observer. StoreKit calls this method when the status of a transaction changes, such as when a payment request has been processed. The transaction status tells you what action your app needs to perform, as described in the table below:

| Status | Action to take in your app |
| --- | --- |
| [`SKPaymentTransactionState.purchasing`](skpaymenttransactionstate/purchasing.md) | Update your UI to reflect the in-progress status, and wait for StoreKit to call the method again. |
| [`SKPaymentTransactionState.deferred`](skpaymenttransactionstate/deferred.md) | Update your UI to reflect the deferred status, and wait for StoreKit to call the method again. |
| [`SKPaymentTransactionState.failed`](skpaymenttransactionstate/failed.md) | Use the value of the `error` property to present a message to the user. For a list of error constants, see [`SKErrorDomain`](skerrordomain.md). |
| [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) | Provide the purchased functionality, typically by unlocking features or delivering content. |
| [`SKPaymentTransactionState.restored`](skpaymenttransactionstate/restored.md) | Restore the previously purchased functionality. |

Transactions in the queue can change state in any order. Your app needs to be ready to work on any active transaction at any time. Act on every transaction according to its transaction state, as in this example:

##### Update the Apps Ui to Reflect Transaction Changes

To keep your user interface up to date while waiting, the transaction queue observer can implement optional methods from the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol as follows:

- StoreKit calls the [`paymentQueue(_:removedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:removedtransactions:).md) method when it removes transactions from the queue. In your implementation of this method, remove the corresponding items from your app’s UI.
- StoreKit calls the [`paymentQueueRestoreCompletedTransactionsFinished(_:)`](skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:).md) or [`paymentQueue(_:restoreCompletedTransactionsFailedWithError:)`](skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:).md) methods when it finishes restoring transactions, depending on whether there is an error. In your implementation of these methods, update your app’s UI to reflect the success or failure.

For successfully processed transactions, validate the receipt associated with the transaction to verify the items the user purchased, and unlock content accordingly. For more information on validating receipts serverside, see [`Validating receipts with the App Store`](validating-receipts-with-the-app-store.md).

## See Also

- [Requesting a payment from the App Store](requesting-a-payment-from-the-app-store.md)
  Submit a payment request to the App Store when a customer selects a product to buy.
- [class SKPayment](skpayment.md)
  A request to the App Store to process payment for additional functionality that your app offers.
- [class SKMutablePayment](skmutablepayment.md)
  A mutable request to the App Store to process payment for additional functionality that your app offers.
- [class SKPaymentTransaction](skpaymenttransaction.md)
  An object in the payment queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/processing-a-transaction)*