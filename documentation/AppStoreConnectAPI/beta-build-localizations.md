# Beta Build Localizations

**Framework**: App Store Connect API

Beta test information about builds, specific to a locale.

#### Overview

A `betaBuildLocalizations` resource represents the localized content that appears in the “What’s New” text in TestFlight. You should change this text for every build.

## Topics

### Getting Build Information
- [List beta build localizations](get-v1-betabuildlocalizations.md)
  Find and list beta build localizations currently associated with apps.
- [Read beta build localization information](get-v1-betabuildlocalizations-_id_.md)
  Get a specific beta build localization resource.
- [Read the build information of a beta build localization](get-v1-betabuildlocalizations-_id_-build.md)
  Get the build information for a specific beta build localization.
- [Get the build ID for a beta build localization](get-v1-betabuildlocalizations-_id_-relationships-build.md)
### Creating, Modifying, and Deleting Beta Build Localizations
- [Create a beta build localization](post-v1-betabuildlocalizations.md)
  Create localized What’s New text for a build.
- [Modify a beta build localization](patch-v1-betabuildlocalizations-_id_.md)
  Update the localized What’s New text for a specific beta build and locale.
- [Delete a beta build localization](delete-v1-betabuildlocalizations-_id_.md)
  Delete a specific beta build localization associated with a build.
### Objects
- [object BetaBuildLocalization](betabuildlocalization.md)
  The localized ‘What’s New’ text shown to TestFlight testers in a specific language for a build.
- [object BetaBuildLocalizationResponse](betabuildlocalizationresponse.md)
  The response body for endpoints that create, read, or modify localized TestFlight build metadata.
- [object BetaBuildLocalizationsWithoutIncludesResponse](betabuildlocalizationswithoutincludesresponse.md)
  A response containing a list of TestFlight build localizations, without related resources.
- [object BetaBuildLocalizationCreateRequest](betabuildlocalizationcreaterequest.md)
  The request body you use to create a Beta Build Localization.
- [object BetaBuildLocalizationUpdateRequest](betabuildlocalizationupdaterequest.md)
  The request body you use to update a Beta Build Localization.
- [object BetaBuildLocalizationsResponse](betabuildlocalizationsresponse.md)
  The response body for endpoints that list localized TestFlight build metadata entries.
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