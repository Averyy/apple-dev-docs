# Get challenge releases for a game center detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all challenge release information for a specific Game Center detail.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Mentions

- [Configuring Game Center challenges](./configuring-game-center-challenges.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/challengeReleases`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center detail resource ID from the [`Read the state of game center for an app`](./get-v1-apps-_id_-gamecenterdetail.md) response.

### Query Parameters

- `fields[gameCenterChallengeVersionReleases]` ([string]): **Allowed Values**: `version`
- `fields[gameCenterChallengeVersions]` ([string]): **Allowed Values**: `version`, `state`, `challenge`, `localizations`, `releases`, `defaultImage`
- `include` ([string]): **Allowed Values**: `version`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterChallengeVersionReleasesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Game center challenge information
- [Read challenge release ids for a game center detail](./get-v1-gamecenterdetails-_id_-relationships-challengereleases.md)
  List all the challenge release IDs for a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-challengereleases)*