# PaymentCardTransactionRequest.TransactionAmountDescription.surchargePercent(_:)

**Framework**: ProximityReader  
**Kind**: case

The maximum surcharge percentage the payment processor may apply to the transaction. Only allowed for [`PaymentCardTransactionRequest.TransactionType.purchase`](paymentcardtransactionrequest/transactiontype/purchase.md)

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
case surchargePercent(Double)
```

#### Discussion

The payment processor determines the final surcharge amount when they process the transaction. The percentage value is between 1 and 100 and up to two decimal places.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/transactionamountdescription/surchargepercent(_:))*