# Beta App Clip Invocations

**Framework**: App Store Connect API

Manage App Clip experiences for testers in TestFlight.

#### Overview

The `betaAppClipInvocations` resource represents an App Clip experience you make available to testers in TestFlight. Use it to read beta App Clip experience information and to create, update, and delete App Clip experiences for testers. For more information on testing App Clip invocations, see [`Testing the launch experience of your App Clip`](https://developer.apple.com/documentation/appclip/testing-the-launch-experience-of-your-app-clip).

## Topics

### Managing Beta App Clip Invocation
- [Read beta app clip invocation information](get-v1-betaappclipinvocations-_id_.md)
  Get a specific App Clip invocation you configure for testing.
- [Create an app clip invocation for testers in testflight](post-v1-betaappclipinvocations.md)
  Configure a new App Clip experience that testers launch using the TestFlight app.
- [Modify an app clip invocation you provide to testers](patch-v1-betaappclipinvocations-_id_.md)
  Change an App Clip invocation you make available to testers in the TestFlight app.
- [Delete an app clip invocation for testers in testflight](delete-v1-betaappclipinvocations-_id_.md)
  Delete an App Clip invocation you make available to testers in TestFlight.
### Objects
- [object BetaAppClipInvocation](betaappclipinvocation.md)
  A TestFlight URL scheme invocation that allows beta testers to launch an App Clip during testing.
- [object BetaAppClipInvocationResponse](betaappclipinvocationresponse.md)
  A response containing a single TestFlight App Clip invocation URL.
- [object BetaAppClipInvocationCreateRequest](betaappclipinvocationcreaterequest.md)
  The request body you use to create an App Clip invocation for testers.
- [object BetaAppClipInvocationUpdateRequest](betaappclipinvocationupdaterequest.md)
  The request body you use to update a Beta App Clip Invocation.

## See Also

- [Beta App Clip Invocation Localizations](beta-app-clip-invocation-localizations.md)
  Manage beta test information for an App Clip and its invocation, specific to a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-app-clip-invocations)*