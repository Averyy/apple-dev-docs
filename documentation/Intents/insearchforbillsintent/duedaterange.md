# dueDateRange

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The range of due dates in which to search for bills.

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
var dueDateRange: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * dueDateRange;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * dueDateRange;
```

## Discussion

When performing the search, your results should contain only bills whose due date falls within the specified date range. With no specified date range, you must decide how you want to filter results during your search. You should limit the number of search results in some way. For example, you might return only the currently due bills.

## See Also

### Getting the Search Attributes
- [var billPayee: INBillPayee?](./billpayee.md)
  The recipient of the payment.
- [var billType: INBillType](./billtype.md)
  The type of the bill.
- [var paymentDateRange: INDateComponentsRange?](./paymentdaterange.md)
  The range of payment dates in which to search for bills.
- [var status: INPaymentStatus](./status.md)
  The status of the bill.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintent/duedaterange)*