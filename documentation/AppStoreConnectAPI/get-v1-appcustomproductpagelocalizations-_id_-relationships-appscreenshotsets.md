# List app screenshot sets IDs for a custom product page localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the app screenshot set IDs for a specific custom product page localization.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.5

> **Deprecated**: This relationship is deprecated. Use the [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) relationship instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}/relationships/appScreenshotSets`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page localization resource ID from the [`List Custom Product Pages Localizations`](./get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md) response.

### Query Parameters

- `limit` (integer): The maximum number of app screenshot set resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppCustomProductPageLocalizationAppScreenshotSetsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting screenshot information
- [List App Screenshot Sets for a Custom Product Page Localization](./get-v1-appcustomproductpagelocalizations-_id_-appscreenshotsets.md)
  List the app screenshot sets for a specific custom product page localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpagelocalizations-_id_-relationships-appscreenshotsets)*