# numberOfPeriods

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An integer that indicates the number of periods the product discount is available.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.SubscriptionOffer.periodCount.

## Declaration

```swift
var numberOfPeriods: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger numberOfPeriods;
```

#### Discussion

A product discount may be available for one or more periods. The period, defined in [`subscriptionPeriod`](./subscriptionperiod.md), is a set number of days, weeks, months, or years.

The total length of time that a product discount is available is calculated by multiplying the [`numberOfPeriods`](./numberofperiods.md) by the period.

Note that the discount period is independent of the product subscription period.

## See Also

### Getting the Discount Duration
- [var subscriptionPeriod: SKProductSubscriptionPeriod](./subscriptionperiod.md)
  An object that defines the period for the product discount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproductdiscount/numberofperiods)*