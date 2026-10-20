# Modify the related app store version for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the relationship between a default App Clip experience and an App Store Version.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}/relationships/releaseWithAppStoreVersion`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Default App Clip Experiences resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageRequest`

The request body you use to update the relationship between a default App Clip experience and an App Store version.

## Responses

- `204` No Content: The request completed successfully and the relationship with the specific App Store Versions resource was updated.
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Default App Clip Experiences
- [Create a default app clip experience](./post-v1-appclipdefaultexperiences.md)
  Configure a new default App Clip experience.
- [Modify a default app clip experience](./patch-v1-appclipdefaultexperiences-_id_.md)
  Update a default App Clip experience.
- [Delete a default app clip experience](./delete-v1-appclipdefaultexperiences-_id_.md)
  Delete a specific default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion)*