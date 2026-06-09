# Beta App Localizations

**Framework**: App Store Connect API

Beta test information about apps, specific to a locale.

#### Overview

A `betaAppLocalization` resource represents one localized set of information about an app that is visible to beta testers. When distributing a prerelease app, the TestFlight app on the beta tester’s device displays information such as descriptions, URLs, and privacy policies. The information can be localized for the languages listed in [`App Store localizations`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev656087953).

## Topics

### Getting Localization Information
- [List beta app localizations](get-v1-betaapplocalizations.md)
  Find and list beta app localizations for all apps and locales.
- [Read beta app localization information](get-v1-betaapplocalizations-_id_.md)
  Get localized beta app information for a specific app and locale.
- [Read the app information of a beta app localization](get-v1-betaapplocalizations-_id_-app.md)
  Get the app information associated with a specific beta app localization.
- [Get the app ID for a beta app localization](get-v1-betaapplocalizations-_id_-relationships-app.md)
### Creating, Modifying, and Deleting Localizations
- [Create a beta app localization](post-v1-betaapplocalizations.md)
  Create localized descriptive information for an app.
- [Modify a beta app localization](patch-v1-betaapplocalizations-_id_.md)
  Update the localized information for a specific beta app and locale.
- [Delete a beta app localization](delete-v1-betaapplocalizations-_id_.md)
  Delete a beta app localization associated with an app.
### Objects
- [object BetaAppLocalization](betaapplocalization.md)
  The localized feedback URL, marketing URL, and privacy policy URL shown to TestFlight testers for a specific language.
- [object BetaAppLocalizationCreateRequest](betaapplocalizationcreaterequest.md)
  The request body you use to create a Beta App Localization.
- [object BetaAppLocalizationResponse](betaapplocalizationresponse.md)
  The response body for endpoints that create, read, or modify localized TestFlight app metadata.
- [object BetaAppLocalizationsWithoutIncludesResponse](betaapplocalizationswithoutincludesresponse.md)
  A response containing a list of TestFlight app localizations, without related resources.
- [object BetaAppLocalizationUpdateRequest](betaapplocalizationupdaterequest.md)
  The request body you use to update a Beta App Localization.
- [object BetaAppLocalizationsResponse](betaapplocalizationsresponse.md)
  The response body for endpoints that list localized TestFlight app metadata entries.
- [object BetaAppLocalizationAppLinkageResponse](betaapplocalizationapplinkageresponse.md)

## See Also

- [Prerelease Versions](prerelease-versions.md)
  Platform-specific versions of your app intended for distribution to beta testers.
- [Beta License Agreements](beta-license-agreements.md)
  Beta license agreements for apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-app-localizations)*