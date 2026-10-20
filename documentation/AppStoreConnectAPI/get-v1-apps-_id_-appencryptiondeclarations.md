# Read an app’s encryption declarations

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list all available app encryption declarations.

**Availability**:
- App Store Connect API 3.0+

## Mentions

- [App Store Connect API 3.0 release notes](./app-store-connect-api-3-0-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appEncryptionDeclarations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[appEncryptionDeclarationDocuments]` ([string]): Additional fields to include for each app encryption declaration document resource returned by the response.

  **Allowed Values**: `fileSize`, `fileName`, `assetToken`, `downloadUrl`, `sourceFileChecksum`, `uploadOperations`, `assetDeliveryState`
- `fields[appEncryptionDeclarations]` ([string]): Additional fields to include for each app encryption declaration resource returned by the response.

  **Allowed Values**: `appDescription`, `createdDate`, `usesEncryption`, `exempt`, `containsProprietaryCryptography`, `containsThirdPartyCryptography`, `availableOnFrenchStore`, `platform`, `uploadedDate`, `documentUrl`, `documentName`, `documentType`, `appEncryptionDeclarationState`, `codeValue`, `app`, `builds`, `appEncryptionDeclarationDocument`
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

  **Allowed Values**: `accessibilityUrl`, `name`, `bundleId`, `sku`, `primaryLocale`, `isOrEverWasMadeForKids`, `subscriptionStatusUrl`, `subscriptionStatusUrlVersion`, `subscriptionStatusUrlForSandbox`, `subscriptionStatusUrlVersionForSandbox`, `contentRightsDeclaration`, `streamlinedPurchasingEnabled`, `accessibilityDeclarations`, `appEncryptionDeclarations`, `appStoreIcon`, `ciProduct`, `betaTesters`, `betaGroups`, `appStoreVersions`, `appTags`, `preReleaseVersions`, `betaAppLocalizations`, `builds`, `betaLicenseAgreement`, `betaAppReviewDetail`, `appInfos`, `appClips`, `appPricePoints`, `endUserLicenseAgreement`, `appPriceSchedule`, `appAvailabilityV2`, `inAppPurchases`, `subscriptionGroups`, `gameCenterEnabledVersions`, `performanceOverviews`, `perfPowerMetrics`, `appCustomProductPages`, `inAppPurchasesV2`, `promotedPurchases`, `appEvents`, `reviewSubmissions`, `subscriptionGracePeriod`, `customerReviews`, `customerReviewSummarizations`, `gameCenterDetail`, `appStoreVersionExperimentsV2`, `alternativeDistributionKey`, `analyticsReportRequests`, `marketplaceSearchDetail`, `buildUploads`, `backgroundAssets`, `assetLibrary`, `betaFeedbackScreenshotSubmissions`, `betaFeedbackCrashSubmissions`, `searchKeywords`, `webhooks`, `androidToIosAppMappingDetails`
- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `filter[builds]` ([string]): Filter the returned app encryption declarations by builds.
- `filter[platform]` ([string]) *(deprecated)*: Filter the returned app encryption declarations by platform.

  **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `app`, `builds`, `appEncryptionDeclarationDocument`
- `limit` (integer): The maximum number of app encryption declaration resources to return.

  **Maximum**: `200`
- `limit[builds]` (integer): The maximum number of related builds resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`AppEncryptionDeclarationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting App Encryption Declarations
- [List app encryption declarations](./get-v1-appencryptiondeclarations.md)
  Find and list all available app encryption declarations.
- [Read app encryption declaration information](./get-v1-appencryptiondeclarations-_id_.md)
  Get information about a specific app encryption declaration.
- [Read an app’s encryption declaration ids](./get-v1-apps-_id_-relationships-appencryptiondeclarations.md)
  Find and list all available app encryption declaration IDs for a specific app.
- [Read the app information of an app encryption declaration](./get-v1-appencryptiondeclarations-_id_-app.md)
  Get the app information from a specific app encryption declaration.
- [Read the App ID of an App Encryption Declaration](./get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read a specific app encryption declaration document](./get-v1-appencryptiondeclarationdocuments-_id_.md)
  Get detailed information about a specified App Encryption Declaration document.
- [Read the declaration document for an app encryption declaration](./get-v1-appencryptiondeclarations-_id_-appencryptiondeclarationdocument.md)
  Read the associated document for a specific App Encryption Declaration.
- [Read the App ID of an App Encryption Declaration](./get-v1-appencryptiondeclarations-_id_-relationships-app.md)
  Get the app id from a specific app encryption declaration.
- [Read the ID of the Document for an App Encryption Declaration](./get-v1-appencryptiondeclarations-_id_-relationships-appencryptiondeclarationdocument.md)
  Get the document id associated with a specific app encryption declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appencryptiondeclarations)*