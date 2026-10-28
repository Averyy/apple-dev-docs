# Create a Game Center Achievement Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a Game Center achievement image.

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

`POST https://api.appstoreconnect.apple.com/v2/gameCenterAchievementImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterAchievementImageV2CreateRequest`

## Responses

- `201` Created (`GameCenterAchievementImageV2Response`, `application/json`)
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
- [Modify a Game Center Achievement Image](./patch-v2-gamecenterachievementimages-_id_.md)
  Update a specific Game Center achievement image.
- [Delete a Game Center Achievement Image](./delete-v2-gamecenterachievementimages-_id_.md)
  Delete a specific Game Center achievement image.
- [Read Achievement Image Information](./get-v1-gamecenterachievementimages-_id_.md)
  Get information about an achievement image and its upload and processing status.
- [Create an Achievement Image](./post-v1-gamecenterachievementimages.md)
  Add a new achievement image.
- [Modify an Achievement Image](./patch-v1-gamecenterachievementimages-_id_.md)
  Commit an achievement image after uploading it.
- [Delete an Achievement Image](./delete-v1-gamecenterachievementimages-_id_.md)
  Delete an image that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-gamecenterachievementimages)*