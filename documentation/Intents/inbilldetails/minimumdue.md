# minimumDue

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The minimum amount to pay toward the bill.

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
var minimumDue: INCurrencyAmount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INCurrencyAmount * minimumDue;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INCurrencyAmount * minimumDue;
```

#### Discussion

Use this property to specify the minimum amount that the payee expects.

## See Also

### Getting the Bill Amount
- [var amountDue: INCurrencyAmount?](./amountdue.md)
  The amount due for the bill.
- [var dueDate: DateComponents?](./duedate.md)
  The due date of the payment.
- [var lateFee: INCurrencyAmount?](./latefee.md)
  The late fee to apply if the payment is late.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/minimumdue)*