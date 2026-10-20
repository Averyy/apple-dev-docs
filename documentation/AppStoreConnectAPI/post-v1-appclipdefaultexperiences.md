# Create a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Configure a new default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipDefaultExperienceCreateRequest`

The request body you use to create a default App Clip experience.

## Responses

- `201` Created (`AppClipDefaultExperienceResponse`, `application/json`): The request completed successfully and a new default App Clip experience has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Default App Clip Experiences
- [Modify a default app clip experience](./patch-v1-appclipdefaultexperiences-_id_.md)
  Update a default App Clip experience.
- [Modify the related app store version for a default app clip experience](./patch-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Update the relationship between a default App Clip experience and an App Store Version.
- [Delete a default app clip experience](./delete-v1-appclipdefaultexperiences-_id_.md)
  Delete a specific default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appclipdefaultexperiences)*