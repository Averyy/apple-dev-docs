# List preview set IDs for an App Store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.5

> **Deprecated**: This relationship is deprecated. Use the [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) relationship instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/relationships/appPreviewSets`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`AppStoreVersionLocalizationAppPreviewSetsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Information from a Localization
- [List all app preview sets for an app store version localization](./get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md)
  List all app preview sets for a specific localization.
- [List all app screenshot sets for an app store version localization](./get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md)
  List all screenshot sets for a specific localization.
- [List screenshot set IDs for an App Store version localization](./get-v1-appstoreversionlocalizations-_id_-relationships-appscreenshotsets.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_-relationships-apppreviewsets)*