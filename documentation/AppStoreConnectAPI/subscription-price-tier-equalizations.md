# Subscription price tier equalizations

**Framework**: App Store Connect API  
**Role**: API Collection

Calculate equalized volume pricing tiers for every territory from the tiers in your base territory.

## Overview

The `subscriptionPriceTierEqualizations` resource represents the volume pricing tiers for each territory that Apple calculates from a base territory’s tiers. Provide the base territory’s single-seat price point and the additional tiers you want, each with a minimum number of seats and a price point. Use it to:

- Convert a set of tiers in your base territory into equalized tiers for every other territory in one request.
- Get the price points that the equalized tiers use by including `priceTierPricePoints` in the response.

The request doesn’t save anything. It only calculates the equalized tiers. To apply them, create a price for each territory with [`Create a subscription price change`](./post-v1-subscriptionprices.md). For more information, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md).

> **Note**:  The response includes only the first 10 price points by default. Add `limit[priceTierPricePoints]` to return more.

## Topics

### Calculating equalized tiers
- [Create a subscription price tier equalization](./post-v1-subscriptionpricetierequalizations.md)
  Calculate equalized volume pricing tiers for every territory from a base territory’s tiers.
### Objects and types
- [object SubscriptionPriceTierEqualization](./subscriptionpricetierequalization.md)
  The equalized volume pricing tiers for each territory, calculated from a base territory’s tiers.
- [object SubscriptionPriceTierEqualizationCreateRequest](./subscriptionpricetierequalizationcreaterequest.md)
  The request body you use to create a subscription price tier equalization.
- [object SubscriptionPriceTierEqualizationResponse](./subscriptionpricetierequalizationresponse.md)
  The response body for endpoints that create a subscription price tier equalization.
- [object SubscriptionEqualizedPriceTiersForTerritory](./subscriptionequalizedpricetiersforterritory.md)
  The equalized volume pricing tiers for a single territory.
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
- [Subscription price change previews](./subscription-price-change-previews.md)
  Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.
- [Subscription images](./subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-price-tier-equalizations)*