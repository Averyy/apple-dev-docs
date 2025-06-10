# Product.SubscriptionInfo.RenewalState

**Framework**: StoreKit  
**Kind**: struct

The renewal states of auto-renewable subscriptions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct RenewalState
```

## Mentions

- [Testing failing subscription renewals and In-App Purchases](testing-failing-subscription-renewals-and-in-app-purchases.md)
- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)

#### Overview

A subscription’s renewal state indicates whether an auto-renewable subscription is entitled to service. Subscriptions in the [`subscribed`](product/subscriptioninfo/renewalstate/subscribed.md) and [`inGracePeriod`](product/subscriptioninfo/renewalstate/ingraceperiod.md) states are entitled to service.

Subscriptions in the [`expired`](product/subscriptioninfo/renewalstate/expired.md), [`inBillingRetryPeriod`](product/subscriptioninfo/renewalstate/inbillingretryperiod.md), and [`revoked`](product/subscriptioninfo/renewalstate/revoked.md) states aren’t entitled to service if the customer doesn’t have other [`Product.SubscriptionInfo.Status`](product/subscriptioninfo/status-swift.struct.md) items that give them entitlement to service for that subscription. For example, a customer may have a status in the [`expired`](product/subscriptioninfo/renewalstate/expired.md) state for a subscription that they purchased individually, and another status in the [`subscribed`](product/subscriptioninfo/renewalstate/subscribed.md) state for the same subscription, which they get through Family Sharing. In that case, the customer has an entitlement to service for that subscription.

For more information about Family Sharing, see [`Supporting Family Sharing in your app`](supporting-family-sharing-in-your-app.md). For more information about entitlements, see [`currentEntitlements`](transaction/currententitlements.md).

## Topics

### Getting the renewal state
- [static let subscribed: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate/subscribed.md)
  The customer is currently subscribed.
- [static let expired: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate/expired.md)
  The subscription expired.
- [static let inBillingRetryPeriod: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate/inbillingretryperiod.md)
  The subscription is in a billing retry period.
- [static let inGracePeriod: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate/ingraceperiod.md)
  The subscription is in a billing grace period state.
- [static let revoked: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate/revoked.md)
  The App Store has revoked the customer’s access to the subscription group.
### Getting a localized description
- [var localizedDescription: String](product/subscriptioninfo/renewalstate/localizeddescription.md)
  A string containing the localized description of the renewal state.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalInfo](product/subscriptioninfo/renewalinfo.md)
  The renewal information for an auto-renewable subscription.
- [typealias SubscriptionRenewalInfo](subscriptionrenewalinfo.md)
  Represents the renewal information for an auto-renewable subscription.
- [typealias SubscriptionRenewalState](subscriptionrenewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionPeriod](subscriptionperiod.md)
  Represents the duration of time between subscription renewals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalstate)*