# Read Build Upload Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific build upload file for an app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildUploads/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[buildUploads]` ([string]): **Allowed Values**: `cfBundleShortVersionString`, `cfBundleVersion`, `createdDate`, `state`, `platform`, `uploadedDate`, `build`, `assetFile`, `assetDescriptionFile`, `assetSpiFile`, `buildUploadFiles`
- `include` ([string]): **Allowed Values**: `build`, `assetFile`, `assetDescriptionFile`, `assetSpiFile`
- `fields[buildUploadFiles]` ([string]): **Allowed Values**: `assetDeliveryState`, `assetToken`, `assetType`, `fileName`, `fileSize`, `sourceFileChecksums`, `uploadOperations`, `uti`
- `fields[builds]` ([string]): **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`

## Responses

- `200` OK (`BuildUploadResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)

## See Also

### Managing build uploads
- [List All Build Uploads for an App](./get-v1-apps-_id_-builduploads.md)
  Get a list of all build uploads for a specific app.
- [List all build uploads ids for an app](./get-v1-apps-_id_-relationships-builduploads.md)
  Get a list of all build upload Ids for a specific app.
- [Create a Build Upload](./post-v1-builduploads.md)
  Add a new build upload to an app.
- [Remove a Build Upload](./delete-v1-builduploads-_id_.md)
  Remove a specific build upload for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builduploads-_id_)*