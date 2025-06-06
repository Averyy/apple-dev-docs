# Restoring purchased products

**Framework**: Storekit

Give customers functionality that restores their purchases in your app to maintain access to purchased content.

#### Overview

Customers sometimes need to restore purchased content, such as when they upgrade to a new phone. Include some mechanism in your app, such as a Restore Purchases button, to let them restore their purchases.

> ❗ **Important**:  Don’t automatically restore purchases, especially when your app launches. Restoring purchases prompts for the user’s App Store credentials, which interrupts the flow of your app.

In most cases, you only need to refresh the app receipt and deliver the products on the receipt. The refreshed receipt contains a record of the user’s purchases in the app, from any device the user’s App Store account is logged into. However, an app might require an alternative approach under the given circumstances:

- You use Apple-hosted content — Restore completed transactions to give your app the transaction objects it uses to download the content.
- You need to support your app on devices where the app receipt isn’t available — Restore completed transactions instead.
- Your app uses non-renewing subscriptions — Your app is responsible for the restoration process.

Refreshing a receipt doesn’t create new transactions; it requests the latest copy of the receipt from the App Store. Refresh the receipt only once; refreshing it multiple times in a row has the same result.

Restoring completed transactions creates a new transaction for each previously completed transaction, essentially replaying history for your transaction queue observer. Your app maintains its own state to keep track of why it’s restoring completed transactions and how to handle them. Restoring multiple times creates multiple restored transactions for each completed transaction.

> **Note**:  If the user attempts to purchase a product that they’ve already purchased, the App Store creates a regular transaction instead of a restore transaction, but the user isn’t charged again for the product. Unlock the content for these transactions the same way you do for original transactions.

Give the user an appropriate level of control over the content that’s downloaded again. For example, don’t automatically download three years of daily newspapers or hundreds of megabytes of game levels at the same time.

##### Refresh the App Receipt

Create a receipt refresh request, set a delegate, and start the request. The request supports optional properties for obtaining receipts in various states, such as expired receipts, during testing. For details, see the [`init(receiptProperties:)`](skreceiptrefreshrequest/init(receiptproperties:).md) method of [`SKReceiptRefreshRequest`](skreceiptrefreshrequest.md).

After the app receipt refreshes, examine it and deliver any additional products, as necessary.

##### Restore Completed Transactions

Your app starts restoring completed transactions by calling the [`restoreCompletedTransactions()`](skpaymentqueue/restorecompletedtransactions().md) method of [`SKPaymentQueue`](skpaymentqueue.md). This call sends a request to the App Store to restore all of your app’s completed transactions. If your app sets a value for the [`applicationUsername`](skmutablepayment/applicationusername.md) property of its payment requests, use the [`restoreCompletedTransactions(withApplicationUsername:)`](skpaymentqueue/restorecompletedtransactions(withapplicationusername:).md) method to provide the same information when restoring the transactions.

The App Store generates a new transaction to restore each previously completed transaction. The restored transaction refers to the original transaction. Instances of [`SKPaymentTransaction`](skpaymenttransaction.md) have an [`original`](skpaymenttransaction/original.md) property, and the entries in the receipt have an [`original_transaction_id`](https://developer.apple.com/documentation/appstorereceipts/original_transaction_id) field value.

> **Note**:  The date fields have slightly different meanings for restored purchases. For details, see the `purchase_date` and `original_purchase_date` fields in the [`responseBody.Receipt.In_app`](https://developer.apple.com/documentation/appstorereceipts/responsebody/receipt/in_app).

StoreKit calls the transaction queue observer with a status of [`SKPaymentTransactionState.restored`](skpaymenttransactionstate/restored.md) for each restored transaction, as described in [`Processing a transaction`](processing-a-transaction.md). The action you take depends on your app’s design.

If your app uses the app receipt and doesn’t have Apple-hosted content, this code isn’t needed because your app doesn’t restore completed transactions. Finish any restored transactions immediately.

If your app uses the app receipt and has Apple-hosted content, let the user select which products to restore before starting the restoration process. During restoration, download the user-selected content before finishing those transactions, and finish any other transactions immediately.

If your app doesn’t use the app receipt, it examines all completed transactions as it restores them. It uses a similar code path to the original purchase logic to make the product available and then finishes the transaction. Apps with more than a few products, especially products with associated content, let the user select which products to restore instead of restoring everything. These apps keep track of which completed transactions to process as they restore them, and which transactions to ignore by finishing them immediately without restoring them.

## See Also

- [class SKReceiptRefreshRequest](skreceiptrefreshrequest.md)
  A request to the App Store to get the app receipt, which represents the customer’s transactions with your app.
- [class SKRequest](skrequest.md)
  An abstract class that represents a request to the App Store.
- [class SKPaymentTransaction](skpaymenttransaction.md)
  An object in the payment queue.
- [func SKTerminateForInvalidReceipt()](skterminateforinvalidreceipt().md)
  Terminates an app if the license to use the app has expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKit/restoring-purchased-products)*