# Read Activity Version Release Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific Game Center activity version release.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterActivityVersionReleases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterActivityVersionReleases]` ([string]): **Allowed Values**: `version`
- `include` ([string]): **Allowed Values**: `version`
- `fields[gameCenterActivityVersions]` ([string]): **Allowed Values**: `version`, `state`, `fallbackUrl`, `activity`, `localizations`, `defaultImage`, `releases`

## Responses

- `200` OK (`GameCenterActivityVersionReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Read, create, and update Game Center activity versions
- [Add an Activity Version Release](./post-v1-gamecenteractivityversionreleases.md)
  Add a version release for a specific Game Center activity.
- [Delete an Activity Version Release](./delete-v1-gamecenteractivityversionreleases-_id_.md)
  Remove a specific version release from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenteractivityversionreleases-_id_)*