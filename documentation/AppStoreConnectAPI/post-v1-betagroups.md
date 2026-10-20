# Create a beta group

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a beta group associated with an app, optionally enabling TestFlight public links.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaGroups`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaGroupCreateRequest`

## Responses

- `201` Created (`BetaGroupResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting Beta Groups
- [Modify a beta group](./patch-v1-betagroups-_id_.md)
  Modify a beta group’s metadata, including changing its TestFlight public link status.
- [Delete a beta group](./delete-v1-betagroups-_id_.md)
  Delete a beta group and remove beta tester access to associated builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betagroups)*