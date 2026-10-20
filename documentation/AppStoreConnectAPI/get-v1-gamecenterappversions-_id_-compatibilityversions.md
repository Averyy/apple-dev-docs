# Read compatibility version information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get compatibility version information for a specific app version.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/{id}/compatibilityVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[gameCenterAppVersions]` ([string]): **Allowed Values**: `enabled`, `compatibilityVersions`, `appStoreVersion`
- `filter[enabled]` ([string])
- `include` ([string]): **Allowed Values**: `compatibilityVersions`, `appStoreVersion`
- `limit` (integer): **Maximum**: `200`
- `limit[compatibilityVersions]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterAppVersionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Game Center app versions
- [Read app versions for a game center detail](./get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [List Game Center app version IDs for a Game Center detail](./get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [Read app version information](./get-v1-gamecenterappversions-_id_.md)
  Read the Game Center enablement state and related app version information.
- [Read the App Store version for an app version](./get-v1-gamecenterappversions-_id_-appstoreversion.md)
  Read the App Store version and related information for an app version.
- [Get the App Store version ID for a Game Center app version](./get-v1-gamecenterappversions-_id_-relationships-appstoreversion.md)
- [List all compatible app version IDs](./get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  List all compatible verisons for an app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterappversions-_id_-compatibilityversions)*