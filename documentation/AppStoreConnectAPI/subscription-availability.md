# Subscription availability

**Framework**: App Store Connect API  
**Role**: API Collection

Read and modify territory availability for an auto-renewable subscription.

## Topics

### Endpoints
- [Read the availability of a subscription](./get-v1-subscriptionavailabilities-_id_.md)
  Get information about the territory availability for a subscription.
- [List the territory availability of a subscription](./get-v1-subscriptionavailabilities-_id_-availableterritories.md)
  List the territory availability and currency of a specific subscription.
- [List available territory IDs for a subscription availability](./get-v1-subscriptionavailabilities-_id_-relationships-availableterritories.md)
- [Modify the territory availability of a subscription](./post-v1-subscriptionavailabilities.md)
  Update the territory availability of a specific subscription.
### Objects
- [object SubscriptionAvailability](./subscriptionavailability.md)
  The territory availability configuration for a subscription, specifying which App Store regions it’s offered in.
- [object SubscriptionAvailabilityCreateRequest](./subscriptionavailabilitycreaterequest.md)
  The request body you use to create a subscription availability.
- [object SubscriptionAvailabilityResponse](./subscriptionavailabilityresponse.md)
  A response containing a single territory availability configuration for a subscription.
- [object SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse](./subscriptionavailabilityavailableterritorieslinkagesresponse.md)

## See Also

### Managing Auto-Renewable Subscriptions
- [Managing auto-renewable subscriptions](./managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](./working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md)
  Schedule a single price to replace in-effect volume pricing, so you can unpreserve earlier subscriber prices in App Store Connect.
- [Querying adjusted subscription price equalizations](./querying-adjusted-subscription-price-equalizations.md)
  Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.
- [Configuring multiseat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md)
  Control whether organizations can purchase an auto-renewable subscription for multiple people, which markets offer it, and who hosts seat invitations.
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)
  Offer lower per-seat prices to groups and organizations that buy an auto-renewable subscription in larger quantities.
- [Subscription Versions](./subscription-versions.md)
  Create and read draft versions of an auto-renewable subscription, with their localized metadata and review images.
- [Subscriptions](./subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](./subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription localizations (v1)](./subscription-localizations-v1.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription price points and subscription prices](./subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription price tiers](./subscription-price-tiers.md)
  Read the volume pricing tiers that set a per-seat price from a minimum number of seats.
- [Subscription price tier equalizations](./subscription-price-tier-equalizations.md)
  Calculate equalized volume pricing tiers for every territory from the tiers in your base territory.
- [Subscription price change previews](./subscription-price-change-previews.md)
  Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-availability)*