# Read app store version information for a default app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get App Store Version information for a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipDefaultExperiences/{id}/releaseWithAppStoreVersion`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the default App Clip experience resource ID from the [`List all default app clip experiences for an app clip`](./get-v1-appclips-_id_-appclipdefaultexperiences.md) response.

### Query Parameters

- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

  **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.

  **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `alternativeDistributionPackage`
- `limit[appStoreVersionLocalizations]` (integer): The maximum number of related App Store version localizations resources to return.

  **Maximum**: `50`
- `fields[appStoreVersionExperiments]` ([string]): Additional fields to include for each App Store version experiment resource returned by the response.

  **Allowed Values**: `name`, `trafficProportion`, `state`, `reviewRequired`, `startDate`, `endDate`, `appStoreVersion`, `appStoreVersionExperimentTreatments`, `platform`, `app`, `latestControlVersion`, `controlVersions`
- `limit[appStoreVersionExperiments]` (integer) *(deprecated)*: The maximum number of related App Store version experiments resources to return.

  **Maximum**: `50`
- `fields[appStoreVersionSubmissions]` ([string]): Additional fields to include for each App Store version submission resource returned by the response.

  **Allowed Values**: `appStoreVersion`
- `fields[appStoreReviewDetails]` ([string]): Additional fields to include for each App Store review detail resource returned by the response.

  **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `appStoreVersion`, `appStoreReviewAttachments`
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[routingAppCoverages]` ([string]): Additional fields to include for each routing app coverage resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `uploadOperations`, `assetDeliveryState`, `appStoreVersion`
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each default App Clip experience resource returned by the response.

  **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `fields[appStoreVersionPhasedReleases]` ([string]): Additional fields to include for each App Store version phased release resource returned by the response.

  **Allowed Values**: `phasedReleaseState`, `startDate`, `totalPauseDuration`, `currentDayNumber`
- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `limit[appStoreVersionExperimentsV2]` (integer): The maximum number of related App Store version experiments (v2) resources to return.

  **Maximum**: `50`
- `fields[alternativeDistributionPackages]` ([string]): Additional fields to include for each alternative distribution package resource returned by the response.

  **Allowed Values**: `sourceFileChecksum`, `versions`
- `fields[gameCenterAppVersions]` ([string]): **Allowed Values**: `enabled`, `compatibilityVersions`, `appStoreVersion`

## Responses

- `200` OK (`AppStoreVersionResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Default App Clip Experience Information
- [Read default app clip experience information](./get-v1-appclipdefaultexperiences-_id_.md)
  Get a specific default App Clip experience.
- [Read the app store review detail for a default app clip experience](./get-v1-appclipdefaultexperiences-_id_-appclipappstorereviewdetail.md)
  Get App Store Review details for a specific default App Clip experience.
- [Get the App Store review detail ID for an App Clip default experience](./get-v1-appclipdefaultexperiences-_id_-relationships-appclipappstorereviewdetail.md)
- [Read localization information for a default app clip experience](./get-v1-appclipdefaultexperiences-_id_-appclipdefaultexperiencelocalizations.md)
  Get localized metadata that appears on the App Clip card for a specific default App Clip experience.
- [List localization IDs for an App Clip default experience](./get-v1-appclipdefaultexperiences-_id_-relationships-appclipdefaultexperiencelocalizations.md)
- [Get the app store versions resource id for a default app clip experience](./get-v1-appclipdefaultexperiences-_id_-relationships-releasewithappstoreversion.md)
  Get IDs for App Store Versions related to a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipdefaultexperiences-_id_-releasewithappstoreversion)*