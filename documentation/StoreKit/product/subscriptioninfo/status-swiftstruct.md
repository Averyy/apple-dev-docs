# Product.SubscriptionInfo.Status

**Framework**: StoreKit  
**Kind**: struct

The renewal status information for an auto-renewable subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Status
```

## Mentions

- [Choosing a StoreKit API for In-App Purchases](choosing-a-storekit-api-for-in-app-purchases.md)

#### Overview

The subscription status provides renewal information signed by the App Store for subscriptions that a customer purchases.

## Topics

### Monitoring subscription status changes
- [static var updates: Product.SubscriptionInfo.Status.Statuses](product/subscriptioninfo/status-swift.struct/updates.md)
  The asynchronous sequence that emits status information when a subscription’s status changes.
- [static var all: AsyncStream<(groupID: String, statuses: [Product.SubscriptionInfo.Status])>](product/subscriptioninfo/status-swift.struct/all.md)
- [Product.SubscriptionInfo.Status.Statuses](product/subscriptioninfo/status-swift.struct/statuses.md)
  An asynchronous sequence that listens for new subscription status information.
### Getting subscription status information
- [let state: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let renewalInfo: VerificationResult<Product.SubscriptionInfo.RenewalInfo>](product/subscriptioninfo/status-swift.struct/renewalinfo.md)
  The signed renewal information for the auto-renewable subscription.
- [let transaction: VerificationResult<Transaction>](product/subscriptioninfo/status-swift.struct/transaction.md)
  The latest transaction for the subscription group.
- [Product.SubscriptionInfo.RenewalInfo](product/subscriptioninfo/renewalinfo.md)
  The renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate.md)
  The renewal states of auto-renewable subscriptions.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Product.SubscriptionInfo.RenewalInfo](product/subscriptioninfo/renewalinfo.md)
  The renewal information for an auto-renewable subscription.
- [typealias SubscriptionRenewalInfo](subscriptionrenewalinfo.md)
  Represents the renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionRenewalState](subscriptionrenewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionPeriod](subscriptionperiod.md)
  Represents the duration of time between subscription renewals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct)*