# Subscription price points and subscription prices

**Framework**: App Store Connect API  
**Role**: API Collection

Manage scheduled price changes for auto-renewable subscriptions and get price point information.

## Overview

You can delete a scheduled price, but not one that’s already in effect. To remove tiers from a price that’s in effect, see [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md).

## Overview

A subscription’s price in a territory combines a price point, which is a specific price in that territory’s currency, with a start date. To set a price, find the price point you want, then create a price that references the subscription and the price point by using [`Create a subscription price change`](./post-v1-subscriptionprices.md). Set a `startDate` to schedule the price to take effect on a future date. To cancel a scheduled price change before it takes effect, use [`Delete subscription prices`](./delete-v1-subscriptionprices-_id_.md). Before you schedule a change to a price that has subscribers, preview its effect on them. For a walkthrough of setting prices across territories, see [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md). To learn how price increases affect subscribers, see [Understanding subscription price increase notice and consent](./understanding-price-increase-notice-and-consent.md).

## Volume pricing

Volume pricing lets you charge less per seat as the number of seats in a subscription grows. When a group or organization buys your auto-renewable subscription for multiple people, you can add volume pricing tiers to the subscription’s price in each territory. Each tier covers a range of seats and has its own per-seat price, and each tier costs less per seat than the one before it. A subscription can have up to five tiers, counting the single-seat price as Tier 1. The single-seat price doesn’t change, so you add tiers only for quantities of 2 or more, and customers pay the price of the tier each seat falls into. The same tiers apply whether customers buy through the App Store, [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/), or [Apple School Manager](https://support.apple.com/guide/apple-school-manager/). Volume pricing tiers are optional.

Customers can use tiers only when they can buy more than one seat of your subscription. Multiseat purchasing is on by default for existing and newly created subscriptions, but you can opt out. You can add and edit tiers whether or not multiseat purchasing is on. If you turn it off, new customers can’t buy more than one seat, and existing multiseat subscribers keep renewing at their current seat count and tier prices. Volume pricing is available only for subscriptions billed up front. A Paid Monthly billing plan is available only for single-seat subscriptions. To turn multiseat purchasing on or off and choose the markets that offer it, see [Configuring multiseat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md). To add tiers to a price, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md). For more information on configuring prices for your subscriptions, see [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md).

> ❗ **Important**:  App Store Connect doesn’t support volume pricing. After you add volume pricing tiers to a subscription, you can manage that subscription’s prices, including its single-seat price, only through the App Store Connect API. To manage its prices in App Store Connect again, remove every additional tier in every territory so that only the single-seat price remains. For a live subscription, removing tiers is a scheduled price change, so you can use App Store Connect again after the change takes effect. Because customers with multiple seats lose their volume discount, the change can raise their price, and you can choose whether to preserve their current price. If you never added volume pricing through the API, you can keep managing the subscription’s prices in App Store Connect.

## Topics

### Configuring prices and volume pricing
- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Configuring multiseat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md)
  Control whether organizations can purchase an auto-renewable subscription for multiple people, which markets offer it, and who hosts seat invitations.
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)
  Offer lower per-seat prices to groups and organizations that buy an auto-renewable subscription in larger quantities.
- [Understanding subscription price increase notice and consent](./understanding-price-increase-notice-and-consent.md)
  Learn when Apple notifies subscribers of a price increase and asks for their consent, and how to keep existing subscribers on their current price.
### Reading and managing subscription price points and prices
- [Read subscription price point information](./get-v1-subscriptionpricepoints-_id_.md)
  Get details about a specific subscription price point.
- [List all subscription price point equalizations](./get-v1-subscriptionpricepoints-_id_-equalizations.md)
  Get a list of subscription price points and their equivalent in a specified currency.
- [List equalization IDs for a subscription price point](./get-v1-subscriptionpricepoints-_id_-relationships-equalizations.md)
- [List adjusted equalizations for a subscription price point](./get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md)
  List the adjusted territory equalizations for a subscription price point.
- [Create a subscription price change](./post-v1-subscriptionprices.md)
  Schedule a subscription price change for a specific territory.
- [Delete subscription prices](./delete-v1-subscriptionprices-_id_.md)
  Delete a scheduled price change for an auto-renewable subscription.
### Objects and types
- [object SubscriptionPricePointResponse](./subscriptionpricepointresponse.md)
  The response body for endpoints that read a single subscription price point.
- [object SubscriptionPricePoint](./subscriptionpricepoint.md)
  A standard price tier for auto-renewable subscriptions, defining the customer price and developer proceeds.
- [object SubscriptionPricePointsResponse](./subscriptionpricepointsresponse.md)
  The response body for endpoints that list available price points for a subscription.
- [object SubscriptionPriceCreateRequest](./subscriptionpricecreaterequest.md)
  The request body you use to create a subscription price.
- [object SubscriptionPriceInlineCreate](./subscriptionpriceinlinecreate.md)
  An inline object for specifying a territory-specific subscription price within a price schedule.
- [object SubscriptionPriceResponse](./subscriptionpriceresponse.md)
  The response body for endpoints that create a single subscription price.
- [object SubscriptionPricePointInlineCreate](./subscriptionpricepointinlinecreate.md)
  An inline object for specifying a price point when creating a subscription pricing configuration.

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
- [Subscription price tiers](./subscription-price-tiers.md)
  Read the volume pricing tiers that set a per-seat price from a minimum number of seats.
- [Subscription price tier equalizations](./subscription-price-tier-equalizations.md)
  Calculate equalized volume pricing tiers for every territory from the tiers in your base territory.
- [Subscription price change previews](./subscription-price-change-previews.md)
  Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.
- [Subscription images](./subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-price-points-and-subscription-prices)*