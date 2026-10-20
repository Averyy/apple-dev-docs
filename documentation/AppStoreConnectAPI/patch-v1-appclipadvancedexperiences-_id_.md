# Modify and delete an advanced app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update and delete an existing advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperiences/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the advanced App Clip experience resource ID from the [`List all advanced app clip experiences for an app clip`](./get-v1-appclips-_id_-appclipadvancedexperiences.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipAdvancedExperienceUpdateRequest`

The request body you use to update an advanced App Clip experience.

## Responses

- `200` OK (`AppClipAdvancedExperienceResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting and Managing Advanced App Clip Experiences
- [Read advanced app clip experience information](./get-v1-appclipadvancedexperiences-_id_.md)
  Get information about a specific advanced App Clip experience.
- [Create an advanced app clip experience](./post-v1-appclipadvancedexperiences.md)
  Configure a new advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipadvancedexperiences-_id_)*