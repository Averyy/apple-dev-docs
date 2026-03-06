# List All Subscription Groups for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of subscription groups for a specific app.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/subscriptionGroups`

## Parameters

- `fields[subscriptionGroupLocalizations]` ([string])
- `fields[subscriptionGroups]` ([string])
- `fields[subscriptions]` ([string])
- `filter[referenceName]` ([string])
- `filter[subscriptions.state]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[subscriptionGroupLocalizations]` (integer)
- `limit[subscriptions]` (integer)
- `sort` ([string])

## See Also

- [Read the Billing Grace Period Value for an App](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [GET /v1/apps/{id}/relationships/subscriptionGracePeriod](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [GET /v1/apps/{id}/relationships/subscriptionGroups](get-v1-apps-_id_-relationships-subscriptiongroups.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-subscriptiongroups)*