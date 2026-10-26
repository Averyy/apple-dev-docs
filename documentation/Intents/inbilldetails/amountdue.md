# amountDue

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The amount due for the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var amountDue: INCurrencyAmount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INCurrencyAmount * amountDue;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INCurrencyAmount * amountDue;
```

#### Discussion

Use this property to specify the total amount due for the bill, as reported by the payee. This value must be greater than or equal to the value in the [`minimumDue`](./minimumdue.md) property.

## See Also

### Getting the Bill Amount
- [var minimumDue: INCurrencyAmount?](./minimumdue.md)
  The minimum amount to pay toward the bill.
- [var dueDate: DateComponents?](./duedate.md)
  The due date of the payment.
- [var lateFee: INCurrencyAmount?](./latefee.md)
  The late fee to apply if the payment is late.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/amountdue)*