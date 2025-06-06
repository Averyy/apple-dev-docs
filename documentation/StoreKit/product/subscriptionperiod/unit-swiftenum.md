# Product.SubscriptionPeriod.Unit

**Framework**: StoreKit  
**Kind**: enum

Units of time that describe subscription periods.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum Unit
```

## Topics

### Getting the subscription period units
- [Product.SubscriptionPeriod.Unit.day](product/subscriptionperiod/unit-swift.enum/day.md)
  A subscription period unit of a day.
- [Product.SubscriptionPeriod.Unit.month](product/subscriptionperiod/unit-swift.enum/month.md)
  A subscription period unit of a month.
- [Product.SubscriptionPeriod.Unit.week](product/subscriptionperiod/unit-swift.enum/week.md)
  A subscription period unit of a week.
- [Product.SubscriptionPeriod.Unit.year](product/subscriptionperiod/unit-swift.enum/year.md)
  A subscription period unit of a year.
### Getting localized and debug descriptions
- [var localizedDescription: String](product/subscriptionperiod/unit-swift.enum/localizeddescription.md)
  The localized text that describes the subscription period unit.
### Getting the formatted description
- [func formatted<S>(S) -> S.FormatOutput](product/subscriptionperiod/unit-swift.enum/formatted(_:).md)
- [Product.SubscriptionPeriod.Unit.FormatStyle](product/subscriptionperiod/unit-swift.enum/formatstyle.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let value: Int](product/subscriptionperiod/value.md)
  The number of period units.
- [let unit: Product.SubscriptionPeriod.Unit](product/subscriptionperiod/unit-swift.property.md)
  The increment of time for the subscription period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiod/unit-swift.enum)*