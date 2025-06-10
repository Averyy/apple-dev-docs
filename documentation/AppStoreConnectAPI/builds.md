# Builds

**Framework**: App Store Connect API

Manage builds for testers and submit builds for review.

#### Overview

A `builds` resource represents a single build of an app. You must upload builds using Xcode or Transporter. Once App Store Connect processes the build, it will appear as a build resource.

Once the build is in the system, you can use the API to perform actions like:

- Submitting builds for review.
- Individually assigning builds to testers.
- Adding the build to a beta group for testing.

## Topics

### Getting Build Information
- [List Builds](get-v1-builds.md)
  Find and list builds for all apps in App Store Connect.
- [Read Build Information](get-v1-builds-_id_.md)
  Get information about a specific build.
- [Read the App Information of a Build](get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the App Store Version Information of a Build](get-v1-builds-_id_-appstoreversion.md)
  Get the App Store version of a specific build.
- [GET /v1/builds/{id}/relationships/appStoreVersion](get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the Prerelease Version of a Build](get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [GET /v1/builds/{id}/relationships/preReleaseVersion](get-v1-builds-_id_-relationships-prereleaseversion.md)
- [Read usage metrics for a beta build](get-v1-builds-_id_-metrics-betabuildusages.md)
  Get usage metrics for a specific build.
### Modifying Builds
- [Modify a Build](patch-v1-builds-_id_.md)
  Expire a build or change its encryption exemption setting.
- [Assign the App Encryption Declaration for a Build](patch-v1-builds-_id_-relationships-appencryptiondeclaration.md)
  Assign an app encryption declaration to a build.
### Adding and Removing Build Access
- [Add Access for Beta Groups to a Build](post-v1-builds-_id_-relationships-betagroups.md)
  Add or create a beta group to a build to enable testing.
- [Remove Access for Beta Groups to a Build](delete-v1-builds-_id_-relationships-betagroups.md)
  Remove access to a specific build for all beta testers in one or more beta groups.
- [Assign Individual Testers to a Build](post-v1-builds-_id_-relationships-individualtesters.md)
  Enable a beta tester who is not a part of a beta group to test a build.
- [Remove Individual Testers from a Build](delete-v1-builds-_id_-relationships-individualtesters.md)
  Remove access to test a specific build from one or more individually assigned testers.
### Listing Individually Assigned Beta Testers
- [List All Individual Testers for a Build](get-v1-builds-_id_-individualtesters.md)
  Get a list of beta testers individually assigned to a build.
- [Get All Resource IDs of Individual Testers for a Build](get-v1-builds-_id_-relationships-individualtesters.md)
  Get a list of resource IDs of individual testers associated with a build.
### Checking Beta Review Submission Status
- [Read the Beta App Review Submission of a Build](get-v1-builds-_id_-betaappreviewsubmission.md)
  Get the beta app review submission status for a specific build.
- [GET /v1/builds/{id}/relationships/betaAppReviewSubmission](get-v1-builds-_id_-relationships-betaappreviewsubmission.md)
### Getting Information Associated with Builds
- [Read the Build Beta Details Information of a Build](get-v1-builds-_id_-buildbetadetail.md)
  Get the beta test details for a specific build.
- [GET /v1/builds/{id}/relationships/buildBetaDetail](get-v1-builds-_id_-relationships-buildbetadetail.md)
- [Read the App Encryption Declaration of a Build](get-v1-builds-_id_-appencryptiondeclaration.md)
  Read an app encryption declaration associated with a specific build.
- [Get the App Encryption Declaration ID for a Build](get-v1-builds-_id_-relationships-appencryptiondeclaration.md)
  Get the beta app encryption declaration resource ID associated with a build.
- [List All Beta Build Localizations of a Build](get-v1-builds-_id_-betabuildlocalizations.md)
  Get a list of localized beta test information for a specific build.
- [GET /v1/builds/{id}/relationships/betaBuildLocalizations](get-v1-builds-_id_-relationships-betabuildlocalizations.md)
- [List All Diagnostic Signatures for a Build](get-v1-builds-_id_-diagnosticsignatures.md)
  List the aggregate backtrace signatures captured for a specific build.
- [List All Icons for a Build](get-v1-builds-_id_-icons.md)
  List all the icons for various platforms delivered with a build.
- [GET /v1/builds/{id}/relationships/icons](get-v1-builds-_id_-relationships-icons.md)
- [GET /v1/builds/{id}/relationships/diagnosticSignatures](get-v1-builds-_id_-relationships-diagnosticsignatures.md)
- [GET /v1/builds/{id}/relationships/appStoreVersion](get-v1-builds-_id_-relationships-appstoreversion.md)
### Objects
- [object Build](build.md)
  The data structure that represents a Builds resource.
- [object BuildResponse](buildresponse.md)
  A response that contains a single Builds resource.
- [object BuildWithoutIncludesResponse](buildwithoutincludesresponse.md)
- [object BuildsResponse](buildsresponse.md)
  A response that contains a list of Builds resources.
- [object BuildsWithoutIncludesResponse](buildswithoutincludesresponse.md)
- [object BuildUpdateRequest](buildupdaterequest.md)
  The request body you use to update a Build.
- [object BuildAppEncryptionDeclarationLinkageRequest](buildappencryptiondeclarationlinkagerequest.md)
  The request body you use to attach an app encryption declaration to a build.
- [object BuildAppEncryptionDeclarationLinkageResponse](buildappencryptiondeclarationlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object BuildIndividualTestersLinkagesRequest](buildindividualtesterslinkagesrequest.md)
  A request body you use to add or remove a build from multiple beta groups.
- [object BuildIndividualTestersLinkagesResponse](buildindividualtesterslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BuildBetaGroupsLinkagesRequest](buildbetagroupslinkagesrequest.md)
  A request body you use to add or remove beta groups from a build.
- [object ImageAsset](imageasset.md)
  An image asset, including its height, width, and template URL.
- [object BetaBuildUsagesV1MetricResponse](betabuildusagesv1metricresponse.md)
  A response that contains one or more beta build metric resources.
- [object BuildAppLinkageResponse](buildapplinkageresponse.md)
- [object BuildAppStoreVersionLinkageResponse](buildappstoreversionlinkageresponse.md)
- [object BuildBetaAppReviewSubmissionLinkageResponse](buildbetaappreviewsubmissionlinkageresponse.md)
- [object BuildBetaBuildLocalizationsLinkagesResponse](buildbetabuildlocalizationslinkagesresponse.md)
- [object BuildBetaDetailBuildLinkageResponse](buildbetadetailbuildlinkageresponse.md)
- [object BuildDiagnosticSignaturesLinkagesResponse](builddiagnosticsignatureslinkagesresponse.md)
- [object BuildIconsLinkagesResponse](buildiconslinkagesresponse.md)
- [object BuildPerfPowerMetricsLinkagesResponse](buildperfpowermetricslinkagesresponse.md)
- [object BuildPreReleaseVersionLinkageResponse](buildprereleaseversionlinkageresponse.md)

## See Also

- [Build Bundles](build-bundles.md)
  Read metadata for app and App Clip binaries included in a build you upload to App Store Connect.
- [Build Icons](build-icons.md)
  Get icons from your app’s binary that are uploaded to App Store.
- [App Encryption Declarations](app-encryption-declarations.md)
  View, and assign to builds, the declarations about types of encryption used in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/builds)*