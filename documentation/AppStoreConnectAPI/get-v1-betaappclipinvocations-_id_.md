# Read beta app clip invocation information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a specific App Clip invocation you configure for testing.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppClipInvocations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Beta App Clip Invocations resource.

### Query Parameters

- `fields[betaAppClipInvocations]` ([string]): Additional fields to include for each Beta App Clip Invocation resource returned by the response.

  **Allowed Values**: `url`, `betaAppClipInvocationLocalizations`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `betaAppClipInvocationLocalizations`
- `limit[betaAppClipInvocationLocalizations]` (integer): The number of included Beta App Clip Invocations resources to return if the beta App Clip invocation localizations relationship is included.

  **Maximum**: `50`
- `fields[betaAppClipInvocationLocalizations]` ([string]): **Allowed Values**: `title`, `locale`

## Responses

- `200` OK (`BetaAppClipInvocationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Beta App Clip Invocation
- [Create an app clip invocation for testers in testflight](./post-v1-betaappclipinvocations.md)
  Configure a new App Clip experience that testers launch using the TestFlight app.
- [Modify an app clip invocation you provide to testers](./patch-v1-betaappclipinvocations-_id_.md)
  Change an App Clip invocation you make available to testers in the TestFlight app.
- [Delete an app clip invocation for testers in testflight](./delete-v1-betaappclipinvocations-_id_.md)
  Delete an App Clip invocation you make available to testers in TestFlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappclipinvocations-_id_)*