# SKPaymentTransactionObserver

**Framework**: StoreKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that process transactions, unlock purchased functionality, and continue promoted Apple In-App Purchases.

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
protocol SKPaymentTransactionObserver : NSObjectProtocol
```

```objc
@protocol SKPaymentTransactionObserver <NSObject>
```

## Mentions

- [Testing Apple In-App Purchases in Xcode](./testing-in-app-purchases-in-xcode.md)
- [Promoting Apple In-App Purchases](./promoting-in-app-purchases.md)
- [Processing a transaction](./processing-a-transaction.md)
- [Setting up the transaction observer for the payment queue](./setting-up-the-transaction-observer-for-the-payment-queue.md)
- [Testing transaction observer code](./testing-transaction-observer-code.md)
- [Choosing a receipt validation technique](./choosing-a-receipt-validation-technique.md)
- [Supporting Family Sharing in your app](./supporting-family-sharing-in-your-app.md)
- [Testing resubscribing from the subscriptions page](./testing-resubscribing-from-the-subscriptions-page.md)

#### Overview

Observers of [`SKPaymentQueue`](./skpaymentqueue.md) objects implement the methods of this protocol.

The system calls an observer when the queue updates or removes transactions. An observer needs to process all successful transactions, unlock the functionality the user purchases, and then finish the transaction by calling the payment queue’s [`finishTransaction(_:)`](./skpaymentqueue/finishtransaction%28_%29.md) method.

## Topics

### Handling transactions
- [func paymentQueue(SKPaymentQueue, updatedTransactions: [SKPaymentTransaction])](./skpaymenttransactionobserver/paymentqueue%28_,updatedtransactions%29.md)
  Tells an observer that one or more transactions have been updated.
- [func paymentQueue(SKPaymentQueue, removedTransactions: [SKPaymentTransaction])](./skpaymenttransactionobserver/paymentqueue%28_,removedtransactions%29.md)
  Tells an observer that one or more transactions have been removed from the queue.
### Restoring transactions
- [func paymentQueue(SKPaymentQueue, restoreCompletedTransactionsFailedWithError: any Error)](./skpaymenttransactionobserver/paymentqueue%28_,restorecompletedtransactionsfailedwitherror%29.md)
  Tells the observer that an error occurred while restoring transactions.
- [func paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue)](./skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished%28_%29.md)
  Tells the observer that the payment queue has finished sending restored transactions.
### Handling promoted Apple In-App Purchases
- [Promoting Apple In-App Purchases](./promoting-in-app-purchases.md)
  Show promoted Apple In-App Purchases on your product page and handle purchases that customers initiate on the App Store.
- [func paymentQueue(SKPaymentQueue, shouldAddStorePayment: SKPayment, for: SKProduct) -> Bool](./skpaymenttransactionobserver/paymentqueue%28_,shouldaddstorepayment,for%29.md)
  Tells the observer when a user initiates an Apple In-App Purchase from the App Store.
### Revoking entitlements
- [func paymentQueue(SKPaymentQueue, didRevokeEntitlementsForProductIdentifiers: [String])](./skpaymenttransactionobserver/paymentqueue%28_,didrevokeentitlementsforproductidentifiers%29.md)
  Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases.
### Changing the storefront
- [func paymentQueueDidChangeStorefront(SKPaymentQueue)](./skpaymenttransactionobserver/paymentqueuedidchangestorefront%28_%29.md)
  Tells the observer that the storefront for the payment queue has changed.
### Handling download actions
- [func paymentQueue(SKPaymentQueue, updatedDownloads: [SKDownload])](./skpaymenttransactionobserver/paymentqueue%28_,updateddownloads%29.md)
  Tells the observer that the payment queue has updated one or more download objects.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [Setting up the transaction observer for the payment queue](./setting-up-the-transaction-observer-for-the-payment-queue.md)
  Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring Apple In-App Purchases](./offering-completing-and-restoring-in-app-purchases.md)
  Fetch, display, purchase, validate, and finish transactions in your app.
- [class SKPaymentQueue](./skpaymentqueue.md)
  A queue of payment transactions for the App Store to process.
- [protocol SKPaymentQueueDelegate](./skpaymentqueuedelegate.md)
  The protocol that provides information needed to complete transactions.
- [class SKRequest](./skrequest.md)
  An abstract class that represents a request to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver)*