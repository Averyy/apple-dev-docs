# List prerelease versions

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of prerelease versions for all apps.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [App Store Connect API 4.1 release notes](./app-store-connect-api-4-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/preReleaseVersions`

## Parameters

### Query Parameters

- `fields[apps]` ([string]): Fields to return for included related types.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[builds]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `fields[preReleaseVersions]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `platform`, `builds`, `app`
- `filter[app]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[builds.expired]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[builds.processingState]` ([string]): Attributes, relationships, and IDs by which to filter.

  **Allowed Values**: `PROCESSING`, `FAILED`, `INVALID`, `VALID`
- `filter[builds]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[platform]` ([string]): Attributes, relationships, and IDs by which to filter.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[version]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `builds`, `app`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`
- `limit[builds]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `version`, `-version`
- `filter[builds.version]` ([string])
- `filter[builds.buildAudienceType]` ([string]): **Allowed Values**: `INTERNAL_ONLY`, `APP_STORE_ELIGIBLE`

## Responses

- `200` OK (`PreReleaseVersionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Prerelease Version Information
- [Read prerelease version information](./get-v1-prereleaseversions-_id_.md)
  Get information about a specific prerelease version.
- [Read the app information of a prerelease version](./get-v1-prereleaseversions-_id_-app.md)
  Get the app information for a specific prerelease version.
- [Get the app ID for a prerelease version](./get-v1-prereleaseversions-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-prereleaseversions)*