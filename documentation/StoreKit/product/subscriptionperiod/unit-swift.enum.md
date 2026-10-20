# Product.SubscriptionPeriod.Unit

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Units of time that describe subscription periods.

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
enum Unit
```

## Topics

### Getting the subscription period units
- [Product.SubscriptionPeriod.Unit.day](./unit-swift.enum/day.md)
  A subscription period unit of a day.
- [Product.SubscriptionPeriod.Unit.month](./unit-swift.enum/month.md)
  A subscription period unit of a month.
- [Product.SubscriptionPeriod.Unit.week](./unit-swift.enum/week.md)
  A subscription period unit of a week.
- [Product.SubscriptionPeriod.Unit.year](./unit-swift.enum/year.md)
  A subscription period unit of a year.
### Getting localized and debug descriptions
- [var localizedDescription: String](./unit-swift.enum/localizeddescription.md)
  The localized text that describes the subscription period unit.
### Getting the formatted description
- [func formatted<S>(S) -> S.FormatOutput](./unit-swift.enum/formatted%28_%29.md)
- [Product.SubscriptionPeriod.Unit.FormatStyle](./unit-swift.enum/formatstyle.md)

## Relationships

### Conforms To
- [Comparable](../../../Swift/comparable.md)
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the subscription period
- [let value: Int](./value.md)
  The number of period units.
- [let unit: Product.SubscriptionPeriod.Unit](./unit-swift.property.md)
  The increment of time for the subscription period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptionperiod/unit-swift.enum)*