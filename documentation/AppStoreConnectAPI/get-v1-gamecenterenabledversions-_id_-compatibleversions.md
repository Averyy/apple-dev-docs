# List all compatible versions for a game center enabled version

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: This endpoint is deprecated. Use [`Read compatibility version information`](./get-v1-gamecenterappversions-_id_-compatibilityversions.md) instead.

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterEnabledVersions/{id}/compatibleVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterEnabledVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `iconAsset`, `compatibleVersions`, `app`
- `filter[app]` ([string])
- `filter[id]` ([string])
- `filter[platform]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[versionString]` ([string])
- `include` ([string]): **Allowed Values**: `compatibleVersions`, `app`
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `versionString`, `-versionString`
- `limit[compatibleVersions]` (integer) *(deprecated)*: **Maximum**: `50`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`

## Responses

- `200` OK (`GameCenterEnabledVersionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing Versions
- [List all game center enabled versions for an app](./get-v1-apps-_id_-gamecenterenabledversions.md)
  Get a list of Game Center enabled versions for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterenabledversions-_id_-compatibleversions)*