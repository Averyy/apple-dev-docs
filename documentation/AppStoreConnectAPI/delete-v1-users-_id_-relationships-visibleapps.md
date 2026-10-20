# Remove visible apps from a user

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove a user on your team’s access to one or more apps.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/users/{id}/relationships/visibleApps`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `UserVisibleAppsLinkagesRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing, Adding, and Removing App Access
- [List all apps visible to a user](./get-v1-users-_id_-visibleapps.md)
  Get a list of apps that a user on your team can view.
- [Get all visible app resource ids for a user](./get-v1-users-_id_-relationships-visibleapps.md)
  Get a list of app resource IDs to which a user on your team has access.
- [Add visible apps to a user](./post-v1-users-_id_-relationships-visibleapps.md)
  Give a user on your team access to one or more apps.
- [Replace the list of visible apps for a user](./patch-v1-users-_id_-relationships-visibleapps.md)
  Replace the list of apps a user on your team can see.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-users-_id_-relationships-visibleapps)*