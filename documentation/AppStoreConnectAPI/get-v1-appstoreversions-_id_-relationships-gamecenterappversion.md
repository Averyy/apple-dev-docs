# Get the Game Center app version ID for an App Store version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/relationships/gameCenterAppVersion`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppStoreVersionGameCenterAppVersionLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Game Center app versions
- [Read game center app version information of an app store version](./get-v1-appstoreversions-_id_-gamecenterappversion.md)
  Get the status of Game Center enablement for an App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-relationships-gamecenterappversion)*