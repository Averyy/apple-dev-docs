# restoreCompletedTransactions()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Asks the payment queue to restore previously completed purchases.

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
func restoreCompletedTransactions()
```

```objc
- (void) restoreCompletedTransactions;
```

## Mentions

- [Choosing a receipt validation technique](../choosing-a-receipt-validation-technique.md)
- [Restoring purchased products](../restoring-purchased-products.md)
- [Testing Apple In-App Purchases in Xcode](../testing-in-app-purchases-in-xcode.md)
- [Validating receipts with the App Store](../validating-receipts-with-the-app-store.md)

#### Discussion

Use this method to restore finished transactions—that is, transactions for which you have already called [`finishTransaction(_:)`](./finishtransaction%28_%29.md). You call this method in one of the following situations:

- To install purchases on additional devices
- To restore purchases for an application that the user deleted and reinstalled

When you create a new product to be sold in your store, you choose whether that product can be restored or not. See the [Apple In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267) for more information.

The payment queue delivers a new transaction for each previously completed transaction that can be restored. Each transaction includes a copy of the original transaction.

After the transactions are delivered, the payment queue calls the observer’s [`paymentQueueRestoreCompletedTransactionsFinished(_:)`](../skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished%28_%29.md) method. If an error occurred while restoring transactions, the observer will be notified through its [`paymentQueue(_:restoreCompletedTransactionsFailedWithError:)`](../skpaymenttransactionobserver/paymentqueue%28_,restorecompletedtransactionsfailedwitherror%29.md) method.

This method has no effect in the following situations:

- All transactions are unfinished.
- The user did not purchase anything that is restorable.
- You tried to restore items that are not restorable, such as a non-renewing subscription or a consumable product.
- Your app’s build version does not meet the guidelines for the `CFBundleVersion` key.

> ❗ **Important**:  If you are using the [Apple In-App Purchase](../in-app-purchase.md) API and managing transactions using the [`Transaction`](../transaction.md) API, use [`currentEntitlements`](../transaction/currententitlements.md) to determine which in-app purchases the customer is currently entitled to. The [`restoreCompletedTransactions()`](./restorecompletedtransactions%28%29.md) function doesn’t affect transactions in the [`Transaction`](../transaction.md) API. In rare cases when a user suspects the app isn’t showing all the transactions, call [`sync()`](../appstore/sync%28%29.md) in response to an explicit user action, like tapping a button.

## See Also

### Restoring Purchases
- [func restoreCompletedTransactions(withApplicationUsername: String?)](./restorecompletedtransactions%28withapplicationusername%29.md)
  Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/restorecompletedtransactions())*