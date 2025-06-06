# payment

**Framework**: StoreKit  
**Kind**: property

The payment for the transaction.

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
var payment: SKPayment { get }
```

#### Discussion

Each payment transaction is created in response to a payment that your application added to the payment queue.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/payment)*