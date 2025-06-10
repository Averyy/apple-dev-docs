# Billing Grace Periods

**Framework**: App Store Connect API

Get information about the grace period and modify the opt-in value.

## Topics

### Endpoints
- [Read the Billing Grace Period Value for an App](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [GET /v1/apps/{id}/relationships/subscriptionGracePeriod](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [Read the Billing Grace Period Value](get-v1-subscriptiongraceperiods-_id_.md)
  Get the Boolean value that represents the billing grace period opt-in state and the duration of the billing grace period.
- [Modify the Billing Grace Period Opt-in Status and Duration](patch-v1-subscriptiongraceperiods-_id_.md)
  Change the Boolean value representing the billing grace period opt-in status.
### Object
- [type SubscriptionGracePeriodDuration](subscriptiongraceperiodduration.md)
- [object SubscriptionGracePeriodResponse](subscriptiongraceperiodresponse.md)
- [object SubscriptionGracePeriod](subscriptiongraceperiod.md)
- [object SubscriptionGracePeriodUpdateRequest](subscriptiongraceperiodupdaterequest.md)
- [object AppSubscriptionGracePeriodLinkageResponse](appsubscriptiongraceperiodlinkageresponse.md)

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
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/billing-grace-periods)*