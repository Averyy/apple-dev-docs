# List all background assets for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about the Apple-hosted background assets for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [App Store Connect API 4.4 release notes](./app-store-connect-api-4-4-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/backgroundAssets`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[backgroundAssetVersions]` ([string]): Additional fields to include for each background asset version resource that the response returns.

  **Allowed Values**: `createdDate`, `platforms`, `state`, `stateDetails`, `version`, `locale`, `backgroundAsset`, `internalBetaRelease`, `externalBetaRelease`, `appStoreRelease`, `assetFile`, `manifestFile`, `backgroundAssetUploadFiles`
- `fields[backgroundAssets]` ([string]): Additional fields to include for each background asset resource that the response returns.

  **Allowed Values**: `archived`, `assetPackIdentifier`, `createdDate`, `usedBytes`, `app`, `versions`, `appStoreVersion`, `internalBetaVersion`, `externalBetaVersion`
- `filter[assetPackIdentifier]` ([string]): Filter the returned background assets by asset pack identifier.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `app`, `appStoreVersion`, `internalBetaVersion`, `externalBetaVersion`
- `limit` (integer): The maximum number of background asset resources to return.

  **Maximum**: `200`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `filter[archived]` ([string])
- `filter[versions.locale]` ([string])
- `filter[versions.platforms]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `sort` ([string]): **Allowed Values**: `assetPackIdentifier`, `-assetPackIdentifier`, `createdDate`, `-createdDate`

## Responses

- `200` OK (`BackgroundAssetsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting background asset information
- [List the assets packs ids for an app](./get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Modify a Background Asset](./patch-v1-backgroundassets-_id_.md)
  Update a specific background asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-backgroundassets)*