# Get Review Submissions for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of review submissions associated with a specific app.

**Availability**:
- App Store Connect API 1.7+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/6446998023/reviewSubmissions
```

**Response**:

```json
{
    "data": [
        {
            "type": "reviewSubmissions",
            "id": "fda9bd85-170b-4a1c-8d78-c2b445527542",
            "attributes": {
                "platform": "IOS",
                "submittedDate": null,
                "state": "READY_FOR_REVIEW"
            },
            "relationships": {
                "items": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/reviewSubmissions/fda9bd85-170b-4a1c-8d78-c2b445527542/relationships/items",
                        "related": "https://api.appstoreconnect.apple.com/v1/reviewSubmissions/fda9bd85-170b-4a1c-8d78-c2b445527542/items"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/reviewSubmissions/fda9bd85-170b-4a1c-8d78-c2b445527542"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/reviewSubmissions"
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

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/reviewSubmissions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[reviewSubmissionItems]` ([string]): Additional fields to include for each review submission item resource returned by the response.

  **Allowed Values**: `state`, `appStoreVersion`, `appCustomProductPageVersion`, `appStoreVersionExperiment`, `appStoreVersionExperimentV2`, `appEvent`, `appAssetLibraryImage`, `appAssetLibraryVideo`, `backgroundAssetVersion`, `gameCenterAchievementVersion`, `gameCenterActivityVersion`, `gameCenterChallengeVersion`, `gameCenterLeaderboardSetVersion`, `gameCenterLeaderboardVersion`, `inAppPurchaseVersion`, `subscriptionVersion`, `subscriptionGroupVersion`
- `fields[reviewSubmissions]` ([string]): Additional fields to include for each review submission resource returned by the response.

  **Allowed Values**: `platform`, `submittedDate`, `state`, `app`, `items`, `appStoreVersionForReview`, `submittedByActor`, `lastUpdatedByActor`
- `filter[platform]` ([string]): Filter the returned review submissions by platform.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `filter[state]` ([string]): Filter the returned review submissions by state.

  **Allowed Values**: `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `UNRESOLVED_ISSUES`, `CANCELING`, `COMPLETING`, `COMPLETE`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `app`, `items`, `appStoreVersionForReview`, `submittedByActor`, `lastUpdatedByActor`
- `limit` (integer): The maximum number of review submission resources to return.

  **Maximum**: `200`
- `limit[items]` (integer): The maximum number of related items resources to return.

  **Maximum**: `50`
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.

  **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[actors]` ([string]): Additional fields to include for each actor resource returned by the response.

  **Allowed Values**: `actorType`, `userFirstName`, `userLastName`, `userEmail`, `apiKeyId`

## Responses

- `200` OK (`ReviewSubmissionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting review submissions
- [List review submission IDs](./get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-reviewsubmissions)*