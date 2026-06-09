# Builds

**Framework**: App Store Connect API

Manage builds for testers and submit builds for review.

#### Overview

A `builds` resource represents a single build of an app. You must upload builds using Xcode, Transporter, or the [`Build uploads`](build-uploads.md) resource. Once App Store Connect processes the build, it appears as a build resource.

Once the build is in the system, you can use the API to perform actions like:

- Submitting builds for review.
- Individually assigning builds to testers.
- Adding the build to a beta group for testing.

## Topics

### Getting Build Information
- [List builds](get-v1-builds.md)
  Find and list builds for all apps in App Store Connect.
- [Read build information](get-v1-builds-_id_.md)
  Get information about a specific build.
- [Read the app information of a build](get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the app id of a build](get-v1-builds-_id_-relationships-app.md)
  Get the app ID for a specific build.
- [Read the app store version information of a build](get-v1-builds-_id_-appstoreversion.md)
  Get the App Store version of a specific build.
- [Get the App Store version ID for a build](get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the prerelease version of a build](get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [Get the prerelease version ID for a build](get-v1-builds-_id_-relationships-prereleaseversion.md)
- [Read Usage Metrics for a Beta Build](get-v1-builds-_id_-metrics-betabuildusages.md)
  Get usage metrics for a specific build.
### Modifying Builds
- [Modify a build](patch-v1-builds-_id_.md)
  Expire a build or change its encryption exemption setting.
- [Assign the app encryption declaration for a build](patch-v1-builds-_id_-relationships-appencryptiondeclaration.md)
  Assign an app encryption declaration to a build.
### Adding and Removing Build Access
- [Add access for beta groups to a build](post-v1-builds-_id_-relationships-betagroups.md)
  Add or create a beta group to a build to enable testing.
- [Remove access for beta groups to a build](delete-v1-builds-_id_-relationships-betagroups.md)
  Remove access to a specific build for all beta testers in one or more beta groups.
- [Assign individual testers to a build](post-v1-builds-_id_-relationships-individualtesters.md)
  Enable a beta tester who is not a part of a beta group to test a build.
- [Remove individual testers from a build](delete-v1-builds-_id_-relationships-individualtesters.md)
  Remove access to test a specific build from one or more individually assigned testers.
### Listing Individually Assigned Beta Testers
- [List all individual testers for a build](get-v1-builds-_id_-individualtesters.md)
  Get a list of beta testers individually assigned to a build.
- [Get all resource ids of individual testers for a build](get-v1-builds-_id_-relationships-individualtesters.md)
  Get a list of resource IDs of individual testers associated with a build.
### Checking Beta Review Submission Status
- [Read the beta app review submission of a build](get-v1-builds-_id_-betaappreviewsubmission.md)
  Get the beta app review submission status for a specific build.
- [Get the beta app review submission ID for a build](get-v1-builds-_id_-relationships-betaappreviewsubmission.md)
### Getting Information Associated with Builds
- [Read the build beta details information of a build](get-v1-builds-_id_-buildbetadetail.md)
  Get the beta test details for a specific build.
- [Get the build beta detail ID for a build](get-v1-builds-_id_-relationships-buildbetadetail.md)
- [Read the app encryption declaration of a build](get-v1-builds-_id_-appencryptiondeclaration.md)
  Read an app encryption declaration associated with a specific build.
- [Get the app encryption declaration id for a build](get-v1-builds-_id_-relationships-appencryptiondeclaration.md)
  Get the beta app encryption declaration resource ID associated with a build.
- [List all beta build localizations of a build](get-v1-builds-_id_-betabuildlocalizations.md)
  Get a list of localized beta test information for a specific build.
- [List beta build localization IDs for a build](get-v1-builds-_id_-relationships-betabuildlocalizations.md)
- [List all diagnostic signatures for a build](get-v1-builds-_id_-diagnosticsignatures.md)
  List the aggregate backtrace signatures captured for a specific build.
- [List all icons for a build](get-v1-builds-_id_-icons.md)
  List all the icons for various platforms delivered with a build.
- [List icon IDs for a build](get-v1-builds-_id_-relationships-icons.md)
- [List diagnostic signature IDs for a build](get-v1-builds-_id_-relationships-diagnosticsignatures.md)
- [Get the App Store version ID for a build](get-v1-builds-_id_-relationships-appstoreversion.md)
### Objects and data types
- [object Build](build.md)
  A processed binary uploaded to App Store Connect, ready for TestFlight distribution or App Store submission.
- [object BuildResponse](buildresponse.md)
  The response body for endpoints that read or modify a single build.
- [object BuildWithoutIncludesResponse](buildwithoutincludesresponse.md)
  A response containing a single build, without related resources.
- [object BuildsResponse](buildsresponse.md)
  The response body for endpoints that list builds.
- [object BuildsWithoutIncludesResponse](buildswithoutincludesresponse.md)
  A response containing a list of builds, without related resources.
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
- [type BuildAudienceType](buildaudiencetype.md)
  A string that represents the App Store Connect audience for a build.
- [type DiagnosticInsightDirection](diagnosticinsightdirection.md)
  A string that describes the diagnostic insight direction.
- [type DiagnosticInsightType](diagnosticinsighttype.md)
  A string that desribes the diagnostic insight type.

## See Also

- [Build Bundles](build-bundles.md)
  Read metadata for app and App Clip binaries included in a build you upload to App Store Connect.
- [Build Icons](build-icons.md)
  Get icons from your app’s binary that are uploaded to App Store.
- [Build uploads](build-uploads.md)
  Read metadata for app builds you upload to App Store Connect.
- [App Encryption Declarations](app-encryption-declarations.md)
  View, and assign to builds, the declarations about types of encryption used in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/builds)*