# transactionDescription

**Framework**: ProximityReader  
**Kind**: property

An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?
```

#### Discussion

This attribute is only displayed when the [`PaymentCardTransactionRequest.TransactionType`](paymentcardtransactionrequest/transactiontype.md) is compatible with the [`PaymentCardTransactionRequest.TransactionAmountDescription`](paymentcardtransactionrequest/transactionamountdescription.md) use case.

## See Also

- [let amount: Decimal](paymentcardtransactionrequest/amount.md)
  The amount of the purchase or refund in the specified currency.
- [let currencyCode: String](paymentcardtransactionrequest/currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let type: PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/type.md)
  The type of transaction, either a purchase or a refund.
- [PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/transactiontype.md)
  The type of transaction to perform.
- [PaymentCardTransactionRequest.TransactionAmountDescription](paymentcardtransactionrequest/transactionamountdescription.md)
  Values that provide additional information about the transaction amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactiondescription)*