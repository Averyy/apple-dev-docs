# Remove compatible versions from a game center enabled version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: This endpoint is deprecated. Use [`Remove compatible app version relationships`](./delete-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md) instead.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterEnabledVersionCompatibleVersionsLinkagesRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Removing and Replacing Compatible Versions
- [Replace all compatible versions for a game center enabled version](./patch-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterenabledversions-_id_-relationships-compatibleversions)*