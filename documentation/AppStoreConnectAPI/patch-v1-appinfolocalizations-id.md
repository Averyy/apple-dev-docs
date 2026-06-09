# Modify an app info localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Modify localized app-level information for a particular language.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appInfoLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app info localization resource ID from the [`List all app info localizations for an app info`](get-v1-appinfos-_id_-appinfolocalizations.md) response.

## See Also

- [Create an app info localization](post-v1-appinfolocalizations.md)
  Add app-level localized information for a new locale.
- [Delete an app info localization](delete-v1-appinfolocalizations-_id_.md)
  Delete an app information localization that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appinfolocalizations-_id_)*