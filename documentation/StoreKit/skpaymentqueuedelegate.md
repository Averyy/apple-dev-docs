# SKPaymentQueueDelegate

**Framework**: StoreKit  
**Kind**: protocol

The protocol that provides information needed to complete transactions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
protocol SKPaymentQueueDelegate : NSObjectProtocol
```

#### Overview

This protocol includes a method that lets your app determine whether to continue a transaction if the customer’s App Store storefront changes.

## Topics

### Continuing transactions
- [func paymentQueue(SKPaymentQueue, shouldContinue: SKPaymentTransaction, in: SKStorefront) -> Bool](skpaymentqueuedelegate/paymentqueue(_:shouldcontinue:in:).md)
  Asks the delegate whether to continue the transaction if the device’s App Store storefront changes during a transaction.
### Showing price consent
- [func paymentQueueShouldShowPriceConsent(SKPaymentQueue) -> Bool](skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent(_:).md)
  Asks the delegate whether to immediately display a price consent sheet.

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
- [protocol SKPaymentTransactionObserver](skpaymenttransactionobserver.md)
  A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases.
- [class SKRequest](skrequest.md)
  An abstract class that represents a request to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueuedelegate)*