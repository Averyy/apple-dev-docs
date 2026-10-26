# status

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The status of the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var status: INPaymentStatus { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INPaymentStatus status;
```

*macOS*

```objc
@property (atomic, assign, readonly) INPaymentStatus status;
```

#### Discussion

When performing the search, your results should contain bills whose status matches the value in this property. If the value in this property is [`INPaymentStatus.unknown`](../inpaymentstatus/unknown.md), return all bills regardless of their status.

## See Also

### Getting the Search Attributes
- [var billPayee: INBillPayee?](./billpayee.md)
  The recipient of the payment.
- [var billType: INBillType](./billtype.md)
  The type of the bill.
- [var dueDateRange: INDateComponentsRange?](./duedaterange.md)
  The range of due dates in which to search for bills.
- [var paymentDateRange: INDateComponentsRange?](./paymentdaterange.md)
  The range of payment dates in which to search for bills.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintent/status)*