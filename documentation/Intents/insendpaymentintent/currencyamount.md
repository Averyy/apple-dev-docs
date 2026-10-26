# currencyAmount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The amount of the payment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var currencyAmount: INCurrencyAmount? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INCurrencyAmount * currencyAmount;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INCurrencyAmount * currencyAmount;
```

#### Discussion

Use this property to verify that you can handle the transfer successfully. For example, you might verify they are using a supported currency type and that the user’s account has the needed funds to complete the transaction.

## See Also

### Getting Details About the Payment
- [var payee: INPerson?](./payee.md)
  The recipient of the payment.
- [var note: String?](./note.md)
  A note associated with the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintent/currencyamount)*