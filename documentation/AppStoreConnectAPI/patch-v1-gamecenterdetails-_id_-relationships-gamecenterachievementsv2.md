# Modify the Achievements for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the achievements relationship for a specific Game Center detail.

**Availability**:
- App Store Connect API 3.6+

## Overview

- id:
- 204:
- 401:
- 403:
- 404:
- 409:
- 422:
- 429:

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/gameCenterAchievementsV2`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterDetailGameCenterAchievementsV2LinkagesRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and editing Game Center details
- [Enable game center for an app](./post-v1-gamecenterdetails.md)
  Create a Game Center detail for an app.
- [Modify a game center detail for an app](./patch-v1-gamecenterdetails-_id_.md)
  Edit challenge state, default leaderboards, and groups.
- [Modify the Leaderboard Sets for a Game Center Detail](./patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Update the leaderboard sets relationship for a specific Game Center detail.
- [Modify the Leaderboards for a Game Center Detail](./patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Update the leaderboards relationship for a specific Game Center detail.
- [Modify the associated leaderboard sets for a game center detail](./patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  Edit the associated leaderboard sets for a Game Center detail.
- [Modify the associated leaderboards for a game center detail](./patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  Edit the associated leaderboards for a Game Center detail.
- [Modify the challenges minimum platform version for a game center detail](./patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions.md)
  Update the relationship between a challenges minimum platform version and a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievementsv2)*