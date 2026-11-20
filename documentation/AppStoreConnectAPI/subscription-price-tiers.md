# Subscription price tiers

**Framework**: App Store Connect API  
**Role**: API Collection

Read the volume pricing tiers that set a per-seat price from a minimum number of seats.

## Overview

The `subscriptionPriceTiers` resource represents one volume pricing tier of a subscription price. Each tier has a `minQuantity`, the lowest number of seats it applies to, and a relationship to the price point that sets its per-seat price. Use it to:

- Read the tiers of every price on a subscription in one request.
- Read the additional tiers of a single subscription price, along with each tier’s price point.
- Check the tiers you created with [`Create a subscription price change`](./post-v1-subscriptionprices.md).

You create tiers together with a price, not on their own. For more information, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md). Tiers don’t identify their territory, so add `filter[territory]` to a request to see which territory the results belong to.

> ❗ **Important**:  You can’t delete a price with tiers after it takes effect, and App Store Connect blocks you from unpreserving earlier prices while it exists. To remove the tiers and unpreserve earlier prices, see [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md).

## Topics

### Getting price tiers
- [List subscription price tiers](./get-v1-subscriptionpricetiers.md)
  List the volume pricing tiers for a subscription’s prices.
- [List additional price tiers for a subscription price](./get-v1-subscriptionprices-_id_-additionalpricetiers.md)
  List the additional volume pricing tiers for a subscription price.
- [List additional price tier IDs for a subscription price](./get-v1-subscriptionprices-_id_-relationships-additionalpricetiers.md)
  List the IDs of the additional volume pricing tiers for a subscription price.
### Objects and types
- [object SubscriptionPriceTier](./subscriptionpricetier.md)
  A volume pricing tier that sets a per-seat price from a minimum number of seats.
- [object SubscriptionPriceTierInlineCreate](./subscriptionpricetierinlinecreate.md)
  A volume pricing tier that you create inline with a subscription price.
- [object SubscriptionPriceTiersResponse](./subscriptionpricetiersresponse.md)
  The response body for endpoints that list subscription price tiers.
- [object SubscriptionPriceAdditionalPriceTiersLinkagesResponse](./subscriptionpriceadditionalpricetierslinkagesresponse.md)
  The response body for endpoints that list the IDs of a subscription price’s additional price tiers.

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
- [Subscription price tier equalizations](./subscription-price-tier-equalizations.md)
  Calculate equalized volume pricing tiers for every territory from the tiers in your base territory.
- [Subscription price change previews](./subscription-price-change-previews.md)
  Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.
- [Subscription images](./subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-price-tiers)*