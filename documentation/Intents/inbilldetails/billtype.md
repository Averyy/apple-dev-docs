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
var billType: INBillType { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) INBillType billType;
```

*macOS*

```objc
@property (atomic, assign, readwrite) INBillType billType;
```

## Discussion

Use the value of this property to categorize the bill.

## See Also

### Accessing the Bill Information
- [var billPayee: INBillPayee?](./billpayee.md)
  The entity receiving the payment.
- [var paymentDate: DateComponents?](./paymentdate.md)
  The scheduled payment date for the bill.
- [var paymentStatus: INPaymentStatus](./paymentstatus.md)
  The current status of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/billtype)*