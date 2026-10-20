# Read activity image information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific Game Center activity image.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterActivityImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterActivityImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`

## Responses

- `200` OK (`GameCenterActivityImageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center activities
- [Create an Activity Image](./post-v1-gamecenteractivityimages.md)
  Reserve an image for a Game Center activity.
- [Commit an Image for an Activity](./patch-v1-gamecenteractivityimages-_id_.md)
  Commit an uploaded image asset as a Game Center activity image.
- [Delete an Activity Image](./delete-v1-gamecenteractivityimages-_id_.md)
  Remove a specific image from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenteractivityimages-_id_)*