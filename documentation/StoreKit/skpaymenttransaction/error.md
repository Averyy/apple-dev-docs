# error

**Framework**: StoreKit  
**Kind**: property

An object describing the error that occurred while processing the transaction.

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
var error: (any Error)? { get }
```

#### Discussion

The [`error`](skpaymenttransaction/error.md) property is undefined except when [`transactionState`](skpaymenttransaction/transactionstate.md) is set to [`SKPaymentTransactionState.failed`](skpaymenttransactionstate/failed.md). Your application can read the [`error`](skpaymenttransaction/error.md) property to determine why the transaction failed. For a list of error constants, see SKErrorDomain in `StoreKit Constants`.

## See Also

- [In-App Purchase Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)
- [var payment: SKPayment](skpaymenttransaction/payment.md)
  The payment for the transaction.
- [var transactionIdentifier: String?](skpaymenttransaction/transactionidentifier.md)
  A string that uniquely identifies a successful payment transaction.
- [var transactionDate: Date?](skpaymenttransaction/transactiondate.md)
  The date the transaction was added to the App Store’s payment queue.
- [var original: SKPaymentTransaction?](skpaymenttransaction/original.md)
  The transaction that was restored by the App Store.
- [var transactionReceipt: Data?](skpaymenttransaction/transactionreceipt.md)
  A signed receipt that records all information about a successful payment transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/error)*