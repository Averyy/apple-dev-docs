# List all subscription groups for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of subscription groups for a specific app.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/subscriptionGroups`

## Parameters

- `fields[subscriptionGroupLocalizations]` ([string]): Additional fields to include for each subscription group localization resource returned by the response.
- `fields[subscriptionGroups]` ([string]): Additional fields to include for each subscription group resource returned by the response.
- `fields[subscriptions]` ([string]): Additional fields to include for each subscription resource returned by the response.
- `filter[referenceName]` ([string]): Filter the returned subscription groups by reference name.
- `filter[subscriptions.state]` ([string]): Filter the returned subscription groups by subscriptions state.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of subscription group resources to return.
- `limit[subscriptionGroupLocalizations]` (integer): The maximum number of related subscription group localizations resources to return.
- `limit[subscriptions]` (integer): The maximum number of related subscriptions resources to return.
- `sort` ([string]): Attributes by which to sort.
- `fields[subscriptionGroupVersions]` ([string])
- `limit[versions]` (integer)

## See Also

- [Read the billing grace period value for an app](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [Get the subscription grace period ID for an app](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [List subscription group IDs for an app](get-v1-apps-_id_-relationships-subscriptiongroups.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-subscriptiongroups)*