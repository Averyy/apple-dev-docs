# Modify a subscription group localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update a specific localized display name and optional custom app name for a subscription group.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionGroupLocalizations/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a subscription group localization](post-v1-subscriptiongrouplocalizations.md)
  Create a localized display name and optional custom app name for a subscription group.
- [Read subscription group localization information](get-v1-subscriptiongrouplocalizations-_id_.md)
  Get the specific localized subscription group display name and optional custom app name for a subscription group.
- [Delete a subscription group localization](delete-v1-subscriptiongrouplocalizations-_id_.md)
  Delete localized metadata that you configured for a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptiongrouplocalizations-_id_)*