# Read Challenge Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific Game Center challenge image.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterChallengeImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterChallengeImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`

## Responses

- `200` OK (`GameCenterChallengeImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing challenge images
- [Read Image Information for a Challenge Localization](./get-v1-gamecenterchallengelocalizations-_id_-image.md)
  Get details about the image for a specific Game Center challenge localization.
- [Create a Challenge Image](./post-v1-gamecenterchallengeimages.md)
  Reserve an image for a Game Center challenge.
- [Commit an Image for a Challenge](./patch-v1-gamecenterchallengeimages-_id_.md)
  Commit an uploaded image asset as a Game Center challenge image.
- [Delete a Challenge Image](./delete-v1-gamecenterchallengeimages-_id_.md)
  Remove a specific image from a Game Center challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterchallengeimages-_id_)*