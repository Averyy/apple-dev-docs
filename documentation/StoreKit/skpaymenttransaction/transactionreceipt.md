# transactionReceipt

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A signed receipt that records all information about a successful payment transaction.

**Availability**:
- tvOS - Deprecated in 18.0

> **Deprecated**: Use the app receipt instead, as described in [Receipt Validation Programming Guide](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573).

## Declaration

```swift
var transactionReceipt: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * transactionReceipt;
```

## Discussion

The contents of this property are undefined except when [`transactionState`](./transactionstate.md) is set to [`SKPaymentTransactionState.purchased`](../skpaymenttransactionstate/purchased.md).

The receipt is a signed chunk of data that can be sent to the App Store to verify that the payment was successfully processed. This is most useful when designing a store that uses a server separate from the iPhone to verify that payment was processed. For more information on verifying receipts, see [Receipt Validation Programming Guide](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573).

## See Also

### Getting Transaction Information
- [var payment: SKPayment](./payment.md)
  The payment for the transaction.
- [var transactionIdentifier: String?](./transactionidentifier.md)
  A string that uniquely identifies a successful payment transaction.
- [var transactionDate: Date?](./transactiondate.md)
  The date the transaction was added to the App Store’s payment queue.
- [var original: SKPaymentTransaction?](./original.md)
  The transaction that was restored by the App Store.
- [var error: (any Error)?](./error.md)
  An object describing the error that occurred while processing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactionreceipt)*