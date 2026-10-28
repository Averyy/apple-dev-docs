# payee

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The recipient of the payment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var payee: INPerson? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPerson * payee;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPerson * payee;
```

## Discussion

Use the payee information to determine which account receives the payment.

## See Also

### Getting Details About the Payment
- [var currencyAmount: INCurrencyAmount?](./currencyamount.md)
  The amount of the payment.
- [var note: String?](./note.md)
  A note associated with the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintent/payee)*