# List users

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of the users on your team.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/users`

## Parameters

### Query Parameters

- `fields[apps]` ([string]): Fields to return for included related types.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[users]` ([string]): Fields to return for included related types.

  **Allowed Values**: `username`, `firstName`, `lastName`, `roles`, `allAppsVisible`, `provisioningAllowed`, `visibleApps`
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `visibleApps`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `username`, `-username`, `lastName`, `-lastName`
- `filter[roles]` ([string]): Attributes, relationships, and IDs by which to filter.

  **Allowed Values**: `ADMIN`, `FINANCE`, `ACCOUNT_HOLDER`, `SALES`, `MARKETING`, `APP_MANAGER`, `DEVELOPER`, `ACCESS_TO_REPORTS`, `CUSTOMER_SUPPORT`, `CREATE_APPS`, `CLOUD_MANAGED_DEVELOPER_ID`, `CLOUD_MANAGED_APP_DISTRIBUTION`, `GENERATE_INDIVIDUAL_KEYS`
- `filter[visibleApps]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[username]` ([string]): Attributes, relationships, and IDs by which to filter.
- `limit[visibleApps]` (integer): Number of included related resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`UsersResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting User Information
- [Read user information](./get-v1-users-_id_.md)
  Get information about a user on your team, such as name, roles, and app visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-users)*