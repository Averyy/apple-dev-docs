# unit

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The increment of time that a subscription period is specified in.

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
var unit: SKProduct.PeriodUnit { get }
```

```objc
@property (nonatomic, readonly) SKProductPeriodUnit unit;
```

## Discussion

The units used to specify a subscription period include day, week, month, and year, as defined in [`SKProduct.PeriodUnit`](../skproduct/periodunit.md).

To calculate the duration of one subscription period, multiply the [`unit`](./unit.md) by the number of units ([`numberOfUnits`](./numberofunits.md)).

## See Also

### Getting Subscription Period Details
- [var numberOfUnits: Int](./numberofunits.md)
  The number of units per subscription period.
- [SKProduct.PeriodUnit](../skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod/unit)*