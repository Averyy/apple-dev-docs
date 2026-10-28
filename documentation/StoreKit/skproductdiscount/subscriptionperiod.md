# subscriptionPeriod

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An object that defines the period for the product discount.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionOffer.period.

## Declaration

```swift
var subscriptionPeriod: SKProductSubscriptionPeriod { get }
```

```objc
@property (nonatomic, readonly) SKProductSubscriptionPeriod * subscriptionPeriod;
```

## Discussion

This object represents the duration of a single subscription period. A period is described as a number of units, where a unit can be a [`SKProduct.PeriodUnit.day`](../skproduct/periodunit/day.md), [`SKProduct.PeriodUnit.month`](../skproduct/periodunit/month.md), [`SKProduct.PeriodUnit.week`](../skproduct/periodunit/week.md), or [`SKProduct.PeriodUnit.year`](../skproduct/periodunit/year.md).

To calculate the total amount of time that the discount price is available to the user, multiply the [`subscriptionPeriod`](./subscriptionperiod.md) by [`numberOfPeriods`](./numberofperiods.md).

> **Note**:  The subscription period for the discount is independent of the product’s regular subscription period, and does not have to match in units or duration.

## See Also

### Getting the Discount Duration
- [var numberOfPeriods: Int](./numberofperiods.md)
  An integer that indicates the number of periods the product discount is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/subscriptionperiod)*