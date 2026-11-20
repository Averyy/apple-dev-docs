# Subscription images

**Framework**: App Store Connect API  
**Role**: API Collection

Create, modify, and delete promotion images for auto-renewable subscriptions.

## Topics

### Endpoints
- [Create a subscription image](./post-v2-subscriptionimages.md)
  Reserve a promotion image for an auto-renewable subscription configured with the v2 API and prepare its asset upload.
- [Read subscription image information](./get-v2-subscriptionimages-_id_.md)
  Get the metadata for a subscription image configured with the v2 API, including the asset upload state.
- [Modify a subscription image](./patch-v2-subscriptionimages-_id_.md)
  Commit the asset upload for a subscription image configured with the v2 API.
- [Delete a subscription image](./delete-v2-subscriptionimages-_id_.md)
  Delete a subscription image configured with the v2 API.
### Objects
- [object SubscriptionImageV2](./subscriptionimagev2.md)
  A promotion image attached to an auto-renewable subscription configured with the v2 API.
- [object SubscriptionImageV2CreateRequest](./subscriptionimagev2createrequest.md)
  The request body you use to create a subscription image with the v2 API.
- [object SubscriptionImageV2Response](./subscriptionimagev2response.md)
  The response body for endpoints that create, read, or modify a subscription image with the v2 API.
- [object SubscriptionImageV2UpdateRequest](./subscriptionimagev2updaterequest.md)
  The request body you use to commit an upload for a subscription image with the v2 API.
- [object SubscriptionImagesV2Response](./subscriptionimagesv2response.md)
  The response body for endpoints that list subscription images configured with the v2 API.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-images)*