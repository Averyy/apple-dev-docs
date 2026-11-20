# Subscription localizations (v1)

**Framework**: App Store Connect API  
**Role**: API Collection

Create, modify, and delete localized metadata for auto-renewable subscriptions.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

## Overview

> ❗ **Important**:  This is deprecated. Use [Subscription Localizations](./subscription-localizations.md) instead.

## Topics

### Endpoints
- [List all localizations for an auto-renewable subscription](./get-v1-subscriptions-_id_-subscriptionlocalizations.md)
  Get a list of the subscription localizations for a specific auto-renewable subscription.
- [List localization IDs for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-subscriptionlocalizations.md)
- [Read subscription localization information (v1)](./get-v1-subscriptionlocalizations-_id_.md)
  Get the specific localized metadata for an auto-renewable subscription.
- [Create a subscription localization (v1)](./post-v1-subscriptionlocalizations.md)
  Create a localized display name and description for an auto-renewable subscription.
- [Modify a subscription localization (v1)](./patch-v1-subscriptionlocalizations-_id_.md)
  Update a specific localized subscription display name and description for an auto-renewable subscription.
- [Delete a subscription localization (v1)](./delete-v1-subscriptionlocalizations-_id_.md)
  Delete localized metadata that you configured for an auto-renewable subscription.
### Objects
- [object SubscriptionLocalizationCreateRequest](./subscriptionlocalizationcreaterequest.md)
  The request body you use to create a subscription localization.
- [object SubscriptionLocalizationUpdateRequest](./subscriptionlocalizationupdaterequest.md)
  The request body you use to update a subscription localization update request.
- [object SubscriptionLocalizationResponse](./subscriptionlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single subscription localization.
- [object SubscriptionLocalization](./subscriptionlocalization.md)
  The localized display name and description for an auto-renewable subscription shown to customers on the App Store.

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
- [Subscription price points and subscription prices](./subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription price tiers](./subscription-price-tiers.md)
  Read the volume pricing tiers that set a per-seat price from a minimum number of seats.
- [Subscription price tier equalizations](./subscription-price-tier-equalizations.md)
  Calculate equalized volume pricing tiers for every territory from the tiers in your base territory.
- [Subscription price change previews](./subscription-price-change-previews.md)
  Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.
- [Subscription images](./subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-localizations-v1)*