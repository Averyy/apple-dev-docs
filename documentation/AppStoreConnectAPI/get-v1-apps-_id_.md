# Read app information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific app.

**Availability**:
- App Store Connect API 1.0+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/6446998023
```

**Response**:

```json
{
  "data": {
    "type": "apps",
    "id": "6446998023",
    "attributes": {
      "name": "Your Next Cortado",
      "bundleId": "com.bdt.ync",
      "sku": "YNC",
      "primaryLocale": "en-US",
      "isOrEverWasMadeForKids": false,
      "subscriptionStatusUrl": null,
      "subscriptionStatusUrlVersion": null,
      "subscriptionStatusUrlForSandbox": null,
      "subscriptionStatusUrlVersionForSandbox": null,
      "availableInNewTerritories": true,
      "contentRightsDeclaration": "DOES_NOT_USE_THIRD_PARTY_CONTENT"
    },
    "relationships": {
      "ciProduct": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/ciProduct",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/ciProduct"
        }
      },
      "betaTesters": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaTesters"
        }
      },
      "betaGroups": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaGroups",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaGroups"
        }
      },
      "appStoreVersions": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appStoreVersions",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appStoreVersions"
        }
      },
      "preReleaseVersions": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/preReleaseVersions",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/preReleaseVersions"
        }
      },
      "betaAppLocalizations": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaAppLocalizations",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppLocalizations"
        }
      },
      "builds": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/builds",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/builds"
        }
      },
      "betaLicenseAgreement": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaLicenseAgreement",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaLicenseAgreement"
        }
      },
      "betaAppReviewDetail": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/betaAppReviewDetail",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/betaAppReviewDetail"
        }
      },
      "appInfos": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appInfos",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appInfos"
        }
      },
      "appClips": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appClips",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appClips"
        }
      },
      "appPricePoints": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appPricePoints",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appPricePoints"
        }
      },
      "pricePoints": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/pricePoints",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/pricePoints"
        }
      },
      "endUserLicenseAgreement": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/endUserLicenseAgreement",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/endUserLicenseAgreement"
        }
      },
      "preOrder": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/preOrder",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/preOrder"
        }
      },
      "prices": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/prices",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/prices"
        }
      },
      "appPriceSchedule": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appPriceSchedule",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appPriceSchedule"
        }
      },
      "availableTerritories": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/availableTerritories",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/availableTerritories"
        }
      },
      "appAvailability": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appAvailability",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appAvailability"
        }
      },
      "inAppPurchases": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/inAppPurchases",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchases"
        }
      },
      "subscriptionGroups": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/subscriptionGroups",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/subscriptionGroups"
        }
      },
      "gameCenterEnabledVersions": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/gameCenterEnabledVersions",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/gameCenterEnabledVersions"
        }
      },
      "perfPowerMetrics": {
        "links": {
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/perfPowerMetrics"
        }
      },
      "appCustomProductPages": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appCustomProductPages",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appCustomProductPages"
        }
      },
      "inAppPurchasesV2": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/inAppPurchasesV2",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/inAppPurchasesV2"
        }
      },
      "promotedPurchases": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/promotedPurchases",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/promotedPurchases"
        }
      },
      "appEvents": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/appEvents",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appEvents"
        }
      },
      "reviewSubmissions": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/reviewSubmissions",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/reviewSubmissions"
        }
      },
      "subscriptionGracePeriod": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/subscriptionGracePeriod",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/subscriptionGracePeriod"
        }
      },
      "customerReviews": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/relationships/customerReviews",
          "related": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/customerReviews"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023"
  }
}


