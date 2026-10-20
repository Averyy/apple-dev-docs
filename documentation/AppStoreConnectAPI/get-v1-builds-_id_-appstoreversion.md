# Read the app store version information of a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the App Store version of a specific build.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/appStoreVersion`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[appStoreVersionExperiments]` ([string]): **Allowed Values**: `name`, `trafficProportion`, `state`, `reviewRequired`, `startDate`, `endDate`, `appStoreVersion`, `appStoreVersionExperimentTreatments`, `platform`, `app`, `latestControlVersion`, `controlVersions`
- `fields[appStoreVersionLocalizations]` ([string]): **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `limit[appStoreVersionLocalizations]` (integer): **Maximum**: `50`
- `limit[appStoreVersionExperiments]` (integer) *(deprecated)*: **Maximum**: `50`
- `include` ([string]): **Allowed Values**: `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `alternativeDistributionPackage`
- `fields[appClipDefaultExperiences]` ([string]): **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `fields[appStoreVersionSubmissions]` ([string]): **Allowed Values**: `appStoreVersion`
- `fields[appStoreReviewDetails]` ([string]): **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `appStoreVersion`, `appStoreReviewAttachments`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[routingAppCoverages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `uploadOperations`, `assetDeliveryState`, `appStoreVersion`
- `fields[appStoreVersionPhasedReleases]` ([string]): **Allowed Values**: `phasedReleaseState`, `startDate`, `totalPauseDuration`, `currentDayNumber`
- `fields[builds]` ([string]): **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `limit[appStoreVersionExperimentsV2]` (integer): **Maximum**: `50`
- `fields[alternativeDistributionPackages]` ([string]): **Allowed Values**: `sourceFileChecksum`, `versions`
- `fields[gameCenterAppVersions]` ([string]): **Allowed Values**: `enabled`, `compatibilityVersions`, `appStoreVersion`

## Responses

- `200` OK (`AppStoreVersionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Information
- [List builds](./get-v1-builds.md)
  Find and list builds for all apps in App Store Connect.
- [Read build information](./get-v1-builds-_id_.md)
  Get information about a specific build.
- [Read the app information of a build](./get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the app id of a build](./get-v1-builds-_id_-relationships-app.md)
  Get the app ID for a specific build.
- [Get the App Store version ID for a build](./get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the prerelease version of a build](./get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [Get the prerelease version ID for a build](./get-v1-builds-_id_-relationships-prereleaseversion.md)
- [Read Usage Metrics for a Beta Build](./get-v1-builds-_id_-metrics-betabuildusages.md)
  Get usage metrics for a specific build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-appstoreversion)*