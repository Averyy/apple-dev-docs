# Delete an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a language from your version metadata.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version localization resource ID from the [`List all app store version localizations for an app store version`](get-v1-appstoreversions-_id_-appstoreversionlocalizations.md) response.

## See Also

- [Create an app store version localization](post-v1-appstoreversionlocalizations.md)
  Add localized version-level information for a new locale.
- [Modify an app store version localization](patch-v1-appstoreversionlocalizations-_id_.md)
  Modify localized version-level information for a particular language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstoreversionlocalizations-_id_)*