# Remove compatible app version relationships

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a compatible version relationship from an app version.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/{id}/relationships/compatibilityVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterAppVersionCompatibilityVersionsLinkagesRequest`

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

### Creating, editing, and deleting Game Center app versions
- [Create an app version](./post-v1-gamecenterappversions.md)
  Add a new Game Center app version.
- [Add compatible app version relationships](./post-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Create a relationship between two Game Center app versions.
- [Modify an app version](./patch-v1-gamecenterappversions-_id_.md)
  Change the state of Game Center enablement for an app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterappversions-_id_-relationships-compatibilityversions)*