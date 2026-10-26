# dueDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The due date of the payment.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var dueDate: DateComponents? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDateComponents * dueDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDateComponents * dueDate;
```

#### Discussion

Use this property to specify the date to pay the bill to the payee. The first date in the range represents the due date for the payment and the last date represents the date that afterwards the payee considers the payment deliquent. For example, a mortgage payment might be due on the first of the month but the payment isn’t considered delinquent until several weeks later.

## See Also

### Getting the Bill Amount
- [var minimumDue: INCurrencyAmount?](./minimumdue.md)
  The minimum amount to pay toward the bill.
- [var amountDue: INCurrencyAmount?](./amountdue.md)
  The amount due for the bill.
- [var lateFee: INCurrencyAmount?](./latefee.md)
  The late fee to apply if the payment is late.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/duedate)*