# Product.SubscriptionPeriod

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Values that represent the duration of time between subscription renewals.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SubscriptionPeriod
```

## Overview

Use the [`value`](./subscriptionperiod/value.md) and the [`unit`](./subscriptionperiod/unit-swift.property.md) together to determine the subscription period. For example, if the unit is [`Product.SubscriptionPeriod.Unit.month`](./subscriptionperiod/unit-swift.enum/month.md), and the [`value`](./subscriptionperiod/value.md) is `3`, the subscription period is three months.

## Topics

### Getting the subscription period
- [let value: Int](./subscriptionperiod/value.md)
  The number of period units.
- [let unit: Product.SubscriptionPeriod.Unit](./subscriptionperiod/unit-swift.property.md)
  The increment of time for the subscription period.
- [Product.SubscriptionPeriod.Unit](./subscriptionperiod/unit-swift.enum.md)
  Units of time that describe subscription periods.
### Getting the period date range
- [func dateRange(referenceDate: Date) -> Range<Date>](./subscriptionperiod/daterange%28referencedate%29.md)
  The calculated date range of a subscription period, starting at the reference date.
### Getting subscription periods
- [static var everySixMonths: Product.SubscriptionPeriod](./subscriptionperiod/everysixmonths.md)
- [static var everyThreeDays: Product.SubscriptionPeriod](./subscriptionperiod/everythreedays.md)
- [static var everyThreeMonths: Product.SubscriptionPeriod](./subscriptionperiod/everythreemonths.md)
- [static var everyTwoMonths: Product.SubscriptionPeriod](./subscriptionperiod/everytwomonths.md)
- [static var everyTwoWeeks: Product.SubscriptionPeriod](./subscriptionperiod/everytwoweeks.md)
- [static var monthly: Product.SubscriptionPeriod](./subscriptionperiod/monthly.md)
- [static var weekly: Product.SubscriptionPeriod](./subscriptionperiod/weekly.md)
- [static var yearly: Product.SubscriptionPeriod](./subscriptionperiod/yearly.md)
### Formatting the subscription period
- [func formatted<S>(S, referenceDate: Date) -> S.FormatOutput](./subscriptionperiod/formatted%28_,referencedate%29-3t7wd.md)
  Formats the subscription period using a format style that takes a date range as an input.
- [func formatted<S>(S, referenceDate: Date) -> S.FormatOutput](./subscriptionperiod/formatted%28_,referencedate%29-8s3ar.md)
  Formats the subscription period using a format style that takes a duration as an input.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting subscription information
- [let subscription: Product.SubscriptionInfo?](./subscription.md)
  The subscription information for an auto-renewable subscripton.
- [Product.SubscriptionInfo](./subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [Product.SubscriptionOffer](./subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
- [Product.SubscriptionInfo.Status](./subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiod)*