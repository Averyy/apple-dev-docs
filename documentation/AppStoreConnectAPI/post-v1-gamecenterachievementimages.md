# Create an Achievement Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a new achievement image.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Create a Game Center Achievement Image`](./post-v2-gamecenterachievementimages.md) instead.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterAchievementImageCreateRequest`

## Responses

- `201` Created (`GameCenterAchievementImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center achievements images
- [Read Game Center Achievement Image Information](./get-v2-gamecenterachievementimages-_id_.md)
  Get information about a specific Game Center achievement image.
- [Create a Game Center Achievement Image](./post-v2-gamecenterachievementimages.md)
  Create a Game Center achievement image.
- [Modify a Game Center Achievement Image](./patch-v2-gamecenterachievementimages-_id_.md)
  Update a specific Game Center achievement image.
- [Delete a Game Center Achievement Image](./delete-v2-gamecenterachievementimages-_id_.md)
  Delete a specific Game Center achievement image.
- [Read Achievement Image Information](./get-v1-gamecenterachievementimages-_id_.md)
  Get information about an achievement image and its upload and processing status.
- [Modify an Achievement Image](./patch-v1-gamecenterachievementimages-_id_.md)
  Commit an achievement image after uploading it.
- [Delete an Achievement Image](./delete-v1-gamecenterachievementimages-_id_.md)
  Delete an image that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterachievementimages)*