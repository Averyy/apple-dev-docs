# Beta Build Localizations

**Framework**: App Store Connect API

Beta test information about builds, specific to a locale.

#### Overview

A `betaBuildLocalizations` resource represents the localized content that appears in the “What’s New” text in TestFlight. You should change this text for every build.

## Topics

### Getting Build Information
- [List Beta Build Localizations](get-v1-betabuildlocalizations.md)
  Find and list beta build localizations currently associated with apps.
- [Read Beta Build Localization Information](get-v1-betabuildlocalizations-_id_.md)
  Get a specific beta build localization resource.
- [Read the Build Information of a Beta Build Localization](get-v1-betabuildlocalizations-_id_-build.md)
  Get the build information for a specific beta build localization.
- [GET /v1/betaBuildLocalizations/{id}/relationships/build](get-v1-betabuildlocalizations-_id_-relationships-build.md)
### Creating, Modifying, and Deleting Beta Build Localizations
- [Create a Beta Build Localization](post-v1-betabuildlocalizations.md)
  Create localized What’s New text for a build.
- [Modify a Beta Build Localization](patch-v1-betabuildlocalizations-_id_.md)
  Update the localized What’s New text for a specific beta build and locale.
- [Delete a Beta Build Localization](delete-v1-betabuildlocalizations-_id_.md)
  Delete a specific beta build localization associated with a build.
### Objects
- [object BetaBuildLocalization](betabuildlocalization.md)
  The data structure that represents a Beta Build Localizations resource.
- [object BetaBuildLocalizationResponse](betabuildlocalizationresponse.md)
  A response that contains a single Beta Build Localizations resource.
- [object BetaBuildLocalizationsWithoutIncludesResponse](betabuildlocalizationswithoutincludesresponse.md)
- [object BetaBuildLocalizationCreateRequest](betabuildlocalizationcreaterequest.md)
  The request body you use to create a Beta Build Localization.
- [object BetaBuildLocalizationUpdateRequest](betabuildlocalizationupdaterequest.md)
  The request body you use to update a Beta Build Localization.
- [object BetaBuildLocalizationsResponse](betabuildlocalizationsresponse.md)
  A response that contains a list of Beta Build Localization resources.
- [object BetaBuildLocalizationBuildLinkageResponse](betabuildlocalizationbuildlinkageresponse.md)

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Build Beta Details](build-beta-details.md)
  TestFlight-specific information about beta builds.
- [Build Beta Notifications](build-beta-notifications.md)
  Requests to send notifications to all assigned testers that builds are ready for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-build-localizations)*