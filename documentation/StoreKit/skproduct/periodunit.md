# SKProduct.PeriodUnit

**Framework**: StoreKit  
**Kind**: enum

Values representing the duration of an interval, from a day up to a year.

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
enum PeriodUnit
```

#### Overview

The period unit represents the duration of an interval. Period units are used with the number of units to determine one period in [`SKProductSubscriptionPeriod`](skproductsubscriptionperiod.md).

## Topics

### Period Units
- [SKProduct.PeriodUnit.day](skproduct/periodunit/day.md)
  An interval lasting one day.
- [SKProduct.PeriodUnit.month](skproduct/periodunit/month.md)
  An interval lasting one month.
- [SKProduct.PeriodUnit.week](skproduct/periodunit/week.md)
  An interval lasting one week.
- [SKProduct.PeriodUnit.year](skproduct/periodunit/year.md)
  An interval lasting one year.
### Initializers
- [init?(rawValue: UInt)](skproduct/periodunit/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var subscriptionGroupIdentifier: String?](skproduct/subscriptiongroupidentifier.md)
  The identifier of the subscription group to which the subscription belongs.
- [var subscriptionPeriod: SKProductSubscriptionPeriod?](skproduct/subscriptionperiod.md)
  The period details for products that are subscriptions.
- [class SKProductSubscriptionPeriod](skproductsubscriptionperiod.md)
  An object containing the subscription period duration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/periodunit)*