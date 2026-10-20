# Delete a beta app clip invocation localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete localized metadata you configured for an App Clip that testers launch using the TestFlight app.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaAppClipInvocationLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Beta App Clip Invocation Localizations resource.

## Responses

- `204` No Content: The request completed successfully and the specific Beta App Clip Invocation Localizations resource was deleted.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Localizations for Invocations of Beta App Clips
- [Create localized metadata for a beta app clip invocation](./post-v1-betaappclipinvocationlocalizations.md)
  Provide localized metadata for an App Clip experience you make available to testers.
- [Modify localized metadata of an app clip invocation for testers](./patch-v1-betaappclipinvocationlocalizations-_id_.md)
  Change the metadata for an App Clip you make available to testers in the TestFlight app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betaappclipinvocationlocalizations-_id_)*