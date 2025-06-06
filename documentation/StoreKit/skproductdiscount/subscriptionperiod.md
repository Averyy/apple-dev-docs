# subscriptionPeriod

**Framework**: Storekit  
**Kind**: property

An object that defines the period for the product discount.

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
var subscriptionPeriod: SKProductSubscriptionPeriod { get }
```

#### Discussion

This object represents the duration of a single subscription period. A period is described as a number of units, where a unit can be a [`SKProduct.PeriodUnit.day`](skproduct/periodunit/day.md), [`SKProduct.PeriodUnit.month`](skproduct/periodunit/month.md), [`SKProduct.PeriodUnit.week`](skproduct/periodunit/week.md), or [`SKProduct.PeriodUnit.year`](skproduct/periodunit/year.md).

To calculate the total amount of time that the discount price is available to the user, multiply the [`subscriptionPeriod`](skproductdiscount/subscriptionperiod.md) by [`numberOfPeriods`](skproductdiscount/numberofperiods.md).

> **Note**:  The subscription period for the discount is independent of the product’s regular subscription period, and does not have to match in units or duration.

## See Also

- [var numberOfPeriods: Int](skproductdiscount/numberofperiods.md)
  An integer that indicates the number of periods the product discount is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/subscriptionperiod)*