# Get activity releases for a game center detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all activity release information for a specific Game Center detail.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Mentions

- [Configuring Game center activities](./configuring-game-center-activities.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/activityReleases`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterActivityVersionReleases]` ([string]): **Allowed Values**: `version`
- `fields[gameCenterActivityVersions]` ([string]): **Allowed Values**: `version`, `state`, `fallbackUrl`, `activity`, `localizations`, `defaultImage`, `releases`
- `include` ([string]): **Allowed Values**: `version`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterActivityVersionReleasesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Game center activity information
- [Get activity release ids for a game center detail](./get-v1-gamecenterdetails-_id_-relationships-activityreleases.md)
  List all activity release IDs for a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-activityreleases)*