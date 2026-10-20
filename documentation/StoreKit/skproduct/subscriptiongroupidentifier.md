# subscriptionGroupIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The identifier of the subscription group to which the subscription belongs.

**Availability**:
- iOS 12.0+ - Deprecated in 18.0
- iPadOS 12.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- tvOS 12.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.subscription.subscriptionGroupID.

## Declaration

```swift
var subscriptionGroupIdentifier: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * subscriptionGroupIdentifier;
```

## Mentions

- [Handling Subscriptions Billing](../handling-subscriptions-billing.md)

#### Discussion

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [Offer auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev75708c031).

This property is `nil` if the [`SKProduct`](../skproduct.md) isn’t an auto-renewable subscription.

## See Also

### Getting Subscription Information
- [var subscriptionPeriod: SKProductSubscriptionPeriod?](./subscriptionperiod.md)
  The period details for products that are subscriptions.
- [class SKProductSubscriptionPeriod](../skproductsubscriptionperiod.md)
  An object containing the subscription period duration information.
- [SKProduct.PeriodUnit](./periodunit.md)
  Values representing the duration of an interval, from a day up to a year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skproduct/subscriptiongroupidentifier)*