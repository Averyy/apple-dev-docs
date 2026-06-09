# Read beta app clip invocation information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific App Clip invocation you configure for testing.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppClipInvocations/{id}`

## Parameters

- `fields[betaAppClipInvocations]` ([string]): Additional fields to include for each Beta App Clip Invocation resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[betaAppClipInvocationLocalizations]` (integer): The number of included Beta App Clip Invocations resources to return if the beta App Clip invocation localizations relationship is included.
- `fields[betaAppClipInvocationLocalizations]` ([string])

## See Also

- [Create an app clip invocation for testers in testflight](post-v1-betaappclipinvocations.md)
  Configure a new App Clip experience that testers launch using the TestFlight app.
- [Modify an app clip invocation you provide to testers](patch-v1-betaappclipinvocations-_id_.md)
  Change an App Clip invocation you make available to testers in the TestFlight app.
- [Delete an app clip invocation for testers in testflight](delete-v1-betaappclipinvocations-_id_.md)
  Delete an App Clip invocation you make available to testers in TestFlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappclipinvocations-_id_)*