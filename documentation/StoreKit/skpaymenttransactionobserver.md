# SKPaymentTransactionObserver

**Framework**: StoreKit  
**Kind**: protocol

A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases.

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
protocol SKPaymentTransactionObserver : NSObjectProtocol
```

## Mentions

- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Promoting In-App Purchases](promoting-in-app-purchases.md)
- [Processing a transaction](processing-a-transaction.md)
- [Testing transaction observer code](testing-transaction-observer-code.md)
- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md)
- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)
- [Supporting Family Sharing in your app](supporting-family-sharing-in-your-app.md)
- [Testing resubscribing from the subscriptions page](testing-resubscribing-from-the-subscriptions-page.md)

#### Overview

Observers of [`SKPaymentQueue`](skpaymentqueue.md) objects implement the methods of this protocol.

The system calls an observer when the queue updates or removes transactions. An observer needs to process all successful transactions, unlock the functionality the user purchases, and then finish the transaction by calling the payment queue’s [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md) method.

## Topics

### Handling transactions
- [func paymentQueue(SKPaymentQueue, updatedTransactions: [SKPaymentTransaction])](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md)
  Tells an observer that one or more transactions have been updated.
- [func paymentQueue(SKPaymentQueue, removedTransactions: [SKPaymentTransaction])](skpaymenttransactionobserver/paymentqueue(_:removedtransactions:).md)
  Tells an observer that one or more transactions have been removed from the queue.
### Restoring transactions
- [func paymentQueue(SKPaymentQueue, restoreCompletedTransactionsFailedWithError: any Error)](skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:).md)
  Tells the observer that an error occurred while restoring transactions.
- [func paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue)](skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:).md)
  Tells the observer that the payment queue has finished sending restored transactions.
### Handling promoted in-app purchases
- [Promoting In-App Purchases](promoting-in-app-purchases.md)
  Show promoted In-App Purchases on your product page and handle purchases that customers initiate on the App Store.
- [func paymentQueue(SKPaymentQueue, shouldAddStorePayment: SKPayment, for: SKProduct) -> Bool](skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:).md)
  Tells the observer when a user initiates an in-app purchase from the App Store.
### Revoking entitlements
- [func paymentQueue(SKPaymentQueue, didRevokeEntitlementsForProductIdentifiers: [String])](skpaymenttransactionobserver/paymentqueue(_:didrevokeentitlementsforproductidentifiers:).md)
  Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases.
### Changing the storefront
- [func paymentQueueDidChangeStorefront(SKPaymentQueue)](skpaymenttransactionobserver/paymentqueuedidchangestorefront(_:).md)
  Tells the observer that the storefront for the payment queue has changed.
### Handling download actions
- [func paymentQueue(SKPaymentQueue, updatedDownloads: [SKDownload])](skpaymenttransactionobserver/paymentqueue(_:updateddownloads:).md)
  Tells the observer that the payment queue has updated one or more download objects.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md)
  Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md)
  Fetch, display, purchase, validate, and finish transactions in your app.
- [class SKPaymentQueue](skpaymentqueue.md)
  A queue of payment transactions for the App Store to process.
- [protocol SKPaymentQueueDelegate](skpaymentqueuedelegate.md)
  The protocol that provides information needed to complete transactions.
- [class SKRequest](skrequest.md)
  An abstract class that represents a request to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver)*