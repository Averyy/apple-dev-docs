# Modify an app clip invocation you provide to testers

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change an App Clip invocation you make available to testers in the TestFlight app.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaAppClipInvocations/{id}`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Beta App Clip Invocations resource.

## Request Body

The request body you use to update a beta App Clip invocation.

## See Also

- [Read beta app clip invocation information](get-v1-betaappclipinvocations-_id_.md)
  Get a specific App Clip invocation you configure for testing.
- [Create an app clip invocation for testers in testflight](post-v1-betaappclipinvocations.md)
  Configure a new App Clip experience that testers launch using the TestFlight app.
- [Delete an app clip invocation for testers in testflight](delete-v1-betaappclipinvocations-_id_.md)
  Delete an App Clip invocation you make available to testers in TestFlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betaappclipinvocations-_id_)*