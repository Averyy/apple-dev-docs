# Individually unassign a beta tester from builds

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove an individually assigned beta tester’s ability to test a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaTesters/{id}/relationships/builds`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaTesterBuildsLinkagesRequest`

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

### Assigning Groups and Access
- [Add a beta tester to beta groups](./post-v1-betatesters-_id_-relationships-betagroups.md)
  Add one or more beta testers to a specific beta group.
- [Remove a beta tester from beta groups](./delete-v1-betatesters-_id_-relationships-betagroups.md)
  Remove a specific beta tester from one or more beta groups, revoking their access to test builds associated with those groups.
- [Individually assign a beta tester to builds](./post-v1-betatesters-_id_-relationships-builds.md)
  Individually assign a beta tester to a build.
- [Remove a beta tester’s access to apps](./delete-v1-betatesters-_id_-relationships-apps.md)
  Remove a specific beta tester’s access to test any builds of one or more apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betatesters-_id_-relationships-builds)*