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

The payee is an entity that generates bills for the user and receives payment for those bills. The user must register all payees in advance with your app. Search results should contain only bills associated with the specified payee. If the [`INBillPayee`](../inbillpayee.md) object doesn’t contain enough information to identify a payee, don’t filter your search results based on the payee.

## See Also

### Getting the Search Attributes
- [var billType: INBillType](./billtype.md)
  The type of the bill.
- [var dueDateRange: INDateComponentsRange?](./duedaterange.md)
  The range of due dates in which to search for bills.
- [var paymentDateRange: INDateComponentsRange?](./paymentdaterange.md)
  The range of payment dates in which to search for bills.
- [var status: INPaymentStatus](./status.md)
  The status of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintent/billpayee)*