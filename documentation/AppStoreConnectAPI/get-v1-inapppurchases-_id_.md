# Read In-App Purchase information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about an In-App Purchase.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: Use [`Read In-App Purchase information`](./get-v2-inapppurchases-_id_.md) instead.

#### Discussion

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/inAppPurchases/6446998023
```

**Response**:

```json
{
  "data": [
    {
      "type": "inAppPurchases",
      "id": "6447027998",
      "attributes": {
        "name": "YNC1",
        "productId": "YNCNC1",
        "inAppPurchaseType": "NON_CONSUMABLE",
        "state": "MISSING_METADATA",
        "reviewNote": null,
        "familySharable": false,
        "contentHosting": false,
        "availableInAllTerritories": true
      },
      "relationships": {
        "inAppPurchaseLocalizations": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/inAppPurchaseLocalizations",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/inAppPurchaseLocalizations"
          }
        },
        "pricePoints": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/pricePoints",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/pricePoints"
          }
        },
        "content": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/content",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/content"
          }
        },
        "appStoreReviewScreenshot": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/appStoreReviewScreenshot",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/appStoreReviewScreenshot"
          }
        },
        "promotedPurchase": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/promotedPurchase",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/promotedPurchase"
          }
        },
        "iapPriceSchedule": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/relationships/iapPriceSchedule",
            "related": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998/iapPriceSchedule"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v2/inAppPurchases/6447027998"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchasesV2"
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

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchases/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[inAppPurchases]` ([string]): **Allowed Values**: `referenceName`, `productId`, `inAppPurchaseType`, `state`, `apps`
- `include` ([string]): **Allowed Values**: `apps`
- `limit[apps]` (integer): **Maximum**: `50`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`

## Responses

- `200` OK (`InAppPurchaseResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting In-App Purchase information
- [List all promoted purchases for an app](./get-v1-apps-_id_-promotedpurchases.md)
  Get a list of promoted In-App Purchases, including promoted auto-renewable subscriptions, for an app.
- [List all In-App Purchases for an app v1](./get-v1-apps-_id_-inapppurchases.md)
  List the In-App Purchases that are available for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchases-_id_)*