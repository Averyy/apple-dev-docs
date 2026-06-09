# Subscription Localizations

**Framework**: App Store Connect API

Create, modify, and delete localized metadata for auto-renewable subscriptions.

## Topics

### Endpoints
- [List all localizations for an auto-renewable subscription](get-v1-subscriptions-_id_-subscriptionlocalizations.md)
  Get a list of the subscription localizations for a specific auto-renewable subscription.
- [List localization IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-subscriptionlocalizations.md)
- [Read subscription localization information](get-v1-subscriptionlocalizations-_id_.md)
  Get the specific localized metadata for an auto-renewable subscription.
- [Create a subscription localization](post-v1-subscriptionlocalizations.md)
  Create a localized display name and description for an auto-renewable subscription.
- [Modify a subscription localization](patch-v1-subscriptionlocalizations-_id_.md)
  Update a specific localized subscription display name and description for an auto-renewable subscription.
- [Delete a subscription localization](delete-v1-subscriptionlocalizations-_id_.md)
  Delete localized metadata that you configured for an auto-renewable subscription.
### Objects
- [object SubscriptionLocalizationCreateRequest](subscriptionlocalizationcreaterequest.md)
  The request body you use to create a subscription localization.
- [object SubscriptionLocalizationUpdateRequest](subscriptionlocalizationupdaterequest.md)
  The request body you use to update a subscription localization update request.
- [object SubscriptionLocalizationResponse](subscriptionlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single subscription localization.
- [object SubscriptionLocalization](subscriptionlocalization.md)
  The localized display name and description for an auto-renewable subscription shown to customers on the App Store.

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Price Points and Subscription Prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for your auto-renewalable subscription.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-localizations)*