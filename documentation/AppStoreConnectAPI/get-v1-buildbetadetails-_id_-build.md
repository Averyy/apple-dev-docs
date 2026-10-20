# Read the build information of a build beta detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the build information for a specific build beta details resource.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildBetaDetails/{id}/build`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `fields[builds]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `fields[appEncryptionDeclarations]` ([string]): **Allowed Values**: `appDescription`, `createdDate`, `usesEncryption`, `exempt`, `containsProprietaryCryptography`, `containsThirdPartyCryptography`, `availableOnFrenchStore`, `platform`, `uploadedDate`, `documentUrl`, `documentName`, `documentType`, `appEncryptionDeclarationState`, `codeValue`, `app`, `builds`, `appEncryptionDeclarationDocument`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[betaAppReviewSubmissions]` ([string]): **Allowed Values**: `betaReviewState`, `submittedDate`, `build`
- `fields[betaBuildLocalizations]` ([string]): **Allowed Values**: `whatsNew`, `locale`, `build`
- `fields[betaGroups]` ([string]): **Allowed Values**: `name`, `createdDate`, `isInternalGroup`, `hasAccessToAllBuilds`, `publicLinkEnabled`, `publicLinkId`, `publicLinkLimitEnabled`, `publicLinkLimit`, `publicLink`, `feedbackEnabled`, `iosBuildsAvailableForAppleSiliconMac`, `iosBuildsAvailableForAppleVision`, `app`, `builds`, `betaTesters`, `betaRecruitmentCriteria`, `betaRecruitmentCriterionCompatibleBuildCheck`
- `fields[betaTesters]` ([string]): **Allowed Values**: `firstName`, `lastName`, `email`, `inviteType`, `state`, `appDevices`, `apps`, `betaGroups`, `builds`
- `fields[buildBetaDetails]` ([string]): **Allowed Values**: `autoNotifyEnabled`, `internalBuildState`, `externalBuildState`, `build`
- `fields[buildBundles]` ([string]): **Allowed Values**: `bundleId`, `bundleType`, `sdkBuild`, `platformBuild`, `fileName`, `hasSirikit`, `hasOnDemandResources`, `hasPrerenderedIcon`, `usesLocationServices`, `isIosBuildMacAppStoreCompatible`, `includesSymbols`, `dSYMUrl`, `supportedArchitectures`, `requiredCapabilities`, `deviceProtocols`, `locales`, `entitlements`, `baDownloadAllowance`, `baMaxInstallSize`, `minimumOsVersion`, `appClipDomainCacheStatus`, `appClipDomainDebugStatus`, `betaAppClipInvocations`, `buildBundleFileSizes`
- `fields[buildIcons]` ([string]): **Allowed Values**: `iconAsset`, `iconType`, `masked`, `name`
- `fields[buildUploads]` ([string]): **Allowed Values**: `cfBundleShortVersionString`, `cfBundleVersion`, `createdDate`, `state`, `platform`, `uploadedDate`, `build`, `assetFile`, `assetDescriptionFile`, `assetSpiFile`, `buildUploadFiles`
- `fields[preReleaseVersions]` ([string]): **Allowed Values**: `version`, `platform`, `builds`, `app`
- `include` ([string]): **Allowed Values**: `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`
- `limit[betaBuildLocalizations]` (integer): **Maximum**: `50`
- `limit[betaGroups]` (integer): **Maximum**: `50`
- `limit[buildBundles]` (integer): **Maximum**: `50`
- `limit[icons]` (integer): **Maximum**: `50`
- `limit[individualTesters]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`BuildResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Beta Details Information
- [List build beta details](./get-v1-buildbetadetails.md)
  Find and list build beta details for all builds.
- [Read build beta detail information](./get-v1-buildbetadetails-_id_.md)
  Get a specific build beta details resource.
- [Get the build ID for a build beta detail](./get-v1-buildbetadetails-_id_-relationships-build.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-buildbetadetails-_id_-build)*