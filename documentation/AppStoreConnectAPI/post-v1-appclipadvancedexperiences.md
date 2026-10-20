# Create an advanced app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Configure a new advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperiences`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipAdvancedExperienceCreateRequest`

The request body you use to create a new advanced App Clip experience.

## Responses

- `201` Created (`AppClipAdvancedExperienceResponse`, `application/json`): The request completed successfully and a new advanced App Clip experience has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting and Managing Advanced App Clip Experiences
- [Read advanced app clip experience information](./get-v1-appclipadvancedexperiences-_id_.md)
  Get information about a specific advanced App Clip experience.
- [Modify and delete an advanced app clip experience](./patch-v1-appclipadvancedexperiences-_id_.md)
  Update and delete an existing advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appclipadvancedexperiences)*