# Create a Game Center Leaderboard Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a Game Center leaderboard image.

**Availability**:
- App Store Connect API 3.6+

## Overview

- 201:
- 400:
- 401:
- 403:
- 409:
- 422:
- 429:

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterLeaderboardImageV2CreateRequest`

## Responses

- `201` Created (`GameCenterLeaderboardImageV2Response`, `application/json`)
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
- [Modify a Game Center Leaderboard Image](./patch-v2-gamecenterleaderboardimages-_id_.md)
  Update a specific Game Center leaderboard image.
- [Delete a Game Center Leaderboard Image](./delete-v2-gamecenterleaderboardimages-_id_.md)
  Delete a specific Game Center leaderboard image.
- [Read Leaderboard Image Information](./get-v1-gamecenterleaderboardimages-_id_.md)
  Get information about a leaderboard image and its upload and processing status.
- [Create a Leaderboard Image](./post-v1-gamecenterleaderboardimages.md)
  Add a new leaderboard image.
- [Modify a Leaderboard Image](./patch-v1-gamecenterleaderboardimages-_id_.md)
  Commit a leaderboard image after uploading it.
- [Delete a Leaderboard Image](./delete-v1-gamecenterleaderboardimages-_id_.md)
  Delete an image that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-gamecenterleaderboardimages)*