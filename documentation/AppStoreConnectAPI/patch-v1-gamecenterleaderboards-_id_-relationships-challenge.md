# Modify the challenge for a Game Center leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Modify the Challenge for a Game Center Leaderboard`](./patch-v2-gamecenterleaderboards-_id_-relationships-challenge.md) instead.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/{id}/relationships/challenge`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardChallengeLinkageRequest`

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

### Creating, modifying, and deleting leaderboards
- [Create a Game Center Leaderboard](./post-v2-gamecenterleaderboards.md)
  Create a Game Center leaderboard.
- [Modify a Game Center Leaderboard](./patch-v2-gamecenterleaderboards-_id_.md)
  Update a specific Game Center leaderboard.
- [Modify the Activity for a Game Center Leaderboard](./patch-v2-gamecenterleaderboards-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center leaderboard.
- [Modify the Challenge for a Game Center Leaderboard](./patch-v2-gamecenterleaderboards-_id_-relationships-challenge.md)
  Update the challenge relationship for a specific Game Center leaderboard.
- [Delete a Game Center Leaderboard](./delete-v2-gamecenterleaderboards-_id_.md)
  Delete a specific Game Center leaderboard.
- [Create a Leaderboard](./post-v1-gamecenterleaderboards.md)
  Add a new leaderboard to your app.
- [Edit a Leaderboard](./patch-v1-gamecenterleaderboards-_id_.md)
  Modify the details of a leaderboard.
- [Edit the Relationship Between a Leaderboard and a Group Leaderboard](./patch-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  Modify the group leadboard to which a leaderboard belongs.
- [Modify the activity for a Game Center leaderboard](./patch-v1-gamecenterleaderboards-_id_-relationships-activity.md)
- [Delete a Leaderboard](./delete-v1-gamecenterleaderboards-_id_.md)
  Delete a leaderboard from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterleaderboards-_id_-relationships-challenge)*