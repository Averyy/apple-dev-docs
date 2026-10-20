# Create an app store version phased release

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Enable phased release for an App Store version.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appStoreVersionPhasedReleases`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreVersionPhasedReleaseCreateRequest`

## Responses

- `201` Created (`AppStoreVersionPhasedReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Phased Releases
- [Modify an app store version phased release](./patch-v1-appstoreversionphasedreleases-_id_.md)
  Pause or resume a phased release, or immediately release an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstoreversionphasedreleases)*