# Delete an app clip invocation for testers in testflight

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an App Clip invocation you make available to testers in TestFlight.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaAppClipInvocations/{id}`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Beta App Clip Invocations resource.

## See Also

- [Read beta app clip invocation information](get-v1-betaappclipinvocations-_id_.md)
  Get a specific App Clip invocation you configure for testing.
- [Create an app clip invocation for testers in testflight](post-v1-betaappclipinvocations.md)
  Configure a new App Clip experience that testers launch using the TestFlight app.
- [Modify an app clip invocation you provide to testers](patch-v1-betaappclipinvocations-_id_.md)
  Change an App Clip invocation you make available to testers in the TestFlight app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betaappclipinvocations-_id_)*