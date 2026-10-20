# List all app store versions for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all App Store versions of an app across all platforms.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [Creating alternative distribution packages](./creating-alternative-distribution-packages.md)
- [App Store Connect API 1.3 release notes](./app-store-connect-api-1-3-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/6446998023/appStoreVersions
```

**Response**:

```json
{
  "data": [
    {
      "type": "appStoreVersions",
      "id": "2395b439-fccd-4645-95bc-97afbe9e379e",
      "attributes": {
        "platform": "IOS",
        "versionString": "1.0",
        "appStoreState": "PREPARE_FOR_SUBMISSION",
        "copyright": "2022 YNC",
        "releaseType": "MANUAL",
        "earliestReleaseDate": null,
        "usesIdfa": null,
        "downloadable": true,
        "createdDate": "2022-08-31T09:28:28-07:00"
      },
      "relationships": {
        "appStoreVersionLocalizations": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionLocalizations",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionLocalizations"
          }
        },
        "build": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/build",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/build"
          }
        },
        "appStoreVersionPhasedRelease": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionPhasedRelease",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionPhasedRelease"
          }
        },
        "routingAppCoverage": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/routingAppCoverage",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/routingAppCoverage"
          }
        },
        "appStoreReviewDetail": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreReviewDetail",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreReviewDetail"
          }
        },
        "appStoreVersionSubmission": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionSubmission",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionSubmission"
          }
        },
        "idfaDeclaration": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/idfaDeclaration",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/idfaDeclaration"
          }
        },
        "appClipDefaultExperience": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appClipDefaultExperience",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appClipDefaultExperience"
          }
        },
        "appStoreVersionExperiments": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionExperiments",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionExperiments"
          }
        },
        "customerReviews": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/customerReviews",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/customerReviews"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appStoreVersions"
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

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appStoreVersions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the apps resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `limit` (integer): Number of resources to return.

  **Maximum**: `200`
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `alternativeDistributionPackage`
- `fields[apps]` ([string]): Fields to return for included related types.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[appStoreVersionSubmissions]` ([string]): Fields to return for included related types.

  **Allowed Values**: `appStoreVersion`
- `fields[builds]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `fields[appStoreVersions]` ([string]): Fields to return for included related types.

  **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[appStoreReviewDetails]` ([string]): Fields to return for included related types.

  **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `appStoreVersion`, `appStoreReviewAttachments`
- `fields[appStoreVersionPhasedReleases]` ([string]): Fields to return for included related types.

  **Allowed Values**: `phasedReleaseState`, `startDate`, `totalPauseDuration`, `currentDayNumber`
- `fields[routingAppCoverages]` ([string]): Fields to return for included related types.

  **Allowed Values**: `fileSize`, `fileName`, `sourceFileChecksum`, `uploadOperations`, `assetDeliveryState`, `appStoreVersion`
- `fields[appStoreVersionLocalizations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `description`, `locale`, `keywords`, `marketingUrl`, `promotionalText`, `supportUrl`, `whatsNew`, `appStoreVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `filter[id]` ([string]): Fields to return for included related types.
- `filter[versionString]` ([string]): Fields to return for included related types.
- `filter[platform]` ([string]): Fields to return for included related types.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[appStoreState]` ([string]) *(deprecated)*: Fields to return for included related types.

  **Allowed Values**: `ACCEPTED`, `DEVELOPER_REMOVED_FROM_SALE`, `DEVELOPER_REJECTED`, `IN_REVIEW`, `INVALID_BINARY`, `METADATA_REJECTED`, `PENDING_APPLE_RELEASE`, `PENDING_CONTRACT`, `PENDING_DEVELOPER_RELEASE`, `PREPARE_FOR_SUBMISSION`, `PREORDER_READY_FOR_SALE`, `PROCESSING_FOR_APP_STORE`, `READY_FOR_REVIEW`, `READY_FOR_SALE`, `REJECTED`, `REMOVED_FROM_SALE`, `WAITING_FOR_EXPORT_COMPLIANCE`, `WAITING_FOR_REVIEW`, `REPLACED_WITH_NEW_VERSION`, `NOT_APPLICABLE`
- `limit[appStoreVersionLocalizations]` (integer): **Maximum**: `50`
- `fields[appStoreVersionExperiments]` ([string]): **Allowed Values**: `name`, `trafficProportion`, `state`, `reviewRequired`, `startDate`, `endDate`, `appStoreVersion`, `appStoreVersionExperimentTreatments`, `platform`, `app`, `latestControlVersion`, `controlVersions`
- `limit[appStoreVersionExperiments]` (integer) *(deprecated)*: **Maximum**: `50`
- `fields[appClipDefaultExperiences]` ([string]): **Allowed Values**: `action`, `appClip`, `releaseWithAppStoreVersion`, `appClipDefaultExperienceLocalizations`, `appClipAppStoreReviewDetail`
- `limit[appStoreVersionExperimentsV2]` (integer): **Maximum**: `50`
- `filter[appVersionState]` ([string]): **Allowed Values**: `ACCEPTED`, `DEVELOPER_REJECTED`, `IN_REVIEW`, `INVALID_BINARY`, `METADATA_REJECTED`, `PENDING_APPLE_RELEASE`, `PENDING_DEVELOPER_RELEASE`, `PREPARE_FOR_SUBMISSION`, `PROCESSING_FOR_DISTRIBUTION`, `READY_FOR_DISTRIBUTION`, `READY_FOR_REVIEW`, `REJECTED`, `REPLACED_WITH_NEW_VERSION`, `WAITING_FOR_EXPORT_COMPLIANCE`, `WAITING_FOR_REVIEW`
- `fields[alternativeDistributionPackages]` ([string]): **Allowed Values**: `sourceFileChecksum`, `versions`
- `fields[gameCenterAppVersions]` ([string]): **Allowed Values**: `enabled`, `compatibilityVersions`, `appStoreVersion`

## Responses

- `200` OK (`AppStoreVersionsResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting App Store details for your app
- [List all app infos for an app](./get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List app info IDs for an app](./get-v1-apps-_id_-relationships-appinfos.md)
- [List App Store version IDs for an app](./get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the end user license agreement information of an app](./get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [Get the end user license agreement ID for an app](./get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List All Custom Product Pages for an App](./get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource ids for an app](./get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [List all app store experiments for an app](./get-v1-apps-_id_-appstoreversionexperimentsv2.md)
  Get a list of all App Store version experiments for a specific app.
- [List App Store version experiment IDs for an app](./get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appstoreversions)*