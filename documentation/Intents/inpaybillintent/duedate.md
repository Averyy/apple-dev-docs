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
@NSCopying
var dueDate: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * dueDate;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * dueDate;
```

## Discussion

Use this property to get the date by which the payer must make a payment to the payee. The first date in the range represents the due date for the payment and the last date represents the deliquent date. For example, a mortgage payment might be due on the first of the month but the payment isn’t considered delinquent until several weeks later.

## See Also

### Getting the Bill Information
- [var billPayee: INBillPayee?](./billpayee.md)
  The recipient of the payment.
- [var billType: INBillType](./billtype.md)
  The type of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintent/duedate)*