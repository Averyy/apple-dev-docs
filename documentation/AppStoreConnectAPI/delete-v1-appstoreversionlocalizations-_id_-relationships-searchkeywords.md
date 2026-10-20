# Remove search keywords from an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove search keywords from a specific App Store version localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/relationships/searchKeywords`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version localization resource ID from the [`List all app store version localizations for an app store version`](./get-v1-appstoreversions-_id_-appstoreversionlocalizations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreVersionLocalizationSearchKeywordsLinkagesRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Search Keywords
- [List all search keywords for an app store version localization](./get-v1-appstoreversionlocalizations-_id_-searchkeywords.md)
  Get search keywords for a specific App Store version localization.
- [List search keyword IDs for an app store version localization](./get-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a specific App Store version localization.
- [Add search keywords to an app store version localization](./post-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Add search keywords to a specific App Store version localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords)*