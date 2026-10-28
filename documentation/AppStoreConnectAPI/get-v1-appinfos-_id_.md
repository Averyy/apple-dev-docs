# Read app info information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Read App Store information including your App Store state, age ratings, Brazil age rating, and kids’ age band.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.6 release notes](./app-store-connect-api-3-6-release-notes.md)
- [App Store Connect API 3.7 release notes](./app-store-connect-api-3-7-release-notes.md)

## Discussion

For request and response examples for reading an age rating declaration, see [`Read the age-rating declaration`](./get-v1-appinfos-_id_-ageratingdeclaration.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `appInfo` resource ID from the [`List all app infos for an app`](./get-v1-apps-_id_-appinfos.md) response.

### Query Parameters

- `fields[appCategories]` ([string]): Fields to return for included related types.

  **Allowed Values**: `platforms`, `subcategories`, `parent`
- `fields[appInfoLocalizations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `locale`, `name`, `subtitle`, `privacyPolicyUrl`, `privacyChoicesUrl`, `privacyPolicyText`, `appInfo`
- `fields[appInfos]` ([string]): Fields to return for included related types.

  **Allowed Values**: `appStoreState`, `state`, `appStoreAgeRating`, `australiaAgeRating`, `brazilAgeRating`, `brazilAgeRatingV2`, `franceAgeRating`, `koreaAgeRating`, `app`, `ageRatingDeclaration`, `appInfoLocalizations`, `primaryCategory`, `primarySubcategoryOne`, `primarySubcategoryTwo`, `secondaryCategory`, `secondarySubcategoryOne`, `secondarySubcategoryTwo`, `territoryAgeRatings`
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `app`, `ageRatingDeclaration`, `appInfoLocalizations`, `primaryCategory`, `primarySubcategoryOne`, `primarySubcategoryTwo`, `secondaryCategory`, `secondarySubcategoryOne`, `secondarySubcategoryTwo`
- `limit[appInfoLocalizations]` (integer): Number of included related resources to return.

  **Maximum**: `50`
- `fields[ageRatingDeclarations]` ([string]): Fields to return for included related types.

  **Allowed Values**: `advertising`, `alcoholTobaccoOrDrugUseOrReferences`, `contests`, `gambling`, `gamblingSimulated`, `gunsOrOtherWeapons`, `healthOrWellnessTopics`, `kidsAgeBand`, `lootBox`, `medicalOrTreatmentInformation`, `messagingAndChat`, `parentalControls`, `profanityOrCrudeHumor`, `ageAssurance`, `sexualContentGraphicAndNudity`, `sexualContentOrNudity`, `socialMedia`, `socialMediaAgeRestricted`, `horrorOrFearThemes`, `matureOrSuggestiveThemes`, `unrestrictedWebAccess`, `userGeneratedContent`, `violenceCartoonOrFantasy`, `violenceRealisticProlongedGraphicOrSadistic`, `violenceRealistic`, `ageRatingOverride`, `ageRatingOverrideV2`, `koreaAgeRatingOverride`, `gracRatingClassificationNumber`, `developerAgeRatingInfoUrl`
- `fields[apps]` ([string]): **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`

## Responses

- `200` OK (`AppInfoResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading App Information
- [List all app infos for an app](./get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List all app info localizations for an app info](./get-v1-appinfos-_id_-appinfolocalizations.md)
  Get a list of localized, app-level information for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_)*