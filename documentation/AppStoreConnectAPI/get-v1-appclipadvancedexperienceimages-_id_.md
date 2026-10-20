# Read image information for an advanced app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about the image that appears on the App Clip card of an advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperienceImages/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the advanced App Clip experience image resource ID from the [`Create an app clip card image for an advanced app clip experience`](./post-v1-appclipadvancedexperienceimages.md) response.

### Query Parameters

- `fields[appClipAdvancedExperienceImages]` ([string]): Additional fields to include for each Advanced App Clip Experience Images resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `imageAsset`, `uploadOperations`, `assetDeliveryState`

## Responses

- `200` OK (`AppClipAdvancedExperienceImageResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Images for Advanced App Clip Experiences
- [Create an app clip card image for an advanced app clip experience](./post-v1-appclipadvancedexperienceimages.md)
  Reserve an image asset that appears on the App Clip card of an advanced App Clip experience.
- [Modify the image for an advanced app clip experience](./patch-v1-appclipadvancedexperienceimages-_id_.md)
  Update image information or commit the image asset of an advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipadvancedexperienceimages-_id_)*