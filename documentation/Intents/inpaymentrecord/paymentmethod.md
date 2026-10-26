# paymentMethod

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The payment method used to supply the funds.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var paymentMethod: INPaymentMethod? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPaymentMethod * paymentMethod;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPaymentMethod * paymentMethod;
```

## See Also

### Getting Payment Record Details
- [var payee: INPerson?](./payee.md)
  The person receiving the funds.
- [var payer: INPerson?](./payer.md)
  The person providing the funds.
- [var currencyAmount: INCurrencyAmount?](./currencyamount.md)
  The type of currency to transfer and the amount to transfer.
- [var feeAmount: INCurrencyAmount?](./feeamount.md)
  The total amount of any fees added to the payment record.
- [var note: String?](./note.md)
  A description of the payment to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentrecord/paymentmethod)*