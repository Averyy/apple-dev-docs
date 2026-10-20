# Read game center app version information of an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the status of Game Center enablement for an App Store version.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/gameCenterAppVersion`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `include` ([string]): **Allowed Values**: `compatibilityVersions`, `appStoreVersion`
- `fields[gameCenterAppVersions]` ([string]): **Allowed Values**: `enabled`, `compatibilityVersions`, `appStoreVersion`
- `limit[compatibilityVersions]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`GameCenterAppVersionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Game Center app versions
- [Get the Game Center app version ID for an App Store version](./get-v1-appstoreversions-_id_-relationships-gamecenterappversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-gamecenterappversion)*