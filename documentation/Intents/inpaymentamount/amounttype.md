# amountType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The account-specific amount to pay.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var amountType: INAmountType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INAmountType amountType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INAmountType amountType;
```

## Discussion

When processing an intent, use this property to determine if the user wanted to pay the minimum amount, the amount due, or the current balance due for the bill. You can then map each constant to the appropriate amount when creating your response. If this value is [`INAmountType.unknown`](../inamounttype/unknown.md), use the value in the [`amount`](./amount.md) property to determine the payment amount.

## See Also

### Getting the Payment Amount
- [var amount: INCurrencyAmount?](./amount.md)
  The precise amount of money to pay.
- [enum INAmountType](../inamounttype.md)
  Constants indicating an account-specific amount to apply to a payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentamount/amounttype)*