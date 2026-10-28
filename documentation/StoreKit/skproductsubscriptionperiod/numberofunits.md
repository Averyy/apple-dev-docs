# numberOfUnits

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The number of units per subscription period.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionPeriod.

## Declaration

```swift
var numberOfUnits: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger numberOfUnits;
```

## Discussion

A subscription period duration is calculated by multiplying the number of units by the [`unit`](./unit.md).

For example, if the number of units is `3`, and the unit is [`SKProduct.PeriodUnit.month`](../skproduct/periodunit/month.md), the subscription period is 3 months.

## See Also

### Getting Subscription Period Details
- [var unit: SKProduct.PeriodUnit](./unit.md)
  The increment of time that a subscription period is specified in.
- [SKProduct.PeriodUnit](../skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod/numberofunits)*