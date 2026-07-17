# Subscription Localizations

**Framework**: App Store Connect API

Create, modify, and delete localized metadata for auto-renewable subscriptions.

## Topics

### Endpoints
- [Create a subscription localization](post-v2-subscriptionlocalizations.md)
  Create a localized display name and description for an auto-renewable subscription configured with the v2 API.
- [Read subscription localization information](get-v2-subscriptionlocalizations-_id_.md)
  Get the display name and description for a specific locale of a subscription configured with the v2 API.
- [Modify a subscription localization](patch-v2-subscriptionlocalizations-_id_.md)
  Update the display name and description for a specific locale of a subscription configured with the v2 API.
- [Delete a subscription localization](delete-v2-subscriptionlocalizations-_id_.md)
  Delete a localized display name and description for a subscription configured with the v2 API.
### Objects
- [object SubscriptionLocalizationV2](subscriptionlocalizationv2.md)
  The localized display name and description for an auto-renewable subscription configured with the v2 API, shown to customers in a specific language.
- [object SubscriptionLocalizationV2CreateRequest](subscriptionlocalizationv2createrequest.md)
  The request body you use to create a subscription localization with the v2 API.
- [object SubscriptionLocalizationV2Response](subscriptionlocalizationv2response.md)
  The response body for endpoints that create, read, or modify a subscription localization with the v2 API.
- [object SubscriptionLocalizationV2UpdateRequest](subscriptionlocalizationv2updaterequest.md)
  The request body you use to update a subscription localization with the v2 API.
- [object SubscriptionLocalizationsV2Response](subscriptionlocalizationsv2response.md)
  The response body for endpoints that list subscription localizations configured with the v2 API.

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Querying adjusted subscription price equalizations](querying-adjusted-subscription-price-equalizations.md)
  Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.
- [Subscription Versions](subscription-versions.md)
  Create and read draft versions of an auto-renewable subscription, with their localized metadata and review images.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-localizations)*