# billPayee

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The entity receiving the payment.

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
var billPayee: INBillPayee? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INBillPayee * billPayee;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INBillPayee * billPayee;
```

#### Discussion

Use this property to specify the recipient of the payment. The payee may refer to a bank, a utility, or any entity for which the user has set up online bill payment in your app. The user must configure payees in advance in your app.

## See Also

### Accessing the Bill Information
- [var paymentDate: DateComponents?](./paymentdate.md)
  The scheduled payment date for the bill.
- [var paymentStatus: INPaymentStatus](./paymentstatus.md)
  The current status of the payment.
- [var billType: INBillType](./billtype.md)
  The type of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/billpayee)*