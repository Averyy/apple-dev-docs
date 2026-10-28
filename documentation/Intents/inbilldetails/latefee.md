# lateFee

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The late fee to apply if the payment is late.

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
var lateFee: INCurrencyAmount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INCurrencyAmount * lateFee;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INCurrencyAmount * lateFee;
```

## Discussion

Use this property to specify the late fee, if any, that to apply if the user pays the bill after the due date.

## See Also

### Getting the Bill Amount
- [var minimumDue: INCurrencyAmount?](./minimumdue.md)
  The minimum amount to pay toward the bill.
- [var amountDue: INCurrencyAmount?](./amountdue.md)
  The amount due for the bill.
- [var dueDate: DateComponents?](./duedate.md)
  The due date of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/latefee)*