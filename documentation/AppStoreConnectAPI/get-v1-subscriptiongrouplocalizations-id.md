# Read Subscription Group Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the specific localized subscription group display name and optional custom app name for a subscription group.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionGroupLocalizations/{id}`

## Parameters

- `fields[subscriptionGroupLocalizations]` ([string])
- `include` ([string])
- `fields[subscriptionGroups]` ([string])

## See Also

- [Create a Subscription Group Localization](post-v1-subscriptiongrouplocalizations.md)
  Create a localized display name and optional custom app name for a subscription group.
- [Modify a Subscription Group Localization](patch-v1-subscriptiongrouplocalizations-_id_.md)
  Update a specific localized display name and optional custom app name for a subscription group.
- [Delete a Subscription Group Localization](delete-v1-subscriptiongrouplocalizations-_id_.md)
  Delete localized metadata that you configured for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptiongrouplocalizations-_id_)*