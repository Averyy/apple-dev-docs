# Product.SubscriptionInfo

**Framework**: StoreKit  
**Kind**: struct

Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SubscriptionInfo
```

## Mentions

- [Choosing a StoreKit API for In-App Purchases](choosing-a-storekit-api-for-in-app-purchases.md)
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)

## Topics

### Determining the subscription status
- [var status: [Product.SubscriptionInfo.Status]](product/subscriptioninfo/status-swift.property.md)
  An array that contains status information for a subscription group, including renewal and transaction information.
- [static func status(for: String) async throws -> [Product.SubscriptionInfo.Status]](product/subscriptioninfo/status(for:).md)
  Gets the subscription status for a subscription group identifier.
- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.
### Identifying the subscription group
- [let subscriptionGroupID: String](product/subscriptioninfo/subscriptiongroupid.md)
  The subscription group identifier for this subscription.
- [var groupDisplayName: String](product/subscriptioninfo/groupdisplayname.md)
  The localized name of the subscription group, suitable for display.
- [var groupLevel: Int](product/subscriptioninfo/grouplevel.md)
  The rank of the subscription relative to other subscriptions in the same subscription group.
### Getting the subscription period
- [let subscriptionPeriod: Product.SubscriptionPeriod](product/subscriptioninfo/subscriptionperiod.md)
  The duration of time between subscription renewals.
- [Product.SubscriptionPeriod](product/subscriptionperiod.md)
  Values that represent the duration of time between subscription renewals.
### Getting introductory offer details
- [var isEligibleForIntroOffer: Bool](product/subscriptioninfo/iseligibleforintrooffer.md)
  A Boolean value that indicates whether the customer is eligible for an introductory offer.
- [static func isEligibleForIntroOffer(for: String) async -> Bool](product/subscriptioninfo/iseligibleforintrooffer(for:).md)
  Returns a Boolean value that determines the customer’s eligibility for an introductory offer within the provided subscription group.
- [let introductoryOffer: Product.SubscriptionOffer?](product/subscriptioninfo/introductoryoffer.md)
  Information about the introductory offer available for the auto-renewable subscription.
- [Product.SubscriptionOffer](product/subscriptionoffer.md)
  Information about a subscription offer that you configure in App Store Connect.
### Getting win-back offer details
- [let winBackOffers: [Product.SubscriptionOffer]](product/subscriptioninfo/winbackoffers.md)
  An array of available win-back offers for the auto-renewable subscription that you configured in App Store Connect.
### Getting promotional offer details
- [let promotionalOffers: [Product.SubscriptionOffer]](product/subscriptioninfo/promotionaloffers.md)
  An array of promotional offers available for the auto-renewable subscription.
### Structures
- [Product.SubscriptionInfo.RenewalInfo](product/subscriptioninfo/renewalinfo.md)
  The renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate.md)
  The renewal states of auto-renewable subscriptions.
### Type Methods
- [static func status(transactionID: UInt64) async throws -> SubscriptionStatus?](product/subscriptioninfo/status(transactionid:).md)
  Gets the subscription status for a transaction ID.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md)
  Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [struct Product](product.md)
  Information about a product that you configure in App Store Connect.
- [typealias SubscriptionInfo](subscriptioninfo.md)
  Information about an auto-renewable subscription.
- [typealias SubscriptionStatus](subscriptionstatus.md)
  Represents the renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo)*