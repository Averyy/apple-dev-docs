# Build Beta Details

**Framework**: App Store Connect API

TestFlight-specific information about beta builds.

#### Overview

Every build has a `buildBetaDetails` resource that represents TestFlight-specific information about the build.

## Topics

### Getting Build Beta Details Information
- [List build beta details](get-v1-buildbetadetails.md)
  Find and list build beta details for all builds.
- [Read build beta detail information](get-v1-buildbetadetails-_id_.md)
  Get a specific build beta details resource.
- [Read the build information of a build beta detail](get-v1-buildbetadetails-_id_-build.md)
  Get the build information for a specific build beta details resource.
- [Get the build ID for a build beta detail](get-v1-buildbetadetails-_id_-relationships-build.md)
### Modifying Build Beta Details
- [Modify a build beta detail](patch-v1-buildbetadetails-_id_.md)
  Update beta test details for a specific build.
### Objects and Data Types
- [object BuildBetaDetail](buildbetadetail.md)
  The TestFlight distribution settings for a build, including whether it is available for external testing.
- [object BuildBetaDetailUpdateRequest](buildbetadetailupdaterequest.md)
  The request body you use to update a Build Data Detail.
- [object BuildBetaDetailResponse](buildbetadetailresponse.md)
  The response body for endpoints that read or modify beta testing details for a build.
- [object BuildBetaDetailsResponse](buildbetadetailsresponse.md)
  The response body for endpoints that list beta testing details across builds.
- [type ExternalBetaState](externalbetastate.md)
  String that represents a build’s availability for external testing.
- [type InternalBetaState](internalbetastate.md)
  String that represents a build’s availability for internal testing.
- [object BuildBuildBetaDetailLinkageResponse](buildbuildbetadetaillinkageresponse.md)
- [object BuildBundleAppClipDomainCacheStatusLinkageResponse](buildbundleappclipdomaincachestatuslinkageresponse.md)
- [object BuildBundleAppClipDomainDebugStatusLinkageResponse](buildbundleappclipdomaindebugstatuslinkageresponse.md)
- [object BuildBundleBetaAppClipInvocationsLinkagesResponse](buildbundlebetaappclipinvocationslinkagesresponse.md)
- [object BuildBundleBuildBundleFileSizesLinkagesResponse](buildbundlebuildbundlefilesizeslinkagesresponse.md)

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Beta Build Localizations](beta-build-localizations.md)
  Beta test information about builds, specific to a locale.
- [Build Beta Notifications](build-beta-notifications.md)
  Requests to send notifications to all assigned testers that builds are ready for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-beta-details)*