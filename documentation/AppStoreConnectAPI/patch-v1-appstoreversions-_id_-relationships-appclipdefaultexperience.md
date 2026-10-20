# Modify the default app clip experience of an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the relationship between an App Store version and a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/relationships/appClipDefaultExperience`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the App Store Versions resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppStoreVersionAppClipDefaultExperienceLinkageRequest`

The request body you use to update the relationship between an App Store version and a default App Clip experience.

## Responses

- `204` No Content: The request completed successfully and the relationship with the specific default App Clip experience was updated.
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Attaching a Default App Clip Experience to a Version
- [Get the default app clip experience for an app store version](./get-v1-appstoreversions-_id_-appclipdefaultexperience.md)
  Get the default App Clip experience for an App Store version of your app.
- [Get the default app clip experiences resource id for an app store version](./get-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Get the ID of an app’s related default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appstoreversions-_id_-relationships-appclipdefaultexperience)*