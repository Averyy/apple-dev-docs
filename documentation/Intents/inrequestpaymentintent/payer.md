# payer

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The recipient of the payment request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var payer: INPerson? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPerson * payer;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPerson * payer;
```

#### Discussion

Use the payer information to determine which user to notify.

## See Also

### Getting Details About the Payment
- [var currencyAmount: INCurrencyAmount?](./currencyamount.md)
  The amount of the payment.
- [var note: String?](./note.md)
  A note associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintent/payer)*