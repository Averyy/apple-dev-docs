# subscriptionPeriod

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The period details for products that are subscriptions.

**Availability**:
- iOS 11.2+ - Deprecated in 18.0
- iPadOS 11.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.13.2+ - Deprecated in 15.0
- tvOS 11.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.subscription.subscriptionPeriod.

## Declaration

```swift
var subscriptionPeriod: SKProductSubscriptionPeriod? { get }
```

```objc
@property (nonatomic, readonly, nullable) SKProductSubscriptionPeriod * subscriptionPeriod;
```

## Discussion

This read-only property is `nil` if the product is not a subscription.

A subscription period is described in terms of a unit and the number of units that make up a single period.

## See Also

### Getting Subscription Information
- [var subscriptionGroupIdentifier: String?](./subscriptiongroupidentifier.md)
  The identifier of the subscription group to which the subscription belongs.
- [class SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md)
  An object containing the subscription period duration information.
- [SKProduct.PeriodUnit](./periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/subscriptionperiod)*