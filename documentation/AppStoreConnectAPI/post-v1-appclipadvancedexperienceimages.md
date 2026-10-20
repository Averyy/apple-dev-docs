# Create an app clip card image for an advanced app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Reserve an image asset that appears on the App Clip card of an advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperienceImages`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipAdvancedExperienceImageCreateRequest`

The request body you use to reserve an image asset for an advanced App Clip experience.

## Responses

- `201` Created (`AppClipAdvancedExperienceImageResponse`, `application/json`): The request completed successfully and a new Advanced App Clip Experience Images resource has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Images for Advanced App Clip Experiences
- [Read image information for an advanced app clip experience](./get-v1-appclipadvancedexperienceimages-_id_.md)
  Get information about the image that appears on the App Clip card of an advanced App Clip experience.
- [Modify the image for an advanced app clip experience](./patch-v1-appclipadvancedexperienceimages-_id_.md)
  Update image information or commit the image asset of an advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appclipadvancedexperienceimages)*