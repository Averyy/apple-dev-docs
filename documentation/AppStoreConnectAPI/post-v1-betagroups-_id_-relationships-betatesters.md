# Add beta testers to a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a specific beta tester to one or more beta groups for beta testing.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaGroups/{id}/relationships/betaTesters`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaGroupBetaTestersLinkagesRequest`

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

### Adding and Removing Builds and Testers
- [Remove beta testers from a beta group](./delete-v1-betagroups-_id_-relationships-betatesters.md)
  Remove a specific beta tester from a one or more beta groups, revoking their access to test builds associated with those groups.
- [Add builds to a beta group](./post-v1-betagroups-_id_-relationships-builds.md)
  Associate builds with a beta group to enable the group to test the builds.
- [Remove builds from a beta group](./delete-v1-betagroups-_id_-relationships-builds.md)
  Remove access to test one or more builds from beta testers in a specific beta group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betagroups-_id_-relationships-betatesters)*