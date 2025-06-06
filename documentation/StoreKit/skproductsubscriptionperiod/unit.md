# unit

**Framework**: StoreKit  
**Kind**: property

The increment of time that a subscription period is specified in.

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
var unit: SKProduct.PeriodUnit { get }
```

#### Discussion

The units used to specify a subscription period include day, week, month, and year, as defined in [`SKProduct.PeriodUnit`](skproduct/periodunit.md).

To calculate the duration of one subscription period, multiply the [`unit`](skproductsubscriptionperiod/unit.md) by the number of units ([`numberOfUnits`](skproductsubscriptionperiod/numberofunits.md)).

## See Also

- [var numberOfUnits: Int](skproductsubscriptionperiod/numberofunits.md)
  The number of units per subscription period.
- [SKProduct.PeriodUnit](skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductsubscriptionperiod/unit)*