# transactionDescription

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?
```

#### Discussion

This attribute is only displayed when the [`PaymentCardTransactionRequest.TransactionType`](./transactiontype.md) is compatible with the [`PaymentCardTransactionRequest.TransactionAmountDescription`](./transactionamountdescription.md) use case.

## See Also

### Getting the transaction details
- [let amount: Decimal](./amount.md)
  The amount of the purchase or refund in the specified currency.
- [let currencyCode: String](./currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let type: PaymentCardTransactionRequest.TransactionType](./type.md)
  The type of transaction, either a purchase or a refund.
- [PaymentCardTransactionRequest.TransactionType](./transactiontype.md)
  The type of transaction to perform.
- [PaymentCardTransactionRequest.TransactionAmountDescription](./transactionamountdescription.md)
  Values that provide additional information about the transaction amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactiondescription)*