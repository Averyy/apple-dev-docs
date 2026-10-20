# Read Leaderboard Set Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a leaderboard set image and its upload and processing status.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Read Game Center Leaderboard Set Image Information`](./get-v2-gamecenterleaderboardsetimages-_id_.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterLeaderboardSetImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`, `gameCenterLeaderboardSetLocalization`
- `include` ([string]): **Allowed Values**: `gameCenterLeaderboardSetLocalization`
- `fields[gameCenterLeaderboardSetLocalizations]` ([string]) *(deprecated)*: **Allowed Values**: `locale`, `name`, `gameCenterLeaderboardSet`, `gameCenterLeaderboardSetImage`

## Responses

- `200` OK (`GameCenterLeaderboardSetImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
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
- [Create a Leaderboard Set Image](./post-v1-gamecenterleaderboardsetimages.md)
  Add a new leaderboard set image.
- [Modify a Leaderboard Set Image](./patch-v1-gamecenterleaderboardsetimages-_id_.md)
  Commit a leaderboard set image after uploading it.
- [Delete a Leaderboard Set Image](./delete-v1-gamecenterleaderboardsetimages-_id_.md)
  Delete an image that’s associated with a leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardsetimages-_id_)*