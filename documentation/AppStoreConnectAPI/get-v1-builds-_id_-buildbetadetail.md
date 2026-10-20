# Read the build beta details information of a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the beta test details for a specific build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/buildBetaDetail`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `fields[buildBetaDetails]` ([string]): Fields to return for included related types.

  **Allowed Values**: `autoNotifyEnabled`, `internalBuildState`, `externalBuildState`, `build`
- `fields[builds]` ([string]): **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `include` ([string]): **Allowed Values**: `build`

## Responses

- `200` OK (`BuildBetaDetailResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Information Associated with Builds
- [Get the build beta detail ID for a build](./get-v1-builds-_id_-relationships-buildbetadetail.md)
- [Read the app encryption declaration of a build](./get-v1-builds-_id_-appencryptiondeclaration.md)
  Read an app encryption declaration associated with a specific build.
- [Get the app encryption declaration id for a build](./get-v1-builds-_id_-relationships-appencryptiondeclaration.md)
  Get the beta app encryption declaration resource ID associated with a build.
- [List all beta build localizations of a build](./get-v1-builds-_id_-betabuildlocalizations.md)
  Get a list of localized beta test information for a specific build.
- [List beta build localization IDs for a build](./get-v1-builds-_id_-relationships-betabuildlocalizations.md)
- [List all diagnostic signatures for a build](./get-v1-builds-_id_-diagnosticsignatures.md)
  List the aggregate backtrace signatures captured for a specific build.
- [List all icons for a build](./get-v1-builds-_id_-icons.md)
  List all the icons for various platforms delivered with a build.
- [List icon IDs for a build](./get-v1-builds-_id_-relationships-icons.md)
- [List diagnostic signature IDs for a build](./get-v1-builds-_id_-relationships-diagnosticsignatures.md)
- [Get the App Store version ID for a build](./get-v1-builds-_id_-relationships-appstoreversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-buildbetadetail)*