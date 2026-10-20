# List Nominations

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get all featuring nominations.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/nominations`

## Parameters

### Query Parameters

- `fields[actors]` ([string]): **Allowed Values**: `actorType`, `userFirstName`, `userLastName`, `userEmail`, `apiKeyId`
- `fields[appEvents]` ([string]): **Allowed Values**: `referenceName`, `badge`, `eventState`, `deepLink`, `purchaseRequirement`, `primaryLocale`, `priority`, `purpose`, `territorySchedules`, `archivedTerritorySchedules`, `localizations`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[nominations]` ([string]): **Allowed Values**: `name`, `type`, `description`, `createdDate`, `lastModifiedDate`, `submittedDate`, `state`, `publishStartDate`, `publishEndDate`, `deviceFamilies`, `locales`, `supplementalMaterialsUris`, `hasInAppEvents`, `launchInSelectMarketsFirst`, `notes`, `preOrderEnabled`, `relatedApps`, `createdByActor`, `lastModifiedByActor`, `submittedByActor`, `inAppEvents`, `supportedTerritories`
- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `filter[hasInAppEvents]` ([string])
- `filter[relatedApps]` ([string])
- `filter[state]` ([string]) *(required)*: **Allowed Values**: `DRAFT`, `SUBMITTED`, `ARCHIVED`
- `filter[type]` ([string]): **Allowed Values**: `APP_LAUNCH`, `APP_ENHANCEMENTS`, `NEW_CONTENT`
- `include` ([string]): **Allowed Values**: `relatedApps`, `createdByActor`, `lastModifiedByActor`, `submittedByActor`, `inAppEvents`, `supportedTerritories`
- `limit` (integer): **Maximum**: `200`
- `limit[inAppEvents]` (integer): **Maximum**: `50`
- `limit[relatedApps]` (integer): **Maximum**: `50`
- `limit[supportedTerritories]` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `lastModifiedDate`, `-lastModifiedDate`, `publishStartDate`, `-publishStartDate`, `publishEndDate`, `-publishEndDate`, `name`, `-name`, `type`, `-type`

## Responses

- `200` OK (`csv`, `text/csv`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing nominations
- [Create a Featuring Nomination](./post-v1-nominations.md)
  Tell Apple about your upcoming app or feature.
- [Read Details for a Nomination](./get-v1-nominations-_id_.md)
  Get information for a specific featuring nomination.
- [Modify a Nomination](./patch-v1-nominations-_id_.md)
  Update a specific featuring nomination.
- [Delete a Featuring Nomination](./delete-v1-nominations-_id_.md)
  Remove a specific featuring nomination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-nominations)*