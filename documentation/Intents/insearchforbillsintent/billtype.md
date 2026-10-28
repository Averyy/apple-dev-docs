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

When performing the search, your results should contain bills whose type matches the value in this property. If the value in this property is [`INBillType.unknown`](../inbilltype/unknown.md), return all bills regardless of their type.

## See Also

### Getting the Search Attributes
- [var billPayee: INBillPayee?](./billpayee.md)
  The recipient of the payment.
- [var dueDateRange: INDateComponentsRange?](./duedaterange.md)
  The range of due dates in which to search for bills.
- [var paymentDateRange: INDateComponentsRange?](./paymentdaterange.md)
  The range of payment dates in which to search for bills.
- [var status: INPaymentStatus](./status.md)
  The status of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintent/billtype)*