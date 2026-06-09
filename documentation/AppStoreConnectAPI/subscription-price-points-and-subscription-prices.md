# Subscription Price Points and Subscription Prices

**Framework**: App Store Connect API

Manage scheduled price changes for auto-renewable subscriptions and get price point information.

## Topics

### Endpoints
- [Read subscription price point information](get-v1-subscriptionpricepoints-_id_.md)
  Get details about a specific subscription price point.
- [List all subscription price point equalizations](get-v1-subscriptionpricepoints-_id_-equalizations.md)
  Get a list of subscription price points and their equivalent in a specified currency.
- [List equalization IDs for a subscription price point](get-v1-subscriptionpricepoints-_id_-relationships-equalizations.md)
- [Create a subscription price change](post-v1-subscriptionprices.md)
  Schedule a subscription price change for a specific territory.
- [Delete subscription prices](delete-v1-subscriptionprices-_id_.md)
  Delete a scheduled price change for an auto-renewable subscription.
### Objects
- [object SubscriptionPricePointResponse](subscriptionpricepointresponse.md)
  The response body for endpoints that read a single subscription price point.
- [object SubscriptionPricePoint](subscriptionpricepoint.md)
  A standard price tier for auto-renewable subscriptions, defining the customer price and developer proceeds.
- [object SubscriptionPricePointsResponse](subscriptionpricepointsresponse.md)
  The response body for endpoints that list available price points for a subscription.
- [object SubscriptionPriceCreateRequest](subscriptionpricecreaterequest.md)
  The request body you use to create a subscription price.
- [object SubscriptionPriceInlineCreate](subscriptionpriceinlinecreate.md)
  An inline object for specifying a territory-specific subscription price within a price schedule.
- [object SubscriptionPriceResponse](subscriptionpriceresponse.md)
  The response body for endpoints that create a single subscription price.
- [object SubscriptionPricePointInlineCreate](subscriptionpricepointinlinecreate.md)
  An inline object for specifying a price point when creating a subscription pricing configuration.

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for your auto-renewalable subscription.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-price-points-and-subscription-prices)*