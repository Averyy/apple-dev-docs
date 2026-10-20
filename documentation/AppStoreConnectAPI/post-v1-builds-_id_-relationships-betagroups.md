# Add access for beta groups to a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add or create a beta group to a build to enable testing.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/builds/{id}/relationships/betaGroups`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BuildBetaGroupsLinkagesRequest`

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

### Adding and Removing Build Access
- [Remove access for beta groups to a build](./delete-v1-builds-_id_-relationships-betagroups.md)
  Remove access to a specific build for all beta testers in one or more beta groups.
- [Assign individual testers to a build](./post-v1-builds-_id_-relationships-individualtesters.md)
  Enable a beta tester who is not a part of a beta group to test a build.
- [Remove individual testers from a build](./delete-v1-builds-_id_-relationships-individualtesters.md)
  Remove access to test a specific build from one or more individually assigned testers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-builds-_id_-relationships-betagroups)*