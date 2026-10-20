# Get all build ids in a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of build resource IDs in a specific beta group.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaGroups/{id}/relationships/builds`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `limit` (integer): Number of resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`BetaGroupBuildsLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Build and Beta Tester Information
- [List all builds for a beta group](./get-v1-betagroups-_id_-builds.md)
  Get a list of builds associated with a specific beta group.
- [List all beta testers in a beta group](./get-v1-betagroups-_id_-betatesters.md)
  Get a list of beta testers contained in a specific beta group.
- [Get all beta tester ids in a beta group](./get-v1-betagroups-_id_-relationships-betatesters.md)
  Get a list of the beta tester resource IDs in a specific beta group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betagroups-_id_-relationships-builds)*