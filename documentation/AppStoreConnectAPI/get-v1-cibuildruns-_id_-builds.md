# List all builds xcode cloud created in app store connect

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List All App Store Connect and TestFlight Builds when it performed a build.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/{id}/builds`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Build Runs resource.

### Query Parameters

- `fields[betaBuildLocalizations]` ([string]): Additional fields to include for each Builds resource returned by the response.

  **Allowed Values**: `whatsNew`, `locale`, `build`
- `fields[betaTesters]` ([string]): Additional fields to include for each Builds resource returned by the response.

  **Allowed Values**: `firstName`, `lastName`, `email`, `inviteType`, `state`, `appDevices`, `apps`, `betaGroups`, `builds`
- `fields[buildIcons]` ([string]): Additional fields to include for each Builds resource returned by the response.

  **Allowed Values**: `iconAsset`, `iconType`, `masked`, `name`
- `fields[builds]` ([string]): Additional fields to include for each Builds resource returned by the response.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `filter[appStoreVersion]` ([string]): Filter the returned builds using the ID of the related App Store Versions resource.
- `filter[app]` ([string]): Filter the returned builds using the ID of the related Apps resource.
- `filter[betaAppReviewSubmission.betaReviewState]` ([string]): Filter the returned builds using the beta review state attribute.

  **Allowed Values**: `WAITING_FOR_REVIEW`, `IN_REVIEW`, `REJECTED`, `APPROVED`
- `filter[betaGroups]` ([string]): Filter the returned builds using the ID of the related Beta Groups resource.
- `filter[expired]` ([string]): Filter the returned builds using the expired attribute.
- `filter[id]` ([string]): Filter the returned builds using the ID of the Builds resource.
- `filter[preReleaseVersion.platform]` ([string]): Filter the returned builds using the platform attribute of the Pre-Release Versions resource.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[preReleaseVersion.version]` ([string]): Filter the returned builds using the version attribute of the Pre-Release Versions resource.
- `filter[preReleaseVersion]` ([string]): Filter the returned builds using the ID of the related Pre-Release Versions resource.
- `filter[processingState]` ([string]): Filter the returned builds using the processing state attribute.

  **Allowed Values**: `PROCESSING`, `FAILED`, `INVALID`, `VALID`
- `filter[usesNonExemptEncryption]` ([string]): Filter the returned builds using the uses nonexempt encryption  attribute.
- `filter[version]` ([string]): Filter the returned builds using the version attribute.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`
- `limit` (integer): The number of Builds resources to return.

  **Maximum**: `200`
- `limit[betaBuildLocalizations]` (integer): The number of included Builds resources to return if the beta build localization relationship is included.

  **Maximum**: `50`
- `limit[icons]` (integer): The number of included Builds resources to return if the icons relationship is included.

  **Maximum**: `50`
- `limit[individualTesters]` (integer): The number of included Builds resources to return if the individual testers relationship is included.

  **Maximum**: `50`
- `sort` ([string]): Attributes by which to sort the returned Builds resources.

  **Allowed Values**: `version`, `-version`, `uploadedDate`, `-uploadedDate`, `preReleaseVersion`, `-preReleaseVersion`
- `filter[buildAudienceType]` ([string]): **Allowed Values**: `INTERNAL_ONLY`, `APP_STORE_ELIGIBLE`
- `limit[buildBundles]` (integer): **Maximum**: `50`
- `fields[buildBundles]` ([string]): **Allowed Values**: `bundleId`, `bundleType`, `sdkBuild`, `platformBuild`, `fileName`, `hasSirikit`, `hasOnDemandResources`, `hasPrerenderedIcon`, `usesLocationServices`, `isIosBuildMacAppStoreCompatible`, `includesSymbols`, `dSYMUrl`, `supportedArchitectures`, `requiredCapabilities`, `deviceProtocols`, `locales`, `entitlements`, `baDownloadAllowance`, `baMaxInstallSize`, `minimumOsVersion`, `appClipDomainCacheStatus`, `appClipDomainDebugStatus`, `betaAppClipInvocations`, `buildBundleFileSizes`
- `fields[betaGroups]` ([string]): **Allowed Values**: `name`, `createdDate`, `isInternalGroup`, `hasAccessToAllBuilds`, `publicLinkEnabled`, `publicLinkId`, `publicLinkLimitEnabled`, `publicLinkLimit`, `publicLink`, `feedbackEnabled`, `iosBuildsAvailableForAppleSiliconMac`, `iosBuildsAvailableForAppleVision`, `app`, `builds`, `betaTesters`, `betaRecruitmentCriteria`, `betaRecruitmentCriterionCompatibleBuildCheck`
- `limit[betaGroups]` (integer): **Maximum**: `50`
- `fields[betaAppReviewSubmissions]` ([string]): **Allowed Values**: `betaReviewState`, `submittedDate`, `build`
- `fields[buildBetaDetails]` ([string]): **Allowed Values**: `autoNotifyEnabled`, `internalBuildState`, `externalBuildState`, `build`
- `fields[preReleaseVersions]` ([string]): **Allowed Values**: `version`, `platform`, `builds`, `app`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[appEncryptionDeclarations]` ([string]): **Allowed Values**: `appDescription`, `createdDate`, `usesEncryption`, `exempt`, `containsProprietaryCryptography`, `containsThirdPartyCryptography`, `availableOnFrenchStore`, `platform`, `uploadedDate`, `documentUrl`, `documentName`, `documentType`, `appEncryptionDeclarationState`, `codeValue`, `app`, `builds`, `appEncryptionDeclarationDocument`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `exists[usesNonExemptEncryption]` (boolean)
- `fields[buildUploads]` ([string]): **Allowed Values**: `cfBundleShortVersionString`, `cfBundleVersion`, `createdDate`, `state`, `platform`, `uploadedDate`, `build`, `assetFile`, `assetDescriptionFile`, `assetSpiFile`, `buildUploadFiles`

## Responses

- `200` OK (`BuildsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Information
- [Read xcode cloud build information](./get-v1-cibuildruns-_id_.md)
  Get information about a specific Xcode Cloud build.
- [List all actions for an xcode cloud build](./get-v1-cibuildruns-_id_-actions.md)
  List all actions Xcode Cloud performed during a specific build.
- [List action IDs for a CI build run](./get-v1-cibuildruns-_id_-relationships-actions.md)
- [List build IDs for a CI build run](./get-v1-cibuildruns-_id_-relationships-builds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildruns-_id_-builds)*