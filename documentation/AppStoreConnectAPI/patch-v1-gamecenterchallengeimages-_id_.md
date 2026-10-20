# Commit an Image for a Challenge

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Commit an uploaded image asset as a Game Center challenge image.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game Center challenges](./configuring-game-center-challenges.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterChallengeImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterChallengeImageUpdateRequest`

## Responses

- `200` OK (`GameCenterChallengeImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing challenge images
- [Read Image Information for a Challenge Localization](./get-v1-gamecenterchallengelocalizations-_id_-image.md)
  Get details about the image for a specific Game Center challenge localization.
- [Read Challenge Image Information](./get-v1-gamecenterchallengeimages-_id_.md)
  Get information for a specific Game Center challenge image.
- [Create a Challenge Image](./post-v1-gamecenterchallengeimages.md)
  Reserve an image for a Game Center challenge.
- [Delete a Challenge Image](./delete-v1-gamecenterchallengeimages-_id_.md)
  Remove a specific image from a Game Center challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterchallengeimages-_id_)*