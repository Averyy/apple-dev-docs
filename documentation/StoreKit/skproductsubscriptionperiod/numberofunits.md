# numberOfUnits

**Framework**: StoreKit  
**Kind**: property

The number of units per subscription period.

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
var numberOfUnits: Int { get }
```

#### Discussion

A subscription period duration is calculated by multiplying the number of units by the [`unit`](skproductsubscriptionperiod/unit.md).

For example, if the number of units is `3`, and the unit is [`SKProduct.PeriodUnit.month`](skproduct/periodunit/month.md), the subscription period is 3 months.

## See Also

- [var unit: SKProduct.PeriodUnit](skproductsubscriptionperiod/unit.md)
  The increment of time that a subscription period is specified in.
- [SKProduct.PeriodUnit](skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod/numberofunits)*