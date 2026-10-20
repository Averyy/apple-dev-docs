# Read the App Store version for an app version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the App Store version and related information for an app version.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/{id}/appStoreVersion`

## Parameters

- `fields[appClipDefaultExperiences]` ([string])
- `fields[appStoreReviewDetails]` ([string])
- `fields[appStoreVersionExperiments]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])
- `fields[appStoreVersionPhasedReleases]` ([string])
- `fields[appStoreVersionSubmissions]` ([string])
- `fields[appStoreVersions]` ([string])
- `fields[apps]` ([string])
- `fields[builds]` ([string])
- `fields[routingAppCoverages]` ([string])
- `include` ([string])
- `limit[appStoreVersionExperimentsV2]` (integer)
- `limit[appStoreVersionExperiments]` (integer)
- `limit[appStoreVersionLocalizations]` (integer)
- `fields[alternativeDistributionPackages]` ([string])
- `fields[gameCenterAppVersions]` ([string])

## See Also

- [Read app versions for a game center detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [List Game Center app version IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [Read app version information](get-v1-gamecenterappversions-_id_.md)
  Read the Game Center enablement state and related app version information.
- [Get the App Store version ID for a Game Center app version](get-v1-gamecenterappversions-_id_-relationships-appstoreversion.md)
- [Read compatibility version information](get-v1-gamecenterappversions-_id_-compatibilityversions.md)
  Get compatibility version information for a specific app version.
- [List all compatible app version IDs](get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  List all compatible verisons for an app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterappversions-_id_-appstoreversion)*