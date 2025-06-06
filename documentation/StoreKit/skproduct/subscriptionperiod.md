# subscriptionPeriod

**Framework**: StoreKit  
**Kind**: property

The period details for products that are subscriptions.

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
var subscriptionPeriod: SKProductSubscriptionPeriod? { get }
```

#### Discussion

This read-only property is `nil` if the product is not a subscription.

A subscription period is described in terms of a unit and the number of units that make up a single period.

## See Also

- [var subscriptionGroupIdentifier: String?](skproduct/subscriptiongroupidentifier.md)
  The identifier of the subscription group to which the subscription belongs.
- [class SKProductSubscriptionPeriod](skproductsubscriptionperiod.md)
  An object containing the subscription period duration information.
- [SKProduct.PeriodUnit](skproduct/periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/subscriptionperiod)*