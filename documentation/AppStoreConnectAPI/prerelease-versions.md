# Prerelease Versions

**Framework**: App Store Connect API

Platform-specific versions of your app intended for distribution to beta testers.

#### Overview

A `preReleaseVersions` resource represents a version of your app intended for TestFlight testing, not for release on the store.

## Topics

### Getting Prerelease Version Information
- [List prerelease versions](get-v1-prereleaseversions.md)
  Get a list of prerelease versions for all apps.
- [Read prerelease version information](get-v1-prereleaseversions-_id_.md)
  Get information about a specific prerelease version.
- [Read the app information of a prerelease version](get-v1-prereleaseversions-_id_-app.md)
  Get the app information for a specific prerelease version.
- [Get the app ID for a prerelease version](get-v1-prereleaseversions-_id_-relationships-app.md)
### Getting Build Information
- [List all builds of a prerelease version](get-v1-prereleaseversions-_id_-builds.md)
  Get a list of builds of a specific prerelease version.
- [List build IDs for a prerelease version](get-v1-prereleaseversions-_id_-relationships-builds.md)
### Objects
- [object PrereleaseVersion](prereleaseversion.md)
  A pre-release version associated with a build, representing a development or beta software version before App Store submission.
- [object PrereleaseVersionResponse](prereleaseversionresponse.md)
  The response body for endpoints that read a single prerelease version of an app.
- [object PreReleaseVersionsResponse](prereleaseversionsresponse.md)
  A response containing a list of pre-release versions for an app.
- [object PrereleaseVersionWithoutIncludesResponse](prereleaseversionwithoutincludesresponse.md)
  A response containing a single pre-release version, without related resources.
- [object PreReleaseVersionsWithoutIncludesResponse](prereleaseversionswithoutincludesresponse.md)
  A response containing a list of pre-release versions, without related resources.
- [object AppPreReleaseVersionsLinkagesResponse](appprereleaseversionslinkagesresponse.md)
- [object PrereleaseVersionAppLinkageResponse](prereleaseversionapplinkageresponse.md)
- [object PrereleaseVersionBuildsLinkagesResponse](prereleaseversionbuildslinkagesresponse.md)

## See Also

- [Beta App Localizations](beta-app-localizations.md)
  Beta test information about apps, specific to a locale.
- [Beta License Agreements](beta-license-agreements.md)
  Beta license agreements for apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/prerelease-versions)*