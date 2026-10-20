# Delete an Activity Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a specific image from a Game Center activity.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterActivityImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Game Center activities
- [Read activity image information](./get-v1-gamecenteractivityimages-_id_.md)
  Get information for a specific Game Center activity image.
- [Create an Activity Image](./post-v1-gamecenteractivityimages.md)
  Reserve an image for a Game Center activity.
- [Commit an Image for an Activity](./patch-v1-gamecenteractivityimages-_id_.md)
  Commit an uploaded image asset as a Game Center activity image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenteractivityimages-_id_)*