# Read Challenge Version Release Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific Game Center challenge version release.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterChallengeVersionReleases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterChallengeVersionReleases]` ([string]): **Allowed Values**: `version`
- `include` ([string]): **Allowed Values**: `version`
- `fields[gameCenterChallengeVersions]` ([string]): **Allowed Values**: `version`, `state`, `challenge`, `localizations`, `releases`, `defaultImage`

## Responses

- `200` OK (`GameCenterChallengeVersionReleaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing version releases
- [Add a Challenge Version Release](./post-v1-gamecenterchallengeversionreleases.md)
  Add a version release for a specific Game Center challenge version.
- [Delete a Challenge Version Release](./delete-v1-gamecenterchallengeversionreleases-_id_.md)
  Remove a specific version release from a Game Center challenge version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterchallengeversionreleases-_id_)*