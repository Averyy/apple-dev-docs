# SKProductSubscriptionPeriod

**Framework**: StoreKit  
**Kind**: class

An object containing the subscription period duration information.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class SKProductSubscriptionPeriod
```

#### Overview

A subscription period is a duration of time defined as some number of units, where a unit can be a [`SKProduct.PeriodUnit.day`](skproduct/periodunit/day.md), [`SKProduct.PeriodUnit.week`](skproduct/periodunit/week.md), [`SKProduct.PeriodUnit.month`](skproduct/periodunit/month.md), or [`SKProduct.PeriodUnit.year`](skproduct/periodunit/year.md).

For example, a subscription period of two weeks has a [`unit`](skproductsubscriptionperiod/unit.md) of a [`SKProduct.PeriodUnit.week`](skproduct/periodunit/week.md), and a  [`numberOfUnits`](skproductsubscriptionperiod/numberofunits.md) equal to `2`.

## Topics

### Getting Subscription Period Details
- [var numberOfUnits: Int](skproductsubscriptionperiod/numberofunits.md)
  The number of units per subscription period.
- [var unit: SKProduct.PeriodUnit](skproductsubscriptionperiod/unit.md)
  The increment of time that a subscription period is specified in.
- [SKProduct.PeriodUnit](skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var subscriptionGroupIdentifier: String?](skproduct/subscriptiongroupidentifier.md)
  The identifier of the subscription group to which the subscription belongs.
- [var subscriptionPeriod: SKProductSubscriptionPeriod?](skproduct/subscriptionperiod.md)
  The period details for products that are subscriptions.
- [SKProduct.PeriodUnit](skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod)*