# Modify the Billing Grace Period Opt-in Status and Duration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change the Boolean value representing the billing grace period opt-in status.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)

#### Discussion

##### Example Request and Response

## Request Body

There are now new duration options that can be set by using [`SubscriptionGracePeriodDuration`](subscriptiongraceperiodduration.md)

## See Also

- [Read the Billing Grace Period Value for an App](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [GET /v1/apps/{id}/relationships/subscriptionGracePeriod](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [Read the Billing Grace Period Value](get-v1-subscriptiongraceperiods-_id_.md)
  Get the Boolean value that represents the billing grace period opt-in state and the duration of the billing grace period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptiongraceperiods-_id_)*