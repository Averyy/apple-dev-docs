# List Leaderboards

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

​List all leaderboards for a Game Center detail.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated.

## Mentions

- [Configuring Game Center challenges](./configuring-game-center-challenges.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboards`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center detail resource ID from the [`Read the state of game center for an app`](./get-v1-apps-_id_-gamecenterdetail.md) response.

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterDetailGameCenterLeaderboardsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and editing Game Center detail leaderboards
- [List All Game Center Leaderboards for a Game Center Detail](./get-v1-gamecenterdetails-_id_-gamecenterleaderboardsv2.md)
  Get a list of leaderboards for a specific Game Center detail.
- [Get All Leaderboard IDs for a Game Center Detail](./get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Get a list of leaderboard resource IDs for a specific Game Center detail.
- [Read Leaderboard Releases](./get-v1-gamecenterdetails-_id_-leaderboardreleases.md)
  List all leaderboard releases for a Game Center detail.
- [List leaderboard release IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-leaderboardreleases.md)
- [Get leaderboards information](./get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md)
  Get all leaderboards and related information for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards)*