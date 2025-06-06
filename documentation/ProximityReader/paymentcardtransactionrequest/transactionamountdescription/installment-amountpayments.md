# PaymentCardTransactionRequest.TransactionAmountDescription.installment(_:amount:payments:)

**Framework**: ProximityReader  
**Kind**: case

The total amount authorized upfront. The customer pays the specified amount on each payment cycle. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
case installment(PaymentCardTransactionRequest.PaymentCycle, amount: Decimal, payments: Int)
```

## Parameters

- `amount`: The amount the payment processor deducts from the card for each installment.
- `payments`: The number of payments for the deducted amount.   Must be greater than  , otherwise the description won’t appear in the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactionamountdescription/installment(_:amount:payments:))*