# payee

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The person receiving the funds.

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

## See Also

### Getting Payment Record Details
- [var payer: INPerson?](./payer.md)
  The person providing the funds.
- [var currencyAmount: INCurrencyAmount?](./currencyamount.md)
  The type of currency to transfer and the amount to transfer.
- [var feeAmount: INCurrencyAmount?](./feeamount.md)
  The total amount of any fees added to the payment record.
- [var paymentMethod: INPaymentMethod?](./paymentmethod.md)
  The payment method used to supply the funds.
- [var note: String?](./note.md)
  A description of the payment to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentrecord/payee)*