# Create the localized metadata for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Provide localized metadata that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppClipDefaultExperienceLocalizationCreateRequest`

The request body you use to create a default App Clip experience localization.

## Responses

- `201` Created (`AppClipDefaultExperienceLocalizationResponse`, `application/json`): The request completed successfully and a new Default App Clip Experience Localizations resource has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Your Default App Clip Experience’s Metadata
- [Modify the localization for a default app clip experience](./patch-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Update localized metadata for a specific default App Clip experience.
- [Delete a default app clip experience localization](./delete-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Delete localized metadata that appears on the App Clip card of a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appclipdefaultexperiencelocalizations)*