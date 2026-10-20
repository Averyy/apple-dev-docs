# List builds

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list builds for all apps in App Store Connect.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds`

## Parameters

### Query Parameters

- `fields[appEncryptionDeclarations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `appDescription`, `createdDate`, `usesEncryption`, `exempt`, `containsProprietaryCryptography`, `containsThirdPartyCryptography`, `availableOnFrenchStore`, `platform`, `uploadedDate`, `documentUrl`, `documentName`, `documentType`, `appEncryptionDeclarationState`, `codeValue`, `app`, `builds`, `appEncryptionDeclarationDocument`
- `fields[apps]` ([string]): Fields to return for included related types.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[betaTesters]` ([string]): Fields to return for included related types.

  **Allowed Values**: `firstName`, `lastName`, `email`, `inviteType`, `state`, `appDevices`, `apps`, `betaGroups`, `builds`
- `fields[builds]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `fields[preReleaseVersions]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `platform`, `builds`, `app`
- `filter[app]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[expired]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[id]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[preReleaseVersion]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[processingState]` ([string]): Attributes, relationships, and IDs by which to filter.

  **Allowed Values**: `PROCESSING`, `FAILED`, `INVALID`, `VALID`
- `filter[version]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`
- `limit[individualTesters]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `version`, `-version`, `uploadedDate`, `-uploadedDate`, `preReleaseVersion`, `-preReleaseVersion`
- `filter[usesNonExemptEncryption]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[preReleaseVersion.version]` ([string]): Attributes, relationships, and IDs by which to filter.
- `fields[buildBetaDetails]` ([string]): Fields to return for included related types.

  **Allowed Values**: `autoNotifyEnabled`, `internalBuildState`, `externalBuildState`, `build`
- `filter[betaGroups]` ([string]): Attributes, relationships, and IDs by which to filter.
- `fields[betaAppReviewSubmissions]` ([string]): Fields to return for included related types.

  **Allowed Values**: `betaReviewState`, `submittedDate`, `build`
- `filter[betaAppReviewSubmission.betaReviewState]` ([string]): Attributes, relationships, and IDs by which to filter.

  **Allowed Values**: `WAITING_FOR_REVIEW`, `IN_REVIEW`, `REJECTED`, `APPROVED`
- `fields[betaBuildLocalizations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `whatsNew`, `locale`, `build`
- `limit[betaBuildLocalizations]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `limit[icons]` (integer): **Maximum**: `50`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[buildIcons]` ([string]): **Allowed Values**: `iconAsset`, `iconType`, `masked`, `name`
- `filter[appStoreVersion]` ([string])
- `filter[preReleaseVersion.platform]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[buildAudienceType]` ([string]): **Allowed Values**: `INTERNAL_ONLY`, `APP_STORE_ELIGIBLE`
- `limit[buildBundles]` (integer): **Maximum**: `50`
- `limit[betaGroups]` (integer): **Maximum**: `50`
- `exists[usesNonExemptEncryption]` (boolean)
- `fields[betaGroups]` ([string]): **Allowed Values**: `name`, `createdDate`, `isInternalGroup`, `hasAccessToAllBuilds`, `publicLinkEnabled`, `publicLinkId`, `publicLinkLimitEnabled`, `publicLinkLimit`, `publicLink`, `feedbackEnabled`, `iosBuildsAvailableForAppleSiliconMac`, `iosBuildsAvailableForAppleVision`, `app`, `builds`, `betaTesters`, `betaRecruitmentCriteria`, `betaRecruitmentCriterionCompatibleBuildCheck`
- `fields[buildBundles]` ([string]): **Allowed Values**: `bundleId`, `bundleType`, `sdkBuild`, `platformBuild`, `fileName`, `hasSirikit`, `hasOnDemandResources`, `hasPrerenderedIcon`, `usesLocationServices`, `isIosBuildMacAppStoreCompatible`, `includesSymbols`, `dSYMUrl`, `supportedArchitectures`, `requiredCapabilities`, `deviceProtocols`, `locales`, `entitlements`, `baDownloadAllowance`, `baMaxInstallSize`, `minimumOsVersion`, `appClipDomainCacheStatus`, `appClipDomainDebugStatus`, `betaAppClipInvocations`, `buildBundleFileSizes`
- `fields[buildUploads]` ([string]): **Allowed Values**: `cfBundleShortVersionString`, `cfBundleVersion`, `createdDate`, `state`, `platform`, `uploadedDate`, `build`, `assetFile`, `assetDescriptionFile`, `assetSpiFile`, `buildUploadFiles`

## Responses

- `200` OK (`BuildsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Information
- [Read build information](./get-v1-builds-_id_.md)
  Get information about a specific build.
- [Read the app information of a build](./get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the app id of a build](./get-v1-builds-_id_-relationships-app.md)
  Get the app ID for a specific build.
- [Read the app store version information of a build](./get-v1-builds-_id_-appstoreversion.md)
  Get the App Store version of a specific build.
- [Get the App Store version ID for a build](./get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the prerelease version of a build](./get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [Get the prerelease version ID for a build](./get-v1-builds-_id_-relationships-prereleaseversion.md)
- [Read Usage Metrics for a Beta Build](./get-v1-builds-_id_-metrics-betabuildusages.md)
  Get usage metrics for a specific build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds)*