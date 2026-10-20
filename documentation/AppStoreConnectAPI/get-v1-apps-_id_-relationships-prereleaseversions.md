# List prerelease version IDs for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/preReleaseVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`AppPreReleaseVersionsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting app build and prerelease version information
- [List all builds of an app](./get-v1-apps-_id_-builds.md)
  Get a list of builds associated with a specific app.
- [List build IDs for an app](./get-v1-apps-_id_-relationships-builds.md)
- [List all prerelease versions for an app](./get-v1-apps-_id_-prereleaseversions.md)
  Get a list of prerelease versions associated with a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-relationships-prereleaseversions)*