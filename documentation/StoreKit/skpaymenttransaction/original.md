# original

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The transaction that was restored by the App Store.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use PurchaseResult from Product.purchase(confirmIn:options:).

## Declaration

```swift
var original: SKPaymentTransaction? { get }
```

```objc
@property (nonatomic, readonly, nullable) SKPaymentTransaction * originalTransaction;
```

## Mentions

- [Restoring purchased products](../restoring-purchased-products.md)

#### Discussion

The contents of this property are undefined except when [`transactionState`](./transactionstate.md) is set to [`SKPaymentTransactionState.restored`](../skpaymenttransactionstate/restored.md). When a transaction is restored, the current transaction holds a new transaction identifier, receipt, and so on. Your application will read this property to retrieve the restored transaction.

## See Also

### Getting Transaction Information
- [var payment: SKPayment](./payment.md)
  The payment for the transaction.
- [var transactionIdentifier: String?](./transactionidentifier.md)
  A string that uniquely identifies a successful payment transaction.
- [var transactionDate: Date?](./transactiondate.md)
  The date the transaction was added to the App Store’s payment queue.
- [var error: (any Error)?](./error.md)
  An object describing the error that occurred while processing the transaction.
- [var transactionReceipt: Data?](./transactionreceipt.md)
  A signed receipt that records all information about a successful payment transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/original)*