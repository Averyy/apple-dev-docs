# Get all visible app resource ids for a user

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of app resource IDs to which a user on your team has access.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/users/{id}/relationships/visibleApps`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `limit` (integer): Number of resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`UserVisibleAppsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing, Adding, and Removing App Access
- [List all apps visible to a user](./get-v1-users-_id_-visibleapps.md)
  Get a list of apps that a user on your team can view.
- [Add visible apps to a user](./post-v1-users-_id_-relationships-visibleapps.md)
  Give a user on your team access to one or more apps.
- [Replace the list of visible apps for a user](./patch-v1-users-_id_-relationships-visibleapps.md)
  Replace the list of apps a user on your team can see.
- [Remove visible apps from a user](./delete-v1-users-_id_-relationships-visibleapps.md)
  Remove a user on your team’s access to one or more apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-users-_id_-relationships-visibleapps)*