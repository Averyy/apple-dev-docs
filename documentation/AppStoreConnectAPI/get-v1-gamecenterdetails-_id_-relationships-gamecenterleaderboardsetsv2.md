# Get All Leaderboard Set IDs for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of leaderboard set resource IDs for a specific Game Center detail.

**Availability**:
- App Store Connect API 3.6+

## Overview

- id:
- limit:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/gameCenterLeaderboardSetsV2`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterDetailGameCenterLeaderboardSetsV2LinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and editing leaderboard sets in a Game Center detail
- [List All Game Center Leaderboard Sets for a Game Center Detail](./get-v1-gamecenterdetails-_id_-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard sets for a specific Game Center detail.
- [Get leaderboard sets information](./get-v1-gamecenterdetails-_id_-gamecenterleaderboardsets.md)
  Get all leaderboard sets and related information for a Game Center detail.
- [List Leaderboard Sets](./get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  List all leaderboards for a Game Center detail.
- [Get leaderboard set releases information](./get-v1-gamecenterdetails-_id_-leaderboardsetreleases.md)
  List all leaderboard set releases for a Game Center detail.
- [List leaderboard set release IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-leaderboardsetreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2)*