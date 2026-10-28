# PaymentCardTransactionRequest.TransactionAmountDescription

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

Values that provide additional information about the transaction amount.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
enum TransactionAmountDescription
```

## Overview

This information appears below the central transaction details in the system UI. Each case applies to specific types of transactions, such as a purchase or refund. Check the [`PaymentCardTransactionRequest.TransactionAmountDescription`](./transactionamountdescription.md) values description. If an incompatible transaction type is requested or the value(s) are out of range, it will simply not appear in the system UI.

## Topics

### Enumeration Cases
- [case installment(PaymentCardTransactionRequest.PaymentCycle, amount: Decimal, payments: Int)](./transactionamountdescription/installment%28_,amount,payments%29.md)
  The total amount authorized upfront. The customer pays the specified amount on each payment cycle. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](./transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.membership(_:)](./transactionamountdescription/membership%28_%29.md)
  Charges the customer the amount shown for each payment cycle. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](./transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.preauthorization](./transactionamountdescription/preauthorization.md)
  Places a temporary hold on the customer’s account. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](./transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.preauthorizationAmount(_:)](./transactionamountdescription/preauthorizationamount%28_%29.md)
  Places a temporary hold on the customer’s account for the specified amount. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](./transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.preauthorizationRelease](./transactionamountdescription/preauthorizationrelease.md)
  Releases the amount shown from the temporary deposit. Only allowed for [`PaymentCardTransactionRequest.TransactionType.refund`](./transactiontype/refund.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.surchargeAmount(_:)](./transactionamountdescription/surchargeamount%28_%29.md)
  The transaction’s surcharge amount. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](./transactiontype/purchase.md)
- [PaymentCardTransactionRequest.TransactionAmountDescription.surchargePercent(_:)](./transactionamountdescription/surchargepercent%28_%29.md)
  The maximum surcharge percentage the payment processor may apply to the transaction. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](./transactiontype/purchase.md)

## Relationships

### Conforms To
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
- [PaymentCardTransactionRequest.TransactionType](./transactiontype.md)
  The type of transaction to perform.
- [var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?](./transactiondescription.md)
  An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactionamountdescription)*