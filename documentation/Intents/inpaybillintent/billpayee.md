# billPayee

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The recipient of the payment.

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
var billPayee: INBillPayee? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INBillPayee * billPayee;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INBillPayee * billPayee;
```

## Discussion

Use the information in this property to identify the recipient of the payment. You must configure your app to process payments for the specified payee before handling the request.

## See Also

### Getting the Bill Information
- [var billType: INBillType](./billtype.md)
  The type of the bill.
- [var dueDate: INDateComponentsRange?](./duedate.md)
  The due date of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintent/billpayee)*