# PaymentCardTransactionRequest.TransactionType

**Framework**: ProximityReader  
**Kind**: enum

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
- [PaymentCardTransactionRequest.TransactionType.purchase](paymentcardtransactionrequest/transactiontype/purchase.md)
  A purchase transaction.
- [PaymentCardTransactionRequest.TransactionType.refund](paymentcardtransactionrequest/transactiontype/refund.md)
  A refund transaction.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let amount: Decimal](paymentcardtransactionrequest/amount.md)
  The amount of the purchase or refund in the specified currency.
- [let currencyCode: String](paymentcardtransactionrequest/currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let type: PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/type.md)
  The type of transaction, either a purchase or a refund.
- [var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?](paymentcardtransactionrequest/transactiondescription.md)
  An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.
- [PaymentCardTransactionRequest.TransactionAmountDescription](paymentcardtransactionrequest/transactionamountdescription.md)
  Values that provide additional information about the transaction amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactiontype)*