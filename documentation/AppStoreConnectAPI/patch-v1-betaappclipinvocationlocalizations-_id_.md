# Modify localized metadata of an app clip invocation for testers

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Change the metadata for an App Clip you make available to testers in the TestFlight app.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaAppClipInvocationLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Beta App Clip Invocation Localizations resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BetaAppClipInvocationLocalizationUpdateRequest`

The request body you use to update a beta App Clip invocation localization.

## Responses

- `200` OK (`BetaAppClipInvocationLocalizationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Localizations for Invocations of Beta App Clips
- [Create localized metadata for a beta app clip invocation](./post-v1-betaappclipinvocationlocalizations.md)
  Provide localized metadata for an App Clip experience you make available to testers.
- [Delete a beta app clip invocation localization](./delete-v1-betaappclipinvocationlocalizations-_id_.md)
  Delete localized metadata you configured for an App Clip that testers launch using the TestFlight app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betaappclipinvocationlocalizations-_id_)*