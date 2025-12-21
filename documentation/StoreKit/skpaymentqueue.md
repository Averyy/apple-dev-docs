# SKPaymentQueue

**Framework**: StoreKit  
**Kind**: class

A queue of payment transactions for the App Store to process.

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
class SKPaymentQueue
```

## Mentions

- [Restoring purchased products](restoring-purchased-products.md)
- [Testing transaction observer code](testing-transaction-observer-code.md)
- [Unlocking purchased content](unlocking-purchased-content.md)

#### Overview

The payment queue communicates with the App Store and presents a user interface so that the user can authorize payment. The contents of the queue are persistent between launches of your app.

To process a payment, first add at least one observer object ([`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md)) to the queue (see [`add(_:)`](skpaymentqueue/add(_:)-5ciz2.md)). Then, add a payment object ([`SKPayment`](skpayment.md)) for the item the user wants to purchase. Each time you add a payment object, the queue creates a transaction object ([`SKPaymentTransaction`](skpaymenttransaction.md)) to process that payment and enqueues it to be processed. After payment is fulfilled, the queue updates the transaction object and then calls any observer objects to provide them the updated transaction. Your observer should process the transaction and then remove it from the queue.

The exact mechanism you use to process a processed transaction depends on the design of your app and the product being purchased. Here are a few common examples:

- If the product is a feature already built into your app, your app enables the feature to process the transaction.
- If the product includes downloadable content provided by the App Store, your app retrieves the [`SKDownload`](skdownload.md) objects from the transaction and ask the payment queue to download them. You provide the actual content files to be served by the App Store to App Store Connect when you create the product information.
- If the product represents downloadable content provided by your own server, your app might open a network connection to your server and download the content from there.

For more information on designing the payment processing portion of your app, see [`In-App Purchase Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267).

## Topics

### Determining Whether the User Can Make Payments
- [class func canMakePayments() -> Bool](skpaymentqueue/canmakepayments.md)
  A method that indicates whether the person can make purchases.
### Determining Store Content
- [var storefront: SKStorefront?](skpaymentqueue/storefront.md)
  The App Store storefront of the device.
### Getting the Queue
- [class func `default`() -> Self](skpaymentqueue/default.md)
  Returns the default payment queue instance.
### Adding, Getting, and Removing Observers
- [func add(any SKPaymentTransactionObserver)](skpaymentqueue/add(_:)-5ciz2.md)
  Adds an observer to the payment queue.
- [var transactionObservers: [any SKPaymentTransactionObserver]](skpaymentqueue/transactionobservers.md)
  An array of all active payment queue observers.
- [func remove(any SKPaymentTransactionObserver)](skpaymentqueue/remove(_:).md)
  Removes an observer from the payment queue.
### Managing Transactions
- [var delegate: (any SKPaymentQueueDelegate)?](skpaymentqueue/delegate.md)
  A delegate that provides information needed to complete transactions.
- [var transactions: [SKPaymentTransaction]](skpaymentqueue/transactions.md)
  Returns an array of pending transactions.
- [func add(SKPayment)](skpaymentqueue/add(_:)-4vct1.md)
  Adds a payment request to the queue.
- [func finishTransaction(SKPaymentTransaction)](skpaymentqueue/finishtransaction(_:).md)
  Notifies the App Store that the app finished processing the transaction.
### Restoring Purchases
- [func restoreCompletedTransactions()](skpaymentqueue/restorecompletedtransactions.md)
  Asks the payment queue to restore previously completed purchases.
- [func restoreCompletedTransactions(withApplicationUsername: String?)](skpaymentqueue/restorecompletedtransactions(withapplicationusername:).md)
  Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account.
### Showing Price Consent
- [func showPriceConsentIfNeeded()](skpaymentqueue/showpriceconsentifneeded.md)
  Asks the system to display the price consent sheet if the user hasn’t yet responded to a subscription price increase.
### Redeeming Codes
- [func presentCodeRedemptionSheet()](skpaymentqueue/presentcoderedemptionsheet.md)
  Displays a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
### Downloading Content
- [func start([SKDownload])](skpaymentqueue/start(_:).md)
  Adds a set of downloads to the download list.
- [func cancel([SKDownload])](skpaymentqueue/cancel(_:).md)
  Removes a set of downloads from the download list.
- [func pause([SKDownload])](skpaymentqueue/pause(_:).md)
  Pauses a set of downloads.
- [func resume([SKDownload])](skpaymentqueue/resume(_:).md)
  Resumes a set of downloads.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md)
  Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md)
  Fetch, display, purchase, validate, and finish transactions in your app.
- [protocol SKPaymentTransactionObserver](skpaymenttransactionobserver.md)
  A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases.
- [protocol SKPaymentQueueDelegate](skpaymentqueuedelegate.md)
  The protocol that provides information needed to complete transactions.
- [class SKRequest](skrequest.md)
  An abstract class that represents a request to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue)*