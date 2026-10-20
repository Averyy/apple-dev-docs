# List all search keywords for an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get search keywords for a specific App Store version localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/searchKeywords`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Store version localization resource ID from the [`List all app store version localizations for an app store version`](./get-v1-appstoreversions-_id_-appstoreversionlocalizations.md) response.

### Query Parameters

- `fields[appKeywords]` ([string]): Additional fields to include for each app keyword resource returned by the response.
- `filter[locale]` ([string]): Filter the returned app keywords by locale.
- `filter[platform]` ([string]): Filter the returned app keywords by platform.
- `limit` (integer): The maximum number of app keyword resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppKeywordsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Search Keywords
- [List search keyword IDs for an app store version localization](./get-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a specific App Store version localization.
- [Add search keywords to an app store version localization](./post-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Add search keywords to a specific App Store version localization.
- [Remove search keywords from an app store version localization](./delete-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Remove search keywords from a specific App Store version localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_-searchkeywords)*