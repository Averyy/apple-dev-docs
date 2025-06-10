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
### Operators
- [static func == (PaymentCardTransactionRequest.TransactionType, PaymentCardTransactionRequest.TransactionType) -> Bool](paymentcardtransactionrequest/transactiontype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](paymentcardtransactionrequest/transactiontype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](paymentcardtransactionrequest/transactiontype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](paymentcardtransactionrequest/transactiontype/equatable-implementations.md)

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