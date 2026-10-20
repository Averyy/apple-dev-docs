# PaymentCardTransactionRequest.TransactionType

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

The type of transaction to perform.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum TransactionType
```

## Topics

### Getting the transaction type
- [PaymentCardTransactionRequest.TransactionType.purchase](./transactiontype/purchase.md)
  A purchase transaction.
- [PaymentCardTransactionRequest.TransactionType.refund](./transactiontype/refund.md)
  A refund transaction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the transaction details
- [let amount: Decimal](./amount.md)
  The amount of the purchase or refund in the specified currency.
- [let currencyCode: String](./currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let type: PaymentCardTransactionRequest.TransactionType](./type.md)
  The type of transaction, either a purchase or a refund.
- [var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?](./transactiondescription.md)
  An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.
- [PaymentCardTransactionRequest.TransactionAmountDescription](./transactionamountdescription.md)
  Values that provide additional information about the transaction amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactiontype)*