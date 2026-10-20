# Create a beta tester

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a beta tester assigned to a group, a build, or an app.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaTesters`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaTesterCreateRequest`

## Responses

- `201` Created (`BetaTesterResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Deleting Beta Testers
- [Delete a beta tester](./delete-v1-betatesters-_id_.md)
  Remove a beta tester’s ability to test all apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betatesters)*