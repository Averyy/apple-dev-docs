# Delete a beta app clip invocation localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete localized metadata you configured for an App Clip that testers launch using the TestFlight app.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaAppClipInvocationLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Beta App Clip Invocation Localizations resource.

## See Also

- [Create localized metadata for a beta app clip invocation](post-v1-betaappclipinvocationlocalizations.md)
  Provide localized metadata for an App Clip experience you make available to testers.
- [Modify localized metadata of an app clip invocation for testers](patch-v1-betaappclipinvocationlocalizations-_id_.md)
  Change the metadata for an App Clip you make available to testers in the TestFlight app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betaappclipinvocationlocalizations-_id_)*