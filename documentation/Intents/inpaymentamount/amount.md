# amount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The precise amount of money to pay.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var amount: INCurrencyAmount? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INCurrencyAmount * amount;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INCurrencyAmount * amount;
```

## Discussion

Upon receiving an intent, this property contains the monetary value (if any) specified by the user. If the amount is missing or `0`, use the [`amountType`](./amounttype.md) property to infer the amount to pay. When reporting amounts back to Siri using this class, always specify a value for this property.

## See Also

### Getting the Payment Amount
- [var amountType: INAmountType](./amounttype.md)
  The account-specific amount to pay.
- [enum INAmountType](../inamounttype.md)
  Constants indicating an account-specific amount to apply to a payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentamount/amount)*