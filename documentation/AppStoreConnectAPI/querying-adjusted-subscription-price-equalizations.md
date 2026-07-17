# Querying adjusted subscription price equalizations

**Framework**: App Store Connect API

Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.

#### Overview

Every subscription price point has a territory and a customer price. When you set a price in one territory, Apple can equalize equivalent price points across all other territories so customers see a consistent price relative to their local currency. The equalizations endpoint returns those matching price points. The adjusted equalizations endpoint returns the same set with adjustments applied for territories where the direct equalization would violate a local pricing rule — for example, a territory that requires rounded prices or that limits price bands.

Use the adjusted equalizations endpoint when you plan a price change and need to see the actual per-territory prices customers would pay, not the raw currency conversion.

##### Read Adjusted Equalizations for a Price Point

Use `GET /v1/subscriptionPricePoints/{id}/adjustedEqualizations` ([`List adjusted equalizations for a subscription price point`](get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md)) with the `id` of the source price point:

```other
GET /v1/subscriptionPricePoints/${sourcePricePointId}/adjustedEqualizations?include=territory&fields[subscriptionPricePoints]=customerPrice,territory
```

The response is a list of `SubscriptionPricePoints` — one per territory — where each price reflects the adjusted equalization for that territory. Compare each `customerPrice` against the source price to see where adjustments occur.

To read the raw equalizations without adjustments, use `GET /v1/subscriptionPricePoints/{id}/equalizations` ([`List all subscription price point equalizations`](get-v1-subscriptionpricepoints-_id_-equalizations.md)) with the same `id`. Compare the two responses to see which territories required an adjustment.

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Subscription Versions](subscription-versions.md)
  Create and read draft versions of an auto-renewable subscription, with their localized metadata and review images.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription localizations (v1)](subscription-localizations-v1.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription price points and subscription prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.
- [Subscription images (v1)](subscription-images-v1.md)
  Create, modify, and delete promotion images for your auto-renewable subscription.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/querying-adjusted-subscription-price-equalizations)*