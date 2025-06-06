# Product.SubscriptionPeriod

**Framework**: StoreKit  
**Kind**: struct

Values that represent the duration of time between subscription renewals.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SubscriptionPeriod
```

#### Overview

Use the [`value`](product/subscriptionperiod/value.md) and the [`unit`](product/subscriptionperiod/unit-swift.property.md) together to determine the subscription period. For example, if the unit is [`Product.SubscriptionPeriod.Unit.month`](product/subscriptionperiod/unit-swift.enum/month.md), and the [`value`](product/subscriptionperiod/value.md) is `3`, the subscription period is three months.

## Topics

### Getting the subscription period
- [let value: Int](product/subscriptionperiod/value.md)
  The number of period units.
- [let unit: Product.SubscriptionPeriod.Unit](product/subscriptionperiod/unit-swift.property.md)
  The increment of time for the subscription period.
- [Product.SubscriptionPeriod.Unit](product/subscriptionperiod/unit-swift.enum.md)
  Units of time that describe subscription periods.
### Getting the period date range
- [func dateRange(referenceDate: Date) -> Range<Date>](product/subscriptionperiod/daterange(referencedate:).md)
  The calculated date range of a subscription period, starting at the reference date.
### Getting subscription periods
- [static var everySixMonths: Product.SubscriptionPeriod](product/subscriptionperiod/everysixmonths.md)
- [static var everyThreeDays: Product.SubscriptionPeriod](product/subscriptionperiod/everythreedays.md)
- [static var everyThreeMonths: Product.SubscriptionPeriod](product/subscriptionperiod/everythreemonths.md)
- [static var everyTwoMonths: Product.SubscriptionPeriod](product/subscriptionperiod/everytwomonths.md)
- [static var everyTwoWeeks: Product.SubscriptionPeriod](product/subscriptionperiod/everytwoweeks.md)
- [static var monthly: Product.SubscriptionPeriod](product/subscriptionperiod/monthly.md)
- [static var weekly: Product.SubscriptionPeriod](product/subscriptionperiod/weekly.md)
- [static var yearly: Product.SubscriptionPeriod](product/subscriptionperiod/yearly.md)
### Formatting the subscription period
- [func formatted<S>(S, referenceDate: Date) -> S.FormatOutput](product/subscriptionperiod/formatted(_:referencedate:)-3t7wd.md)
  Formats the subscription period using a format style that takes a date range as an input.
- [func formatted<S>(S, referenceDate: Date) -> S.FormatOutput](product/subscriptionperiod/formatted(_:referencedate:)-8s3ar.md)
  Formats the subscription period using a format style that takes a duration as an input.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let subscription: Product.SubscriptionInfo?](product/subscription.md)
  The subscription information for an auto-renewable subscripton.
- [Product.SubscriptionInfo](product/subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiod)*