```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[apps]` ([string]): Fields to return for included related types.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[betaLicenseAgreements]` ([string]): Fields to return for included related types.

  **Allowed Values**: `agreementText`, `app`
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaGroups`, `appStoreVersions`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `endUserLicenseAgreement`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `androidToIosAppMappingDetails`
- `fields[preReleaseVersions]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `platform`, `builds`, `app`
- `fields[betaAppReviewDetails]` ([string]): Fields to return for included related types.

  **Allowed Values**: `contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountName`, `demoAccountPassword`, `demoAccountRequired`, `notes`, `app`
- `fields[betaAppLocalizations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `feedbackEmail`, `marketingUrl`, `privacyPolicyUrl`, `tvOsPrivacyPolicy`, `description`, `locale`, `app`
- `fields[builds]` ([string]): Fields to return for included related types.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `fields[betaGroups]` ([string]): Fields to return for included related types.

  **Allowed Values**: `name`, `createdDate`, `isInternalGroup`, `hasAccessToAllBuilds`, `publicLinkEnabled`, `publicLinkId`, `publicLinkLimitEnabled`, `publicLinkLimit`, `publicLink`, `feedbackEnabled`, `iosBuildsAvailableForAppleSiliconMac`, `iosBuildsAvailableForAppleVision`, `app`, `builds`, `betaTesters`, `betaRecruitmentCriteria`, `betaRecruitmentCriterionCompatibleBuildCheck`
- `limit[preReleaseVersions]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `limit[builds]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `limit[betaGroups]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `limit[betaAppLocalizations]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `limit[appStoreVersions]` (integer): Number of resources to return.

  **Maximum**: `50`
- `limit[appInfos]` (integer): Number of resources to return.

  **Maximum**: `50`
- `fields[endUserLicenseAgreements]` ([string]): **Allowed Values**: `agreementText`, `app`, `territories`
- `fields[appStoreVersions]` ([string]): **Allowed Values**: `platform`, `versionString`, `appStoreState`, `appVersionState`, `copyright`, `reviewType`, `releaseType`, `earliestReleaseDate`, `usesIdfa`, `downloadable`, `createdDate`, `app`, `appStoreVersionLocalizations`, `build`, `appStoreVersionPhasedRelease`, `gameCenterAppVersion`, `routingAppCoverage`, `appStoreReviewDetail`, `appStoreVersionSubmission`, `appClipDefaultExperience`, `appStoreVersionExperiments`, `appStoreVersionExperimentsV2`, `customerReviews`, `alternativeDistributionPackage`
- `fields[appInfos]` ([string]): **Allowed Values**: `appStoreState`, `state`, `appStoreAgeRating`, `australiaAgeRating`, `brazilAgeRating`, `brazilAgeRatingV2`, `franceAgeRating`, `koreaAgeRating`, `app`, `ageRatingDeclaration`, `appInfoLocalizations`, `primaryCategory`, `primarySubcategoryOne`, `primarySubcategoryTwo`, `secondaryCategory`, `secondarySubcategoryOne`, `secondarySubcategoryTwo`, `territoryAgeRatings`
- `limit[gameCenterEnabledVersions]` (integer) *(deprecated)*: Number of resources to return.

  **Maximum**: `50`
- `fields[gameCenterEnabledVersions]` ([string]) *(deprecated)*: **Allowed Values**: `platform`, `versionString`, `iconAsset`, `compatibleVersions`, `app`
- `limit[inAppPurchases]` (integer) *(deprecated)*: Number of resources to return.

  **Maximum**: `50`
- `fields[inAppPurchases]` ([string]): **Allowed Values**: `referenceName`, `productId`, `inAppPurchaseType`, `state`, `apps`, `name`, `reviewNote`, `familySharable`, `contentHosting`, `inAppPurchaseLocalizations`, `pricePoints`, `content`, `appStoreReviewScreenshot`, `promotedPurchase`, `iapPriceSchedule`, `inAppPurchaseAvailability`, `images`, `offerCodes`, `versions`
- `fields[ciProducts]` ([string]): **Allowed Values**: `name`, `createdDate`, `productType`, `app`, `bundleId`, `workflows`, `primaryRepositories`, `additionalRepositories`, `buildRuns`
- `limit[appClips]` (integer): Number of resources to return.

  **Maximum**: `50`
- `fields[appClips]` ([string]): **Allowed Values**: `bundleId`, `app`, `appClipDefaultExperiences`, `appClipAdvancedExperiences`
- `fields[reviewSubmissions]` ([string]): **Allowed Values**: `platform`, `submittedDate`, `state`, `app`, `items`, `appStoreVersionForReview`, `submittedByActor`, `lastUpdatedByActor`
- `fields[appCustomProductPages]` ([string]): **Allowed Values**: `name`, `url`, `visible`, `app`, `appCustomProductPageVersions`
- `fields[appEvents]` ([string]): **Allowed Values**: `referenceName`, `badge`, `eventState`, `deepLink`, `purchaseRequirement`, `primaryLocale`, `priority`, `purpose`, `territorySchedules`, `archivedTerritorySchedules`, `localizations`
- `limit[appCustomProductPages]` (integer): Number of resources to return.

  **Maximum**: `50`
- `limit[appEvents]` (integer): Number of resources to return.

  **Maximum**: `50`
- `limit[reviewSubmissions]` (integer): Number of resources to return.

  **Maximum**: `50`
- `fields[subscriptionGracePeriods]` ([string]): **Allowed Values**: `optIn`, `sandboxOptIn`, `duration`, `renewalType`
- `fields[promotedPurchases]` ([string]): **Allowed Values**: `visibleForAllUsers`, `enabled`, `state`, `inAppPurchaseV2`, `subscription`
- `fields[subscriptionGroups]` ([string]): **Allowed Values**: `referenceName`, `subscriptions`, `subscriptionGroupLocalizations`, `versions`
- `limit[inAppPurchasesV2]` (integer): Number of resources to return.

  **Maximum**: `50`
- `limit[promotedPurchases]` (integer): Number of resources to return.

  **Maximum**: `50`
- `limit[subscriptionGroups]` (integer): Number of resources to return.

  **Maximum**: `50`
- `fields[appStoreVersionExperiments]` ([string]): **Allowed Values**: `name`, `platform`, `trafficProportion`, `state`, `reviewRequired`, `startDate`, `endDate`, `app`, `latestControlVersion`, `controlVersions`, `appStoreVersionExperimentTreatments`
- `limit[appStoreVersionExperimentsV2]` (integer): **Maximum**: `50`
- `fields[appEncryptionDeclarations]` ([string]): **Allowed Values**: `appDescription`, `createdDate`, `usesEncryption`, `exempt`, `containsProprietaryCryptography`, `containsThirdPartyCryptography`, `availableOnFrenchStore`, `platform`, `uploadedDate`, `documentUrl`, `documentName`, `documentType`, `appEncryptionDeclarationState`, `codeValue`, `app`, `builds`, `appEncryptionDeclarationDocument`
- `limit[appEncryptionDeclarations]` (integer): **Maximum**: `50`
- `fields[gameCenterDetails]` ([string]): **Allowed Values**: `arcadeEnabled`, `challengeEnabled`, `app`, `gameCenterAppVersions`, `gameCenterGroup`, `gameCenterLeaderboards`, `gameCenterLeaderboardsV2`, `gameCenterLeaderboardSets`, `gameCenterLeaderboardSetsV2`, `gameCenterAchievements`, `gameCenterAchievementsV2`, `gameCenterActivities`, `gameCenterChallenges`, `defaultLeaderboard`, `defaultLeaderboardV2`, `defaultGroupLeaderboard`, `defaultGroupLeaderboardV2`, `achievementReleases`, `activityReleases`, `challengeReleases`, `leaderboardReleases`, `leaderboardSetReleases`, `blockedPlayers`, `challengesMinimumPlatformVersions`
- `fields[androidToIosAppMappingDetails]` ([string]): **Allowed Values**: `packageName`, `appSigningKeyPublicCertificateSha256Fingerprints`
- `limit[androidToIosAppMappingDetails]` (integer): **Maximum**: `50`
- `fields[buildIcons]` ([string]): **Allowed Values**: `iconAsset`, `iconType`, `masked`, `name`

## Responses

- `200` OK (`AppResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting and modifying app information
- [List apps](./get-v1-apps.md)
  Find and list apps in App Store Connect.
- [Modify an app](./patch-v1-apps-_id_.md)
  Update app information, including bundle ID, primary locale, price schedule, and global availability.
- [Read an app’s encryption declarations](./get-v1-apps-_id_-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read an app’s encryption declaration ids](./get-v1-apps-_id_-relationships-appencryptiondeclarations.md)
  Find and list all available app encryption declaration IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_)*