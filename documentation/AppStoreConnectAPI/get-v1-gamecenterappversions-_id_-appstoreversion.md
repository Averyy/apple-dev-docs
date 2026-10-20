# Read the App Store version for an app version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read the App Store version and related information for an app version.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/{id}/appStoreVersion`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[appClipDefaultExperiences]` ([string]): **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `fields[appStoreReviewDetails]` ([string]): **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `appStoreVersion`, `appStoreReviewAttachments`
- `fields[appStoreVersionExperiments]` ([string]): **Allowed Values**: `name`, `trafficProportion`, `state`, `reviewRequired`, `startDate`, `endDate`, `appStoreVersion`, `appStoreVersionExperimentTreatments`, `platform`, `app`, `latestControlVersion`, `controlVersions`
- `fields[appStoreVersionLocalizations]` ([string]): **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appStoreVersionPhasedReleases]` ([string]): **Allowed Values**: `phasedReleaseState`, `startDate`, `totalPauseDuration`, `currentDayNumber`
- `fields[appStoreVersionSubmissions]` ([string]): **Allowed Values**: `appStoreVersion`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[builds]` ([string]): **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `fields[routingAppCoverages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `uploadOperations`, `assetDeliveryState`, `appStoreVersion`
- `include` ([string]): **Allowed Values**: `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `alternativeDistributionPackage`
- `limit[appStoreVersionExperimentsV2]` (integer): **Maximum**: `50`
- `limit[appStoreVersionExperiments]` (integer) *(deprecated)*: **Maximum**: `50`
- `limit[appStoreVersionLocalizations]` (integer): **Maximum**: `50`
- `fields[alternativeDistributionPackages]` ([string]): **Allowed Values**: `sourceFileChecksum`, `versions`
- `fields[gameCenterAppVersions]` ([string]): **Allowed Values**: `enabled`, `compatibilityVersions`, `appStoreVersion`

## Responses

- `200` OK (`AppStoreVersionResponse`, `application/json`)
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
- [Get the App Store version ID for a Game Center app version](./get-v1-gamecenterappversions-_id_-relationships-appstoreversion.md)
- [Read compatibility version information](./get-v1-gamecenterappversions-_id_-compatibilityversions.md)
  Get compatibility version information for a specific app version.
- [List all compatible app version IDs](./get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  List all compatible verisons for an app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterappversions-_id_-appstoreversion)*