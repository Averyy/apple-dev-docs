# Create localized metadata for a beta app clip invocation

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Provide localized metadata for an App Clip experience you make available to testers.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/betaAppClipInvocationLocalizations`

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaAppClipInvocationLocalizationCreateRequest`

The request body you use to create a beta App Clip invocation localization.

## Responses

- `201` Created (`BetaAppClipInvocationLocalizationResponse`, `application/json`): The request completed successfully and a new Beta App Clip Invocation Localizations resource has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Localizations for Invocations of Beta App Clips
- [Modify localized metadata of an app clip invocation for testers](./patch-v1-betaappclipinvocationlocalizations-_id_.md)
  Change the metadata for an App Clip you make available to testers in the TestFlight app.
- [Delete a beta app clip invocation localization](./delete-v1-betaappclipinvocationlocalizations-_id_.md)
  Delete localized metadata you configured for an App Clip that testers launch using the TestFlight app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-betaappclipinvocationlocalizations)*