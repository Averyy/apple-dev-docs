# SKProduct.PeriodUnit

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Values representing the duration of an interval, from a day up to a year.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionPeriod.Unit.

## Declaration

```swift
enum PeriodUnit
```

```c
enum SKProductPeriodUnit : NSUInteger;
```

## Overview

The period unit represents the duration of an interval. Period units are used with the number of units to determine one period in [`SKProductSubscriptionPeriod`](../skproductsubscriptionperiod.md).

## Topics

### Period Units
- [SKProduct.PeriodUnit.day](./periodunit/day.md)
  An interval lasting one day.
- [SKProduct.PeriodUnit.month](./periodunit/month.md)
  An interval lasting one month.
- [SKProduct.PeriodUnit.week](./periodunit/week.md)
  An interval lasting one week.
- [SKProduct.PeriodUnit.year](./periodunit/year.md)
  An interval lasting one year.
### Initializers
- [init?(rawValue: UInt)](./periodunit/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Subscription Information
- [var subscriptionGroupIdentifier: String?](./subscriptiongroupidentifier.md)
  The identifier of the subscription group to which the subscription belongs.
- [var subscriptionPeriod: SKProductSubscriptionPeriod?](./subscriptionperiod.md)
  The period details for products that are subscriptions.
- [class SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md)
  An object containing the subscription period duration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/periodunit)*