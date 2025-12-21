# App Store Versions

**Framework**: App Store Connect API

Manage versions of your app that are available in App Store.

#### Overview

The `appStoreVersions` resource represents the information related to an App Store version of your app. Using this resource, you can:

- Create, modify, or delete a version for your app.
- Read key details for your version, including its App Store state.
- Specify whether to release the version manually or automatically.
- Modify attributes such as your app’s copyright information.

For more information about versions, see [`Create a new version`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version).

## Topics

### Getting App Store Versions
- [List All App Store Versions for an App](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [Read App Store Version Information](get-v1-appstoreversions-_id_.md)
  Get information for a specific app store version.
### Getting App Store Version Experiments
- [List All Experiments for an App Store Version](get-v1-appstoreversions-_id_-appstoreversionexperimentsv2.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiment IDs for an App Store version](get-v1-appstoreversions-_id_-relationships-appstoreversionexperimentsv2.md)
  Get a list of all experiments IDs for an App Store version across all platforms.
- [List All Experiments for an App Store Version v1](get-v1-appstoreversions-_id_-appstoreversionexperiments.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiments IDs for an App Store version v1](get-v1-appstoreversions-_id_-relationships-appstoreversionexperiments.md)
  Get a list of all experiments IDs for an App Store version of an app across all platforms.
### Creating and Modifying App Store Versions
- [Create an App Store Version](post-v1-appstoreversions.md)
  Add a new App Store version or platform to an app.
- [Modify an App Store Version](patch-v1-appstoreversions-_id_.md)
  Update the app store version for a specific app.
- [Delete an App Store Version](delete-v1-appstoreversions-_id_.md)
  Delete an app store version that is associated with an app.
### Attaching a Build to a Version
- [Read the Build Information of an App Store Version](get-v1-appstoreversions-_id_-build.md)
  Get the build that is attached to a specific App Store version.
- [Get the Build ID for an App Store Version](get-v1-appstoreversions-_id_-relationships-build.md)
  Get the ID of the build that is attached to a specific App Store version.
- [Modify the Build for an App Store Version](patch-v1-appstoreversions-_id_-relationships-build.md)
  Change the build that is attached to a specific App Store version.
### Attaching a Default App Clip Experience to a Version
- [Get the Default App Clip Experience for an App Store Version](get-v1-appstoreversions-_id_-appclipdefaultexperience.md)
  Get the default App Clip experience for an App Store version of your app.
- [Get the Default App Clip Experiences Resource ID for an App Store Version](get-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Get the ID of an app’s related default App Clip experience.
- [Modify the Default App Clip Experience of an App Store Version](patch-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Update the relationship between an App Store version and a default App Clip experience.
### Reading Localization Information
- [List All App Store Version Localizations for an App Store Version](get-v1-appstoreversions-_id_-appstoreversionlocalizations.md)
  Get a list of localized, version-level information about an app, for all locales.
- [GET /v1/appStoreVersions/{id}/relationships/appStoreVersionLocalizations](get-v1-appstoreversions-_id_-relationships-appstoreversionlocalizations.md)
### Reading Release and Review Information
- [Read the App Store Version Submission Information of an App Store Version](get-v1-appstoreversions-_id_-appstoreversionsubmission.md)
- [GET /v1/appStoreVersions/{id}/relationships/appStoreVersionSubmission](get-v1-appstoreversions-_id_-relationships-appstoreversionsubmission.md)
- [Read the App Store Review Details Resource Information of an App Store Version](get-v1-appstoreversions-_id_-appstorereviewdetail.md)
  Get the details you provide to App Review so they can test your app.
- [GET /v1/appStoreVersions/{id}/relationships/appStoreReviewDetail](get-v1-appstoreversions-_id_-relationships-appstorereviewdetail.md)
- [Read the App Store Version Phased Release Information of an App Store Version](get-v1-appstoreversions-_id_-appstoreversionphasedrelease.md)
  Read the phased release status and configuration for a version with phased release enabled.
- [GET /v1/appStoreVersions/{id}/relationships/appStoreVersionPhasedRelease](get-v1-appstoreversions-_id_-relationships-appstoreversionphasedrelease.md)
### Reading Declarations
- [Read the Age Rating Declaration Information of an App Store Version](get-v1-appstoreversions-_id_-ageratingdeclaration.md)
  Get the age-related information declared for your app.
- [GET /v1/appStoreVersions/{id}/relationships/ageRatingDeclaration](get-v1-appstoreversions-_id_-relationships-ageratingdeclaration.md)
- [Read the Routing App Coverage Information of an App Store Version](get-v1-appstoreversions-_id_-routingappcoverage.md)
  Get the routing app coverage file that is associated with a specific App Store version
- [GET /v1/appStoreVersions/{id}/relationships/routingAppCoverage](get-v1-appstoreversions-_id_-relationships-routingappcoverage.md)
### Getting Customer Reviews
- [List All Customer Reviews for an App Store Version](get-v1-appstoreversions-_id_-customerreviews.md)
  Get a list of customer reviews for a specific version of your app.
- [GET /v1/appStoreVersions/{id}/relationships/customerReviews](get-v1-appstoreversions-_id_-relationships-customerreviews.md)
### Getting Game Center app versions
- [Read Game Center app version information of an App Store version](get-v1-appstoreversions-_id_-gamecenterappversion.md)
  Get the status of Game Center enablement for an App Store version.
- [GET /v1/appStoreVersions/{id}/relationships/gameCenterAppVersion](get-v1-appstoreversions-_id_-relationships-gamecenterappversion.md)
### Reading Distribution Package Information
- [Read an App Store version’s alternative distribution package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.
- [GET /v1/appStoreVersions/{id}/relationships/alternativeDistributionPackage](get-v1-appstoreversions-_id_-relationships-alternativedistributionpackage.md)
### Objects and Data Types
- [object AppStoreVersionUpdateRequest](appstoreversionupdaterequest.md)
  The request body you use to update an App Store Version.
- [object AgeRatingDeclaration](ageratingdeclaration.md)
  The data structure that represents an Age Rating Declarations resource.
- [object AgeRatingDeclarationWithoutIncludesResponse](ageratingdeclarationwithoutincludesresponse.md)
- [object AppStoreVersion](appstoreversion.md)
  The data structure that represent an App Store Versions resource.
- [object AppStoreVersionResponse](appstoreversionresponse.md)
  A response that contains a single App Store Versions resource.
- [object AppStoreVersionsResponse](appstoreversionsresponse.md)
  A response that contains a list of App Store Version resources.
- [object AppStoreVersionCreateRequest](appstoreversioncreaterequest.md)
  The request body you use to create an App Store Version.
- [object AppStoreVersionBuildLinkageRequest](appstoreversionbuildlinkagerequest.md)
  The request body you use to attach a build to an App Store version.
- [object AppStoreVersionBuildLinkageResponse](appstoreversionbuildlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object AppStoreVersionAppClipDefaultExperienceLinkageRequest](appstoreversionappclipdefaultexperiencelinkagerequest.md)
  The request body you use to attach a default App Clip experience to an App Store version.
- [object AppStoreVersionAppClipDefaultExperienceLinkageResponse](appstoreversionappclipdefaultexperiencelinkageresponse.md)
  A response that contains the ID of a single related Default App Clip Experiences resource.
- [type AppStoreVersionState](appstoreversionstate.md)
  String that represents the state of an app version in the App Store.
- [type AppVersionState](appversionstate.md)
  String that represents the state of an app version.
- [object AppStoreVersionAgeRatingDeclarationLinkageResponse](appstoreversionageratingdeclarationlinkageresponse.md)
- [object AppStoreVersionAlternativeDistributionPackageLinkageResponse](appstoreversionalternativedistributionpackagelinkageresponse.md)
- [object AppStoreVersionAppStoreReviewDetailLinkageResponse](appstoreversionappstorereviewdetaillinkageresponse.md)
- [object AppStoreVersionAppStoreVersionExperimentsLinkagesResponse](appstoreversionappstoreversionexperimentslinkagesresponse.md)
- [object AppStoreVersionAppStoreVersionExperimentsV2LinkagesResponse](appstoreversionappstoreversionexperimentsv2linkagesresponse.md)
- [object AppStoreVersionAppStoreVersionLocalizationsLinkagesResponse](appstoreversionappstoreversionlocalizationslinkagesresponse.md)
- [object AppStoreVersionAppStoreVersionPhasedReleaseLinkageResponse](appstoreversionappstoreversionphasedreleaselinkageresponse.md)
- [object AppStoreVersionAppStoreVersionSubmissionLinkageResponse](appstoreversionappstoreversionsubmissionlinkageresponse.md)
- [object AppStoreVersionCustomerReviewsLinkagesResponse](appstoreversioncustomerreviewslinkagesresponse.md)
- [object AppStoreVersionGameCenterAppVersionLinkageResponse](appstoreversiongamecenterappversionlinkageresponse.md)
- [object AppStoreVersionLocalizationAppPreviewSetsLinkagesResponse](appstoreversionlocalizationapppreviewsetslinkagesresponse.md)
- [object AppStoreVersionLocalizationAppScreenshotSetsLinkagesResponse](appstoreversionlocalizationappscreenshotsetslinkagesresponse.md)
- [object AppStoreVersionRoutingAppCoverageLinkageResponse](appstoreversionroutingappcoveragelinkageresponse.md)

## See Also

- [App Infos](app-infos.md)
  Manage or read the app metadata that applies across all versions of your app.
- [App Info Localizations](app-info-localizations.md)
  Manage the app metadata that is localized and appears on the App Store.
- [App Store Version Localizations](app-store-version-localizations.md)
  Create and maintain version-specific App Store metadata that’s localized.
- [App tags](app-tags.md)
  Read or modify Apple created app tags.
- [Routing App Coverages](routing-app-coverages.md)
  Manage geographic coverage files for apps that use location to provide routing information.
- [Accessibility declarations](accessibility-declarations.md)
  Manage accessibility metadata for your apps per device family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-versions)*