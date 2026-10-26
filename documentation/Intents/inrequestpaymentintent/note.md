# note

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A note associated with the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var note: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * note;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * note;
```

#### Discussion

The user can include a note to indicate the reason for the request. Notes are not normally required, but you can require them as needed to help process the request.

## See Also

### Getting Details About the Payment
- [var payer: INPerson?](./payer.md)
  The recipient of the payment request.
- [var currencyAmount: INCurrencyAmount?](./currencyamount.md)
  The amount of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintent/note)*