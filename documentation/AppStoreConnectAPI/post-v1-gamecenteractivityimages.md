# Create an Activity Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve an image for a Game Center activity.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game center activities](./configuring-game-center-activities.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterActivityImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterActivityImageCreateRequest`

## Responses

- `201` Created (`GameCenterActivityImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center activities
- [Read activity image information](./get-v1-gamecenteractivityimages-_id_.md)
  Get information for a specific Game Center activity image.
- [Commit an Image for an Activity](./patch-v1-gamecenteractivityimages-_id_.md)
  Commit an uploaded image asset as a Game Center activity image.
- [Delete an Activity Image](./delete-v1-gamecenteractivityimages-_id_.md)
  Remove a specific image from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenteractivityimages)*