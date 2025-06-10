# SKPaymentTransaction

**Framework**: StoreKit  
**Kind**: class

An object in the payment queue.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class SKPaymentTransaction
```

## Mentions

- [Restoring purchased products](restoring-purchased-products.md)
- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)

#### Overview

A payment transaction is created whenever a payment is added to the payment queue. The system delivers transactions to your app when the App Store finishes processing the payment. Completed transactions provide a receipt and transaction identifier that your app can use to save a permanent record of the processed payment.

## Topics

### Getting Transaction Information
- [var payment: SKPayment](skpaymenttransaction/payment.md)
  The payment for the transaction.
- [var transactionIdentifier: String?](skpaymenttransaction/transactionidentifier.md)
  A string that uniquely identifies a successful payment transaction.
- [var transactionDate: Date?](skpaymenttransaction/transactiondate.md)
  The date the transaction was added to the App Store’s payment queue.
- [var original: SKPaymentTransaction?](skpaymenttransaction/original.md)
  The transaction that was restored by the App Store.
- [var error: (any Error)?](skpaymenttransaction/error.md)
  An object describing the error that occurred while processing the transaction.
- [var transactionReceipt: Data?](skpaymenttransaction/transactionreceipt.md)
  A signed receipt that records all information about a successful payment transaction.
### Getting Downloads
- [var downloads: [SKDownload]](skpaymenttransaction/downloads.md)
  An array of download objects representing the downloadable content associated with the transaction.
### Getting Transaction State
- [var transactionState: SKPaymentTransactionState](skpaymenttransaction/transactionstate.md)
  The current state of the transaction.
- [enum SKPaymentTransactionState](skpaymenttransactionstate.md)
  Values representing the state of a transaction.

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

- [Requesting a payment from the App Store](requesting-a-payment-from-the-app-store.md)
  Submit a payment request to the App Store when a customer selects a product to buy.
- [Processing a transaction](processing-a-transaction.md)
  Register a transaction queue observer to get and handle transaction updates from the App Store.
- [class SKPayment](skpayment.md)
  A request to the App Store to process payment for additional functionality that your app offers.
- [class SKMutablePayment](skmutablepayment.md)
  A mutable request to the App Store to process payment for additional functionality that your app offers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction)*