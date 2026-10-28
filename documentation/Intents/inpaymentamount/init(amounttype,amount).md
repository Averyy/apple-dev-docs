# init(amountType:amount:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a payment amount object with the specified amounts.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(amountType: INAmountType, amount: INCurrencyAmount)
```

```objc
- (instancetype) initWithAmountType:(INAmountType) amountType amount:(INCurrencyAmount *) amount;
```

## Return Value

An initialized payment amount object, or `nil` if the object could not be created.

## Discussion

When creating an [`INPaymentAmount`](../inpaymentamount.md) object, specify as much information as you have available. Specifically, include a value for the `amount` parameter indicating the amount of money to debit from the user’s account. If that value also represents a specific amount type, such as the balance due on the account, specify an appropriate constant in the [`amountType`](./amounttype.md) property.

## Parameters

- `amountType`: A constant indicating an account-specific amount. Use this parameter to specify whether the payment amount represents the minimum amount due, the current account balance, or the amount due. If the amount does not correspond to any of those values, specify [`INAmountType.unknown`](../inamounttype/unknown.md).
- `amount`: The numerical amount to apply to the payment. Use this parameter to specify the precise amount being applied to the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentamount/init(amounttype:amount:))*