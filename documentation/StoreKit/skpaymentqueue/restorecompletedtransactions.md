# restoreCompletedTransactions()

**Framework**: StoreKit  
**Kind**: method

Asks the payment queue to restore previously completed purchases.

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
func restoreCompletedTransactions()
```

## Mentions

- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)
- [Validating receipts with the App Store](validating-receipts-with-the-app-store.md)
- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Restoring purchased products](restoring-purchased-products.md)

#### Discussion

Use this method to restore finished transactions—that is, transactions for which you have already called [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md). You call this method in one of the following situations:

- To install purchases on additional devices
- To restore purchases for an application that the user deleted and reinstalled

When you create a new product to be sold in your store, you choose whether that product can be restored or not. See the [`In-App Purchase Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267) for more information.

The payment queue delivers a new transaction for each previously completed transaction that can be restored. Each transaction includes a copy of the original transaction.

After the transactions are delivered, the payment queue calls the observer’s [`paymentQueueRestoreCompletedTransactionsFinished(_:)`](skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:).md) method. If an error occurred while restoring transactions, the observer will be notified through its [`paymentQueue(_:restoreCompletedTransactionsFailedWithError:)`](skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:).md) method.

This method has no effect in the following situations:

- All transactions are unfinished.
- The user did not purchase anything that is restorable.
- You tried to restore items that are not restorable, such as a non-renewing subscription or a consumable product.
- Your app’s build version does not meet the guidelines for the `CFBundleVersion` key.

> ❗ **Important**:  If you are using the [`In-App Purchase`](in-app-purchase.md) API and managing transactions using the [`Transaction`](transaction.md) API, use [`currentEntitlements`](transaction/currententitlements.md) to determine which in-app purchases the customer is currently entitled to. The [`restoreCompletedTransactions()`](skpaymentqueue/restorecompletedtransactions().md) function doesn’t affect transactions in the [`Transaction`](transaction.md) API. In rare cases when a user suspects the app isn’t showing all the transactions, call [`sync()`](appstore/sync().md) in response to an explicit user action, like tapping a button.

 If you are using the [`In-App Purchase`](in-app-purchase.md) API and managing transactions using the [`Transaction`](transaction.md) API, use [`currentEntitlements`](transaction/currententitlements.md) to determine which in-app purchases the customer is currently entitled to. The [`restoreCompletedTransactions()`](skpaymentqueue/restorecompletedtransactions().md) function doesn’t affect transactions in the [`Transaction`](transaction.md) API. In rare cases when a user suspects the app isn’t showing all the transactions, call [`sync()`](appstore/sync().md) in response to an explicit user action, like tapping a button.

## See Also

- [func restoreCompletedTransactions(withApplicationUsername: String?)](skpaymentqueue/restorecompletedtransactions(withapplicationusername:).md)
  Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/restorecompletedtransactions())*