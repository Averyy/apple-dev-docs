# Get all compatible version ids for a game center enabled version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: This endpoint is deprecated. Use [`List all compatible app version IDs`](./get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterEnabledVersionCompatibleVersionsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting and Adding Compatible Versions
- [Add compatible versions to a game center enabled version](./post-v1-gamecenterenabledversions-_id_-relationships-compatibleversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterenabledversions-_id_-relationships-compatibleversions)*