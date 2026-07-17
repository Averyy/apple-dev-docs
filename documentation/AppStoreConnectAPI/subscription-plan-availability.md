# Subscription plan availability

**Framework**: App Store Connect API

Create and manage subscription plan availability for auto-renewable subscriptions.

#### Overview

The `subscriptionPlanAvailabilities` resource lets you control which subscription plan type — monthly or up-front — is available for a subscription in specific territories.

There are two possible values for the subscription plan type: `MONTHLY` and `UPFRONT`. To learn more, see [`SubscriptionPlanType`](subscriptionplantype.md) and [`Set availability for an auto-renewable subscription`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription).

Use it to:

- Create a plan availability configuration for a subscription.
- Read or modify the available territories for a plan availability.
- Update available territories for a subscription plan availability.

## Topics

### Creating and modifying plan availability
- [Create a subscription plan availability](post-v1-subscriptionplanavailabilities.md)
  Create the plan availability configuration for an auto-renewable subscription.
- [Read subscription plan availability information](get-v1-subscriptionplanavailabilities-_id_.md)
  Get information about a specific subscription plan availability.
- [Modify a subscription plan availability](patch-v1-subscriptionplanavailabilities-_id_.md)
  Update the plan availability configuration for a specific subscription.
### Managing available territories
- [List available territories for a subscription plan availability](get-v1-subscriptionplanavailabilities-_id_-availableterritories.md)
  List all territories where a specific subscription plan is available.
- [List available territory IDs for a subscription plan availability](get-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Get a list of available territory resource IDs for a specific subscription plan availability.
- [Replace the available territories for a subscription plan availability](patch-v1-subscriptionplanavailabilities-_id_-relationships-availableterritories.md)
  Replace the list of available territories for a specific subscription plan availability.
### Reading plan availability from a subscription
- [List plan availabilities for a subscription](get-v1-subscriptions-_id_-planavailabilities.md)
  List all plan availabilities for a specific auto-renewable subscription.
- [List plan availability IDs for a subscription](get-v1-subscriptions-_id_-relationships-planavailabilities.md)
  Get a list of plan availability resource IDs for a specific auto-renewable subscription.
### Objects and types
- [object SubscriptionPlanAvailability](subscriptionplanavailability.md)
  A configuration object for a subscription’s plan availability, specifying the plan type, the territories in which it is available, and whether it’s automatically available in new territories.
- [object SubscriptionPlanAvailabilityCreateRequest](subscriptionplanavailabilitycreaterequest.md)
  The request body you use to create a subscription plan availability.
- [object SubscriptionPlanAvailabilityUpdateRequest](subscriptionplanavailabilityupdaterequest.md)
  The request body you use to modify a subscription plan availability.
- [object SubscriptionPlanAvailabilityResponse](subscriptionplanavailabilityresponse.md)
  The response body for endpoints that create or read a single subscription plan availability.
- [object SubscriptionPlanAvailabilitiesResponse](subscriptionplanavailabilitiesresponse.md)
  The response body for endpoints that list subscription plan availabilities.
- [object SubscriptionPlanAvailabilitiesLinkagesResponse](subscriptionplanavailabilitieslinkagesresponse.md)
  A response containing the resource identifiers of subscription plan availabilities.
- [object SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesRequest](subscriptionplanavailabilityavailableterritorieslinkagesrequest.md)
  A request body you use to replace the available territories for a subscription plan availability.
- [object SubscriptionPlanAvailabilityAvailableTerritoriesLinkagesResponse](subscriptionplanavailabilityavailableterritorieslinkagesresponse.md)
  A response containing the resource identifiers of available territories for a subscription plan availability.
- [type SubscriptionPlanType](subscriptionplantype.md)
  A string that indicates the billing plan type for an auto-renewable subscription.

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
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-plan-availability)*