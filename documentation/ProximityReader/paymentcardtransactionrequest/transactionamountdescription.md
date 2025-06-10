# PaymentCardTransactionRequest.TransactionAmountDescription

**Framework**: ProximityReader  
**Kind**: enum

Values that provide additional information about the transaction amount.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum TransactionAmountDescription
```

#### Overview

This information appears below the central transaction details in the system UI. Each case applies to specific types of transactions, such as a purchase or refund. Check the [`PaymentCardTransactionRequest.TransactionAmountDescription`](paymentcardtransactionrequest/transactionamountdescription.md) values description. If an incompatible transaction type is requested or the value(s) are out of range, it will simply not appear in the system UI.

## Topics

### Enumeration Cases
- [case installment(PaymentCardTransactionRequest.PaymentCycle, amount: Decimal, payments: Int)](paymentcardtransactionrequest/transactionamountdescription/installment(_:amount:payments:).md)
  The total amount authorized upfront. The customer pays the specified amount on each payment cycle. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.membership(_:)](paymentcardtransactionrequest/transactionamountdescription/membership(_:).md)
  Charges the customer the amount shown for each payment cycle. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.preauthorization](paymentcardtransactionrequest/transactionamountdescription/preauthorization.md)
  Places a temporary hold on the customer’s account. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.preauthorizationAmount(_:)](paymentcardtransactionrequest/transactionamountdescription/preauthorizationamount(_:).md)
  Places a temporary hold on the customer’s account for the specified amount. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.preauthorizationRelease](paymentcardtransactionrequest/transactionamountdescription/preauthorizationrelease.md)
  Releases the amount shown from the temporary deposit. Only allowed for [`PaymentCardTransactionRequest.TransactionType.refund`](paymentcardtransactionrequest/transactiontype/refund.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.surchargeAmount(_:)](paymentcardtransactionrequest/transactionamountdescription/surchargeamount(_:).md)
  The transaction’s surcharge amount. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.surchargePercent(_:)](paymentcardtransactionrequest/transactionamountdescription/surchargepercent(_:).md)
  The maximum surcharge percentage the payment processor may apply to the transaction. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let amount: Decimal](paymentcardtransactionrequest/amount.md)
  The amount of the purchase or refund in the specified currency.
- [let currencyCode: String](paymentcardtransactionrequest/currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let type: PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/type.md)
  The type of transaction, either a purchase or a refund.
- [PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/transactiontype.md)
  The type of transaction to perform.
- [var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?](paymentcardtransactionrequest/transactiondescription.md)
  An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactionamountdescription)*