# Modify an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Modify localized version-level information for a particular language.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version localization resource ID from the [`List all app store version localizations for an app store version`](get-v1-appstoreversions-_id_-appstoreversionlocalizations.md) response.

## See Also

- [Create an app store version localization](post-v1-appstoreversionlocalizations.md)
  Add localized version-level information for a new locale.
- [Delete an app store version localization](delete-v1-appstoreversionlocalizations-_id_.md)
  Delete a language from your version metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appstoreversionlocalizations-_id_)*