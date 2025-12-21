# transactionIdentifier

**Framework**: StoreKit  
**Kind**: property

A string that uniquely identifies a successful payment transaction.

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
var transactionIdentifier: String? { get }
```

#### Discussion

The contents of this property are undefined except when [`transactionState`](skpaymenttransaction/transactionstate.md) is set to [`SKPaymentTransactionState.purchased`](skpaymenttransactionstate/purchased.md) or [`SKPaymentTransactionState.restored`](skpaymenttransactionstate/restored.md). The [`transactionIdentifier`](skpaymenttransaction/transactionidentifier.md) is a string that uniquely identifies an interaction between the user’s device and the App Store, such as a purchase or restore.

This value has the same format as the transaction’s [`transaction_id`](https://developer.apple.com/documentation/AppStoreReceipts/transaction_id) in the receipt; however, the values may not be the same.

## See Also

- [var payment: SKPayment](skpaymenttransaction/payment.md)
  The payment for the transaction.
- [var transactionDate: Date?](skpaymenttransaction/transactiondate.md)
  The date the transaction was added to the App Store’s payment queue.
- [var original: SKPaymentTransaction?](skpaymenttransaction/original.md)
  The transaction that was restored by the App Store.
- [var error: (any Error)?](skpaymenttransaction/error.md)
  An object describing the error that occurred while processing the transaction.
- [var transactionReceipt: Data?](skpaymenttransaction/transactionreceipt.md)
  A signed receipt that records all information about a successful payment transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactionidentifier)*