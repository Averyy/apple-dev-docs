# List all In-App Purchases for an app v1

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the In-App Purchases that are available for your app.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 2.0

> **Deprecated**: Use [`List all In-App Purchases for an app`](./get-v1-apps-_id_-inapppurchasesv2.md) instead.

## Mentions

- [App Store Connect API 2.0 release notes](./app-store-connect-api-2-0-release-notes.md)
- [App Store Connect API 2.2 release notes](./app-store-connect-api-2-2-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchases
```

**Response**:

```json
{
    "data": [
        {
            "type": "inAppPurchases",
            "id": "ca38ea26-b7d5-4989-9615-c678cb05aabd",
            "attributes": {
                "referenceName": "YNC1",
                "productId": "YNCNC1",
                "inAppPurchaseType": "NON_CONSUMABLE",
                "state": "WAITING_FOR_SCREENSHOT"
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/inAppPurchases/ca38ea26-b7d5-4989-9615-c678cb05aabd"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchases"
    },
    "meta": {
        "paging": {
            "total": 1,
            "limit": 50
        }
    }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/inAppPurchases`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[inAppPurchases]` ([string]): Additional fields to include for each In-App Purchase resource returned by the response.

  **Allowed Values**: `referenceName`, `productId`, `inAppPurchaseType`, `state`, `apps`
- `filter[canBeSubmitted]` ([string]): Filter the returned In-App Purchases by whether they can be submitted.
- `filter[inAppPurchaseType]` ([string]): Filter the returned In-App Purchases by In-App Purchase type.

  **Allowed Values**: `AUTOMATICALLY_RENEWABLE_SUBSCRIPTION`, `NON_CONSUMABLE`, `CONSUMABLE`, `NON_RENEWING_SUBSCRIPTION`, `FREE_SUBSCRIPTION`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `apps`
- `limit` (integer): The maximum number of In-App Purchase resources to return.

  **Maximum**: `200`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `referenceName`, `-referenceName`, `productId`, `-productId`, `inAppPurchaseType`, `-inAppPurchaseType`
- `limit[apps]` (integer): The maximum number of related apps resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`InAppPurchasesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting In-App Purchase information
- [Read In-App Purchase information](./get-v1-inapppurchases-_id_.md)
  Get information about an In-App Purchase.
- [List all promoted purchases for an app](./get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted In-App Purchases, including promoted auto-renewable subscriptions, for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-inapppurchases)*