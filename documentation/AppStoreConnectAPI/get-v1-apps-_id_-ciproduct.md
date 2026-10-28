# Read the xcode cloud product for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the Xcode Cloud product information for an app you build with Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Discussion

The example request below retrieves information about a specific Xcode Cloud product. Use the data provided in the response to read additional information; for example, workflow information.

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/6446998023/ciProduct
```

**Response**:

```json
{
    "data": {
        "type": "ciProducts",
        "id": "6446998023",
        "attributes": {
            "name": "Your Next Cortado",
            "createdDate": "2021-08-17T18:02:43.097Z",
            "productType": "APP"
        },
        "relationships": {
            "app": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/app",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/app"
                }
            },
            "workflows": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/workflows",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/workflows"
                }
            },
            "primaryRepositories": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/primaryRepositories",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/primaryRepositories"
                }
            },
            "additionalRepositories": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/additionalRepositories",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/additionalRepositories"
                }
            },
            "buildRuns": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/buildRuns",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/buildRuns"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/ciProduct`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Apps resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[ciProducts]` ([string]): Additional fields to include for each Products resource returned by the response.

  **Allowed Values**: `name`, `createdDate`, `productType`, `app`, `bundleId`, `workflows`, `primaryRepositories`, `additionalRepositories`, `buildRuns`
- `fields[scmRepositories]` ([string]): Additional fields to include for each Products resource returned by the response.

  **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `app`, `bundleId`, `primaryRepositories`
- `limit[primaryRepositories]` (integer): The number of included Products resources to return if the primary repositories relationship is included.

  **Maximum**: `50`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[bundleIds]` ([string]): **Allowed Values**: `name`, `platform`, `identifier`, `seedId`, `profiles`, `bundleIdCapabilities`, `app`

## Responses

- `200` OK (`CiProductResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting an app’s Xcode Cloud products
- [Get the CI product ID for an app](./get-v1-apps-_id_-relationships-ciproduct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-ciproduct)*