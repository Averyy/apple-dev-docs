# Beta App Clip Invocation Localizations

**Framework**: App Store Connect API

Manage beta test information for an App Clip and its invocation, specific to a locale.

#### Overview

The `betaAppClipInvocationLocalizations` resource represents the localization information of an App Clip you distribute to testers that’s specific to a locale. Use this resource to set the text that appears in the App Clips section of a build in the TestFlight app.

For more information on testing App Clip invocations, see [`Testing the launch experience of your App Clip`](https://developer.apple.com/documentation/appclip/testing-the-launch-experience-of-your-app-clip).

## Topics

### Managing Localizations for Invocations of Beta App Clips
- [Create localized metadata for a beta app clip invocation](post-v1-betaappclipinvocationlocalizations.md)
  Provide localized metadata for an App Clip experience you make available to testers.
- [Modify localized metadata of an app clip invocation for testers](patch-v1-betaappclipinvocationlocalizations-_id_.md)
  Change the metadata for an App Clip you make available to testers in the TestFlight app.
- [Delete a beta app clip invocation localization](delete-v1-betaappclipinvocationlocalizations-_id_.md)
  Delete localized metadata you configured for an App Clip that testers launch using the TestFlight app.
### Objects
- [object BetaAppClipInvocationLocalization](betaappclipinvocationlocalization.md)
  The localized title displayed to beta testers for a specific App Clip invocation.
- [object BetaAppClipInvocationLocalizationCreateRequest](betaappclipinvocationlocalizationcreaterequest.md)
  The request body you use to create a Beta App Clip Localization.
- [object BetaAppClipInvocationLocalizationUpdateRequest](betaappclipinvocationlocalizationupdaterequest.md)
  The request body you use to update localized text that appears on the App Clip card for testers.
- [object BetaAppClipInvocationLocalizationResponse](betaappclipinvocationlocalizationresponse.md)
  A response containing a single localized title for a beta App Clip invocation.

## See Also

- [Beta App Clip Invocations](beta-app-clip-invocations.md)
  Manage App Clip experiences for testers in TestFlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-app-clip-invocation-localizations)*