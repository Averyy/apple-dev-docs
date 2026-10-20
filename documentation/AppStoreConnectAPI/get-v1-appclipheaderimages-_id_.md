# Read the app clip card image

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the image that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipHeaderImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip header image resource ID from the [`Create an app clip card image for a default app clip experience`](./post-v1-appclipheaderimages.md) response.

### Query Parameters

- `fields[appClipHeaderImages]` ([string]): Additional fields to include for each app clip header image resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `uploadOperations`, `assetDeliveryState`, `appClipDefaultExperienceLocalization`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appClipDefaultExperienceLocalization`
- `fields[appClipDefaultExperienceLocalizations]` ([string]): **Allowed Values**: `locale`, `subtitle`, `appClipDefaultExperience`, `appClipHeaderImage`

## Responses

- `200` OK (`AppClipHeaderImageResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing App Clip Card Images
- [Create an app clip card image for a default app clip experience](./post-v1-appclipheaderimages.md)
  Reserve an image asset that appears on the App Clip card of a default App Clip experience.
- [Modify an app clip card image](./patch-v1-appclipheaderimages-_id_.md)
  Change the image that appears on the App Clip card of a default App Clip experience.
- [Delete a default app clip experience image](./delete-v1-appclipheaderimages-_id_.md)
  Delete the image asset that appears on the App Clip card for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipheaderimages-_id_)*