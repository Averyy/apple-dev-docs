# original

**Framework**: StoreKit  
**Kind**: property

The transaction that was restored by the App Store.

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
var original: SKPaymentTransaction? { get }
```

## Mentions

- [Restoring purchased products](restoring-purchased-products.md)

#### Discussion

The contents of this property are undefined except when [`transactionState`](skpaymenttransaction/transactionstate.md) is set to [`SKPaymentTransactionState.restored`](skpaymenttransactionstate/restored.md). When a transaction is restored, the current transaction holds a new transaction identifier, receipt, and so on. Your application will read this property to retrieve the restored transaction.

## See Also

- [var payment: SKPayment](skpaymenttransaction/payment.md)
  The payment for the transaction.
- [var transactionIdentifier: String?](skpaymenttransaction/transactionidentifier.md)
  A string that uniquely identifies a successful payment transaction.
- [var transactionDate: Date?](skpaymenttransaction/transactiondate.md)
  The date the transaction was added to the App Store’s payment queue.
- [var error: (any Error)?](skpaymenttransaction/error.md)
  An object describing the error that occurred while processing the transaction.
- [var transactionReceipt: Data?](skpaymenttransaction/transactionreceipt.md)
  A signed receipt that records all information about a successful payment transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/original)*