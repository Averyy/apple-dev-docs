# Billing Grace Periods

**Framework**: App Store Connect API  
**Role**: API Collection

Get information about the grace period and modify the opt-in value.

## Topics

### Endpoints
- [Read the billing grace period value for an app](./get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [Get the subscription grace period ID for an app](./get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [Read the billing grace period value](./get-v1-subscriptiongraceperiods-_id_.md)
  Get the Boolean value that represents the billing grace period opt-in state and the duration of the billing grace period.
- [Modify the billing grace period opt-in status and duration](./patch-v1-subscriptiongraceperiods-_id_.md)
  Change the Boolean value representing the billing grace period opt-in status.
### Object
- [type SubscriptionGracePeriodDuration](./subscriptiongraceperiodduration.md)
  A string that represents the grace period duration for a subscription.
- [object SubscriptionGracePeriodResponse](./subscriptiongraceperiodresponse.md)
  A response containing a single grace period configuration for a subscription.
- [object SubscriptionGracePeriod](./subscriptiongraceperiod.md)
  A grace period configuration for a subscription, allowing subscribers continued access while payment issues are resolved.
- [object SubscriptionGracePeriodUpdateRequest](./subscriptiongraceperiodupdaterequest.md)
  The request body you use to update a subscription grace period update request.
- [object AppSubscriptionGracePeriodLinkageResponse](./appsubscriptiongraceperiodlinkageresponse.md)

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
- [Subscription price points and subscription prices](./subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription price tiers](./subscription-price-tiers.md)
  Read the volume pricing tiers that set a per-seat price from a minimum number of seats.
- [Subscription price tier equalizations](./subscription-price-tier-equalizations.md)
  Calculate equalized volume pricing tiers for every territory from the tiers in your base territory.
- [Subscription price change previews](./subscription-price-change-previews.md)
  Preview how a proposed subscription price, including its volume pricing tiers, changes what existing subscribers pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/billing-grace-periods)*