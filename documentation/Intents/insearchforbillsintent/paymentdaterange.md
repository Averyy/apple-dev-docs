# paymentDateRange

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The range of payment dates in which to search for bills.

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
var paymentDateRange: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * paymentDateRange;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * paymentDateRange;
```

## Discussion

When performing the search, your results should contain only bills whose payment date falls within the specified date range. With no specified date range, you must decide how you want to filter results during your search. You should limit the number of search results in some way. For example, you might want to return only the bills paid during the past month or during the past year.

## See Also

### Getting the Search Attributes
- [var billPayee: INBillPayee?](./billpayee.md)
  The recipient of the payment.
- [var billType: INBillType](./billtype.md)
  The type of the bill.
- [var dueDateRange: INDateComponentsRange?](./duedaterange.md)
  The range of due dates in which to search for bills.
- [var status: INPaymentStatus](./status.md)
  The status of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintent/paymentdaterange)*