# Create an app version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new Game Center app version.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterAppVersionCreateRequest`

## Responses

- `201` Created (`GameCenterAppVersionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, editing, and deleting Game Center app versions
- [Add compatible app version relationships](./post-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Create a relationship between two Game Center app versions.
- [Modify an app version](./patch-v1-gamecenterappversions-_id_.md)
  Change the state of Game Center enablement for an app version.
- [Remove compatible app version relationships](./delete-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  Remove a compatible version relationship from an app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterappversions)*