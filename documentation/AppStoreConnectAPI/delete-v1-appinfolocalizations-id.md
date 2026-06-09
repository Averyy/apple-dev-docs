# Delete an app info localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app information localization that is associated with an app.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appInfoLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app info localization resource ID from the [`List all app info localizations for an app info`](get-v1-appinfos-_id_-appinfolocalizations.md) response.

## See Also

- [Create an app info localization](post-v1-appinfolocalizations.md)
  Add app-level localized information for a new locale.
- [Modify an app info localization](patch-v1-appinfolocalizations-_id_.md)
  Modify localized app-level information for a particular language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appinfolocalizations-_id_)*