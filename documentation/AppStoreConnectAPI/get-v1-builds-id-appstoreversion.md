# Read the app store version information of a build

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the App Store version of a specific build.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/appStoreVersion`

## Parameters

- `fields[appStoreVersions]` ([string])
- `fields[appStoreVersionExperiments]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])
- `limit[appStoreVersionLocalizations]` (integer)
- `limit[appStoreVersionExperiments]` (integer)
- `include` ([string])
- `fields[appClipDefaultExperiences]` ([string])
- `fields[appStoreVersionSubmissions]` ([string])
- `fields[appStoreReviewDetails]` ([string])
- `fields[apps]` ([string])
- `fields[routingAppCoverages]` ([string])
- `fields[appStoreVersionPhasedReleases]` ([string])
- `fields[builds]` ([string])
- `limit[appStoreVersionExperimentsV2]` (integer)
- `fields[alternativeDistributionPackages]` ([string])
- `fields[gameCenterAppVersions]` ([string])

## See Also

- [List builds](get-v1-builds.md)
  Find and list builds for all apps in App Store Connect.
- [Read build information](get-v1-builds-_id_.md)
  Get information about a specific build.
- [Read the app information of a build](get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the app id of a build](get-v1-builds-_id_-relationships-app.md)
  Get the app ID for a specific build.
- [Get the App Store version ID for a build](get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the prerelease version of a build](get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [Get the prerelease version ID for a build](get-v1-builds-_id_-relationships-prereleaseversion.md)
- [Read Usage Metrics for a Beta Build](get-v1-builds-_id_-metrics-betabuildusages.md)
  Get usage metrics for a specific build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-appstoreversion)*