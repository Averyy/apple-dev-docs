# init(amount:currencyCode:for:)

**Framework**: ProximityReader  
**Kind**: init

Creates a new transaction request for the specified amount in the designated currency.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
init(amount: Decimal, currencyCode: String, for type: PaymentCardTransactionRequest.TransactionType = .purchase)
```

## Parameters

- `amount`: The purchase or refund price in the specified currency. This value must be greater than 0.
- `currencyCode`: The ISO 4217 code that indicates the currency type for the purchase or refund.
- `type`: A value that indicates whether the transaction is a purchase or refund.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/init(amount:currencycode:for:))*