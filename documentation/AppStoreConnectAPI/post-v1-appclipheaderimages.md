# Create an app clip card image for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve an image asset that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appClipHeaderImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipHeaderImageCreateRequest`

The request body you use to create an App Clip header image.

## Responses

- `201` Created (`AppClipHeaderImageResponse`, `application/json`): The request completed successfully and a new App Clip Header Images resource has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing App Clip Card Images
- [Read the app clip card image](./get-v1-appclipheaderimages-_id_.md)
  Get the image that appears on the App Clip card of a default App Clip experience.
- [Modify an app clip card image](./patch-v1-appclipheaderimages-_id_.md)
  Change the image that appears on the App Clip card of a default App Clip experience.
- [Delete a default app clip experience image](./delete-v1-appclipheaderimages-_id_.md)
  Delete the image asset that appears on the App Clip card for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appclipheaderimages)*