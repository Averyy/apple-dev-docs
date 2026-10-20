# Read Details for a Nomination

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information for a specific featuring nomination.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/nominations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the nomination resource ID from the [`List Nominations`](./get-v1-nominations.md) response.

### Query Parameters

- `fields[nominations]` ([string]): **Allowed Values**: `name`, `type`, `description`, `createdDate`, `lastModifiedDate`, `submittedDate`, `state`, `publishStartDate`, `publishEndDate`, `deviceFamilies`, `locales`, `supplementalMaterialsUris`, `hasInAppEvents`, `launchInSelectMarketsFirst`, `notes`, `preOrderEnabled`, `relatedApps`, `createdByActor`, `lastModifiedByActor`, `submittedByActor`, `inAppEvents`, `supportedTerritories`
- `include` ([string]): **Allowed Values**: `relatedApps`, `createdByActor`, `lastModifiedByActor`, `submittedByActor`, `inAppEvents`, `supportedTerritories`
- `limit[inAppEvents]` (integer): **Maximum**: `50`
- `limit[relatedApps]` (integer): **Maximum**: `50`
- `limit[supportedTerritories]` (integer): **Maximum**: `200`
- `fields[actors]` ([string]): **Allowed Values**: `actorType`, `userFirstName`, `userLastName`, `userEmail`, `apiKeyId`
- `fields[appEvents]` ([string]): **Allowed Values**: `referenceName`, `badge`, `eventState`, `deepLink`, `purchaseRequirement`, `primaryLocale`, `priority`, `purpose`, `territorySchedules`, `archivedTerritorySchedules`, `localizations`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[territories]` ([string]): **Allowed Values**: `currency`

## Responses

- `200` OK (`NominationResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing nominations
- [Create a Featuring Nomination](./post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [List Nominations](./get-v1-nominations.md)
  Get all featuring nominations.
- [Modify a Nomination](./patch-v1-nominations-_id_.md)
  Update a specific featuring nomination.
- [Delete a Featuring Nomination](./delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-nominations-_id_)*