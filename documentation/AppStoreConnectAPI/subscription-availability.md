# Subscription availability

**Framework**: App Store Connect API

Read and modify territory availability for an auto-renewable subscription.

## Topics

### Endpoints
- [Read the availability of a subscription](get-v1-subscriptionavailabilities-_id_.md)
  Get information about the territory availability for a subscription.
- [List the territory availability of a subscription](get-v1-subscriptionavailabilities-_id_-availableterritories.md)
  List the territory availability and currency of a specific subscription.
- [List available territory IDs for a subscription availability](get-v1-subscriptionavailabilities-_id_-relationships-availableterritories.md)
- [Modify the territory availability of a subscription](post-v1-subscriptionavailabilities.md)
  Update the territory availability of a specific subscription.
### Objects
- [object SubscriptionAvailability](subscriptionavailability.md)
  The territory availability configuration for a subscription, specifying which App Store regions it’s offered in.
- [object SubscriptionAvailabilityCreateRequest](subscriptionavailabilitycreaterequest.md)
  The request body you use to create a subscription availability.
- [object SubscriptionAvailabilityResponse](subscriptionavailabilityresponse.md)
  A response containing a single territory availability configuration for a subscription.
- [object SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse](subscriptionavailabilityavailableterritorieslinkagesresponse.md)

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription Price Points and Subscription Prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for your auto-renewalable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-availability)*