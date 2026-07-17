# Read subscription group localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the custom name for a specific locale of a subscription group configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/subscriptionGroupLocalizations/{id}`

## Parameters

- `fields[subscriptionGroupLocalizations]` ([string])
- `fields[subscriptionGroupVersions]` ([string])
- `include` ([string])

## See Also

- [Create a subscription group localization](post-v2-subscriptiongrouplocalizations.md)
  Create a localized custom name for a subscription group configured with the v2 API.
- [Modify a subscription group localization](patch-v2-subscriptiongrouplocalizations-_id_.md)
  Update the custom name for a specific locale of a subscription group configured with the v2 API.
- [Delete a subscription group localization](delete-v2-subscriptiongrouplocalizations-_id_.md)
  Delete a localized custom name for a subscription group configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-subscriptiongrouplocalizations-_id_)*