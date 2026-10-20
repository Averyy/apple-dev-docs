# List bundle ids

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list bundle IDs that are registered to your team.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/bundleIds`

## Parameters

### Query Parameters

- `fields[bundleIds]` ([string]): **Allowed Values**: `name`, `platform`, `identifier`, `seedId`, `profiles`, `bundleIdCapabilities`, `app`
- `fields[profiles]` ([string]): **Allowed Values**: `name`, `platform`, `profileType`, `profileState`, `profileContent`, `uuid`, `createdDate`, `expirationDate`, `bundleId`, `devices`, `certificates`
- `filter[id]` ([string])
- `filter[identifier]` ([string])
- `filter[name]` ([string])
- `filter[platform]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`, `UNIVERSAL`
- `filter[seedId]` ([string])
- `include` ([string]): **Allowed Values**: `profiles`, `bundleIdCapabilities`, `app`
- `limit` (integer): **Maximum**: `200`
- `limit[profiles]` (integer): **Maximum**: `50`
- `sort` ([string]): **Allowed Values**: `name`, `-name`, `platform`, `-platform`, `identifier`, `-identifier`, `seedId`, `-seedId`, `id`, `-id`
- `fields[bundleIdCapabilities]` ([string]): **Allowed Values**: `capabilityType`, `settings`
- `limit[bundleIdCapabilities]` (integer): **Maximum**: `50`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`

## Responses

- `200` OK (`BundleIdsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Bundle ID Information
- [Read bundle id information](./get-v1-bundleids-_id_.md)
  Get information about a specific bundle ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-bundleids)*