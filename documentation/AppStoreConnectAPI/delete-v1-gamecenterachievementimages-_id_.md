# Delete an Achievement Image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an image that’s associated with an achievement.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Delete a Game Center Achievement Image`](./delete-v2-gamecenterachievementimages-_id_.md) instead.

## Discussion

### Example Request and Response

**Request**:

```
DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages/{id}
```

**Response**:

```json
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center achievement images resource ID from the [`Read Achievement Information`](./get-v1-gamecenterachievements-_id_.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
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
- [Create an Achievement Image](./post-v1-gamecenterachievementimages.md)
  Add a new achievement image.
- [Modify an Achievement Image](./patch-v1-gamecenterachievementimages-_id_.md)
  Commit an achievement image after uploading it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterachievementimages-_id_)*