# Create an app clip invocation for testers in testflight

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Configure a new App Clip experience that testers launch using the TestFlight app.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaAppClipInvocations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaAppClipInvocationCreateRequest`

The request body you use to create a beta App Clip invocation.

## Responses

- `201` Created (`BetaAppClipInvocationResponse`, `application/json`): The request completed successfully and a new Beta App Clip Invocations resource has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Beta App Clip Invocation
- [Read beta app clip invocation information](./get-v1-betaappclipinvocations-_id_.md)
  Get a specific App Clip invocation you configure for testing.
- [Modify an app clip invocation you provide to testers](./patch-v1-betaappclipinvocations-_id_.md)
  Change an App Clip invocation you make available to testers in the TestFlight app.
- [Delete an app clip invocation for testers in testflight](./delete-v1-betaappclipinvocations-_id_.md)
  Delete an App Clip invocation you make available to testers in TestFlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betaappclipinvocations)*