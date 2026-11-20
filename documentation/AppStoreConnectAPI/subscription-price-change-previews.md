# Subscription price change previews

**Framework**: App Store Connect API  
**Role**: API Collection

Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.

## Overview

The `subscriptionPriceChangePreviews` resource represents the result of comparing a subscription’s current price with a price you propose, in each territory you include. Use it to:

- Propose a start date, a single-seat price point, and volume pricing tiers for one or more territories.
- Find out how each proposed change affects existing subscribers, as a `changeType` of `INCREASE_PRESERVABLE`, `DECREASE_NOT_PRESERVABLE`, `MIXED_NOT_PRESERVABLE`, or `NO_CHANGE`.
- Decide whether to set `preserveCurrentPrice` when you create the price with [`Create a subscription price change`](./post-v1-subscriptionprices.md).

The request doesn’t change any prices. For more information about price changes and how they affect existing subscribers, see [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md) and [Understanding subscription price increase notice and consent](./understanding-price-increase-notice-and-consent.md).

> **Note**:  Preview a change before you schedule it. After a price change takes effect, you can’t delete it, but you can schedule a new price.

## Topics

### Previewing price changes
- [Create a subscription price change preview](./post-v1-subscriptionpricechangepreviews.md)
  Preview how proposed subscription prices, including volume pricing tiers, change what existing subscribers pay.
### Objects and types
- [object SubscriptionPriceChangePreview](./subscriptionpricechangepreview.md)
  The result of previewing a subscription price change in each proposed territory.
- [object SubscriptionPriceChangePreviewCreateRequest](./subscriptionpricechangepreviewcreaterequest.md)
  The request body you use to create a subscription price change preview.
- [object SubscriptionPriceChangePreviewResponse](./subscriptionpricechangepreviewresponse.md)
  The response body for endpoints that create a subscription price change preview.
- [object ProposedSubscriptionPriceTier](./proposedsubscriptionpricetier.md)
  A volume pricing tier that you propose for a territory.

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
- [Subscription images](./subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-price-change-previews)*