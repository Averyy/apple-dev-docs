# Add search keywords to an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add search keywords to a specific App Store version localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/relationships/searchKeywords`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version localization resource ID from the [`List all app store version localizations for an app store version`](get-v1-appstoreversions-_id_-appstoreversionlocalizations.md) response.

## See Also

- [List all search keywords for an app store version localization](get-v1-appstoreversionlocalizations-_id_-searchkeywords.md)
  Get search keywords for a specific App Store version localization.
- [List search keyword IDs for an app store version localization](get-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a specific App Store version localization.
- [Remove search keywords from an app store version localization](delete-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Remove search keywords from a specific App Store version localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords)*