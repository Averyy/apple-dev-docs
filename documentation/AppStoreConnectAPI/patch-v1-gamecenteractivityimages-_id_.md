# Commit an Image for an Activity

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit an uploaded image asset as a Game Center activity image.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game center activities](./configuring-game-center-activities.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterActivityImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterActivityImageUpdateRequest`

## Responses

- `200` OK (`GameCenterActivityImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center activities
- [Read activity image information](./get-v1-gamecenteractivityimages-_id_.md)
  Get information for a specific Game Center activity image.
- [Create an Activity Image](./post-v1-gamecenteractivityimages.md)
  Reserve an image for a Game Center activity.
- [Delete an Activity Image](./delete-v1-gamecenteractivityimages-_id_.md)
  Remove a specific image from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenteractivityimages-_id_)*