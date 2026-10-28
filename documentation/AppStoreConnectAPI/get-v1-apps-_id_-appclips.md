# List all app clips for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List your app’s associated App Clips.

**Availability**:
- App Store Connect API 1.6+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.comv1/apps/{id}/appClips
```

**Response**:

```json
{
  "data": [
    {
      "type": "appClips",
      "id": "37453eec-75b3-4578-aba4-ah345936650",
      "attributes": {
        "bundleId": "com.domain.app.AppClip"
      },
      "relationships": {
        "appClipDefaultExperiences": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/relationships/appClipDefaultExperiences",
            "related": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/appClipDefaultExperiences"
          }
        },
        "appClipAdvancedExperiences": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/relationships/appClipAdvancedExperiences",
            "related": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/appClipAdvancedExperiences"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/1000001234/appClips"
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

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appClips`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Apps resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each App Clips resource returned by the response.

  **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `fields[appClips]` ([string]): Additional fields to include for each App Clips resource returned by the response.

  **Allowed Values**: `bundleId`, `app`, `appClipDefaultExperiences`, `appClipAdvancedExperiences`
- `filter[bundleId]` ([string]): Filter the returned App Clips using the bundle ID of the App Clip.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `app`, `appClipDefaultExperiences`
- `limit` (integer): The number of App Clips resources to return.

  **Maximum**: `200`
- `limit[appClipDefaultExperiences]` (integer): The number of included App Clips resources to return if the default App Clip experience localizations relationship is included.

  **Maximum**: `50`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`

## Responses

- `200` OK (`AppClipsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting App Clip information
- [List App Clip IDs for an app](./get-v1-apps-_id_-relationships-appclips.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appclips)*