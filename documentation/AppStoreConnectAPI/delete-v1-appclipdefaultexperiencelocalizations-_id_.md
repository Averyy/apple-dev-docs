# Delete a default app clip experience localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete localized metadata that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appClipDefaultExperienceLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the default App Clip experience localization resource ID from the [`Read localization information for a default app clip experience`](./get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md) response.

## Responses

- `204` No Content: The request completed successfully and the specific Default App Clip Experience Localizations resource was deleted.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Your Default App Clip Experience’s Metadata
- [Create the localized metadata for a default app clip experience](./post-v1-appclipdefaultexperiencelocalizations.md)
  Provide localized metadata that appears on the App Clip card of a default App Clip experience.
- [Modify the localization for a default app clip experience](./patch-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Update localized metadata for a specific default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appclipdefaultexperiencelocalizations-_id_)*