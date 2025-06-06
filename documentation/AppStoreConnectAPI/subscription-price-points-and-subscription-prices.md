# Subscription Price Points and Subscription Prices

**Framework**: App Store Connect API

Manage scheduled price changes for auto-renewable subscriptions and get price point information.

## Topics

### Endpoints
- [Read Subscription Price Point Information](get-v1-subscriptionpricepoints-_id_.md)
  Get details about a specific subscription price point.
- [List All Subscription Price Point Equalizations](get-v1-subscriptionpricepoints-_id_-equalizations.md)
  Get a list of subscription price points and their equivalent in a specified currency.
- [Create a Subscription Price Change](post-v1-subscriptionprices.md)
  Schedule a subscription price change for a specific territory.
- [Delete Subscription Prices](delete-v1-subscriptionprices-_id_.md)
  Delete a scheduled price change for an auto-renewable subscription.
### Objects
- [object SubscriptionPricePointResponse](subscriptionpricepointresponse.md)
- [object SubscriptionPricePoint](subscriptionpricepoint.md)
- [object SubscriptionPricePointsResponse](subscriptionpricepointsresponse.md)
- [object SubscriptionPriceCreateRequest](subscriptionpricecreaterequest.md)
- [object SubscriptionPriceInlineCreate](subscriptionpriceinlinecreate.md)
- [object SubscriptionPriceResponse](subscriptionpriceresponse.md)
- [object SubscriptionPricePointInlineCreate](subscriptionpricepointinlinecreate.md)

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
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-price-points-and-subscription-prices)*