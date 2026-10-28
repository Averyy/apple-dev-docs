# billType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var billType: INBillType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INBillType billType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INBillType billType;
```

## Discussion

Use this information to identify which bill the user wants to pay. You might use this property when the payee provides multiple services, but bills them separately.

## See Also

### Getting the Bill Information
- [var billPayee: INBillPayee?](./billpayee.md)
  The recipient of the payment.
- [var dueDate: INDateComponentsRange?](./duedate.md)
  The due date of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintent/billtype)*