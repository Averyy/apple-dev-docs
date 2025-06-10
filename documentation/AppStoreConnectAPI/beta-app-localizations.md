# Beta App Localizations

**Framework**: App Store Connect API

Beta test information about apps, specific to a locale.

#### Overview

A `betaAppLocalization` resource represents one localized set of information about an app that is visible to beta testers. When distributing a prerelease app, the TestFlight app on the beta tester’s device displays information such as descriptions, URLs, and privacy policies. The information can be localized for the languages listed in [`App Store localizations`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev656087953).

## Topics

### Getting Localization Information
- [List Beta App Localizations](get-v1-betaapplocalizations.md)
  Find and list beta app localizations for all apps and locales.
- [Read Beta App Localization Information](get-v1-betaapplocalizations-_id_.md)
  Get localized beta app information for a specific app and locale.
- [Read the App Information of a Beta App Localization](get-v1-betaapplocalizations-_id_-app.md)
  Get the app information associated with a specific beta app localization.
- [GET /v1/betaAppLocalizations/{id}/relationships/app](get-v1-betaapplocalizations-_id_-relationships-app.md)
### Creating, Modifying, and Deleting Localizations
- [Create a Beta App Localization](post-v1-betaapplocalizations.md)
  Create localized descriptive information for an app.
- [Modify a Beta App Localization](patch-v1-betaapplocalizations-_id_.md)
  Update the localized information for a specific beta app and locale.
- [Delete a Beta App Localization](delete-v1-betaapplocalizations-_id_.md)
  Delete a beta app localization associated with an app.
### Objects
- [object BetaAppLocalization](betaapplocalization.md)
  The data structure that represents a Beta App Localizations resource.
- [object BetaAppLocalizationCreateRequest](betaapplocalizationcreaterequest.md)
  The request body you use to create a Beta App Localization.
- [object BetaAppLocalizationResponse](betaapplocalizationresponse.md)
  A response that contains a single Beta App Localizations resource.
- [object BetaAppLocalizationsWithoutIncludesResponse](betaapplocalizationswithoutincludesresponse.md)
- [object BetaAppLocalizationUpdateRequest](betaapplocalizationupdaterequest.md)
  The request body you use to update a Beta App Localization.
- [object BetaAppLocalizationsResponse](betaapplocalizationsresponse.md)
  A response that contains a list of Beta App Localization resources.
- [object BetaAppLocalizationAppLinkageResponse](betaapplocalizationapplinkageresponse.md)

## See Also

- [Prerelease Versions](prerelease-versions.md)
  Platform-specific versions of your app intended for distribution to beta testers.
- [Beta License Agreements](beta-license-agreements.md)
  Beta license agreements for apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-app-localizations)*