# paymentDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The scheduled payment date for the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var paymentDate: DateComponents? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDateComponents * paymentDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDateComponents * paymentDate;
```

## Discussion

Use this property to specify the scheduled payment date for the bill. When specifying a payment date, be as specific as possible. If you’re unable to give a precise date and time when payment is to occur, you may specify a date range indicating the window for payment to occur. Always ensure that you make payments at the specified time.

## See Also

### Accessing the Bill Information
- [var billPayee: INBillPayee?](./billpayee.md)
  The entity receiving the payment.
- [var paymentStatus: INPaymentStatus](./paymentstatus.md)
  The current status of the payment.
- [var billType: INBillType](./billtype.md)
  The type of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/paymentdate)*