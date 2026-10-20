# List all game center enabled versions for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of Game Center enabled versions for a specific app.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: Use [`Read compatibility version information`](./get-v1-gamecenterappversions-_id_-compatibilityversions.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/gameCenterEnabledVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[gameCenterEnabledVersions]` ([string]): Additional fields to include for each Game Center enabled version resource returned by the response.

  **Allowed Values**: `platform`, `versionString`, `iconAsset`, `compatibleVersions`, `app`
- `filter[id]` ([string]): Filter the returned Game Center enabled versions by ID.
- `filter[platform]` ([string]): Filter the returned Game Center enabled versions by platform.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[versionString]` ([string]): Filter the returned Game Center enabled versions by version string.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `compatibleVersions`, `app`
- `limit` (integer): The maximum number of Game Center enabled version resources to return.

  **Maximum**: `200`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `versionString`, `-versionString`
- `limit[compatibleVersions]` (integer) *(deprecated)*: The maximum number of related compatible versions resources to return.

  **Maximum**: `50`
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`

## Responses

- `200` OK (`GameCenterEnabledVersionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing Versions
- [List all compatible versions for a game center enabled version](./get-v1-gamecenterenabledversions-_id_-compatibleversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-gamecenterenabledversions)*