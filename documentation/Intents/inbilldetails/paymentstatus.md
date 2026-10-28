# paymentStatus

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The current status of the payment.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var paymentStatus: INPaymentStatus { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) INPaymentStatus paymentStatus;
```

*macOS*

```objc
@property (atomic, assign, readwrite) INPaymentStatus paymentStatus;
```

## Discussion

Specify the current status of a scheduled payment. If the payment date of the bill is in the future, you typically set the payment status to [`INPaymentStatus.pending`](../inpaymentstatus/pending.md). For bills in the past, set the status to [`INPaymentStatus.completed`](../inpaymentstatus/completed.md) if payment was successful or to another value if the transaction wasn’t completed. If you haven’t scheduled the bill for payment, set its status to [`INPaymentStatus.unknown`](../inpaymentstatus/unknown.md).

## See Also

### Accessing the Bill Information
- [var billPayee: INBillPayee?](./billpayee.md)
  The entity receiving the payment.
- [var paymentDate: DateComponents?](./paymentdate.md)
  The scheduled payment date for the bill.
- [var billType: INBillType](./billtype.md)
  The type of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/paymentstatus)*