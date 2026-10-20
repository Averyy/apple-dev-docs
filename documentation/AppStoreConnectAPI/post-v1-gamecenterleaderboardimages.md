# Create a Leaderboard Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new leaderboard image.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Create a Game Center Leaderboard Image`](./post-v2-gamecenterleaderboardimages.md) instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardImageCreateRequest`

## Responses

- `201` Created (`GameCenterLeaderboardImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard images
- [Read Game Center Leaderboard Image Information](./get-v2-gamecenterleaderboardimages-_id_.md)
  Get information about a specific Game Center leaderboard image.
- [Create a Game Center Leaderboard Image](./post-v2-gamecenterleaderboardimages.md)
  Create a Game Center leaderboard image.
- [Modify a Game Center Leaderboard Image](./patch-v2-gamecenterleaderboardimages-_id_.md)
  Update a specific Game Center leaderboard image.
- [Delete a Game Center Leaderboard Image](./delete-v2-gamecenterleaderboardimages-_id_.md)
  Delete a specific Game Center leaderboard image.
- [Read Leaderboard Image Information](./get-v1-gamecenterleaderboardimages-_id_.md)
  Get information about a leaderboard image and its upload and processing status.
- [Modify a Leaderboard Image](./patch-v1-gamecenterleaderboardimages-_id_.md)
  Commit a leaderboard image after uploading it.
- [Delete a Leaderboard Image](./delete-v1-gamecenterleaderboardimages-_id_.md)
  Delete an image that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterleaderboardimages)*