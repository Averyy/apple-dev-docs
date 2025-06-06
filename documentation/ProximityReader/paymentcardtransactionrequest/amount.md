# amount

**Framework**: ProximityReader  
**Kind**: property

The amount of the purchase or refund in the specified currency.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
let amount: Decimal
```

#### Discussion

The value in this property must be greater than 0.

## See Also

- [let currencyCode: String](paymentcardtransactionrequest/currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let type: PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/type.md)
  The type of transaction, either a purchase or a refund.
- [PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/transactiontype.md)
  The type of transaction to perform.
- [var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?](paymentcardtransactionrequest/transactiondescription.md)
  An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.
- [PaymentCardTransactionRequest.TransactionAmountDescription](paymentcardtransactionrequest/transactionamountdescription.md)
  Values that provide additional information about the transaction amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/amount)*