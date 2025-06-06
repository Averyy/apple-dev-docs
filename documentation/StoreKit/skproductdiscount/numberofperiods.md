# numberOfPeriods

**Framework**: StoreKit  
**Kind**: property

An integer that indicates the number of periods the product discount is available.

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
var numberOfPeriods: Int { get }
```

#### Discussion

A product discount may be available for one or more periods. The period, defined in [`subscriptionPeriod`](skproductdiscount/subscriptionperiod.md), is a set number of days, weeks, months, or years.

The total length of time that a product discount is available is calculated by multiplying the [`numberOfPeriods`](skproductdiscount/numberofperiods.md) by the period.

Note that the discount period is independent of the product subscription period.

## See Also

- [var subscriptionPeriod: SKProductSubscriptionPeriod](skproductdiscount/subscriptionperiod.md)
  An object that defines the period for the product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/numberofperiods)*