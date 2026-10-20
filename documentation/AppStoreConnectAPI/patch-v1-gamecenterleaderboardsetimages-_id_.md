# Modify a Leaderboard Set Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit a leaderboard set image after uploading it.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Modify a Game Center Leaderboard Set Image`](./patch-v2-gamecenterleaderboardsetimages-_id_.md) instead.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardSetImageUpdateRequest`

## Responses

- `200` OK (`GameCenterLeaderboardSetImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set images
- [Read Game Center Leaderboard Set Image Information](./get-v2-gamecenterleaderboardsetimages-_id_.md)
  Get information about a specific Game Center leaderboard set image.
- [Create a Game Center Leaderboard Set Image](./post-v2-gamecenterleaderboardsetimages.md)
  Create a Game Center leaderboard set image.
- [Modify a Game Center Leaderboard Set Image](./patch-v2-gamecenterleaderboardsetimages-_id_.md)
  Update a specific Game Center leaderboard set image.
- [Delete a Game Center Leaderboard Set Image](./delete-v2-gamecenterleaderboardsetimages-_id_.md)
  Delete a specific Game Center leaderboard set image.
- [Read Leaderboard Set Image Information](./get-v1-gamecenterleaderboardsetimages-_id_.md)
  Get information about a leaderboard set image and its upload and processing status.
- [Create a Leaderboard Set Image](./post-v1-gamecenterleaderboardsetimages.md)
  Add a new leaderboard set image.
- [Delete a Leaderboard Set Image](./delete-v1-gamecenterleaderboardsetimages-_id_.md)
  Delete an image that’s associated with a leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterleaderboardsetimages-_id_)*