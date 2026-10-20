# Read Version Details for a Background Asset

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific background asset version.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/backgroundAssets/{id}/versions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `backgroundAssets` resource ID from the [`List all background assets for an app`](./get-v1-apps-_id_-backgroundassets.md) response.

### Query Parameters

- `fields[backgroundAssetVersionAppStoreReleases]` ([string]): **Allowed Values**: `state`, `backgroundAssetVersion`
- `fields[backgroundAssetVersionExternalBetaReleases]` ([string]): **Allowed Values**: `state`, `backgroundAssetVersion`
- `fields[backgroundAssetVersionInternalBetaReleases]` ([string]): **Allowed Values**: `state`, `backgroundAssetVersion`
- `fields[backgroundAssetVersions]` ([string]): **Allowed Values**: `createdDate`, `platforms`, `state`, `stateDetails`, `version`, `locale`, `backgroundAsset`, `internalBetaRelease`, `externalBetaRelease`, `appStoreRelease`, `assetFile`, `manifestFile`, `backgroundAssetUploadFiles`
- `filter[appStoreRelease.state]` ([string]): **Allowed Values**: `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, `REJECTED`, `PROCESSING_FOR_DISTRIBUTION`, `READY_FOR_DISTRIBUTION`, `SUPERSEDED`
- `filter[externalBetaRelease.state]` ([string]): **Allowed Values**: `READY_FOR_BETA_SUBMISSION`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `REJECTED`, `PROCESSING_FOR_TESTING`, `READY_FOR_TESTING`, `SUPERSEDED`
- `filter[internalBetaRelease.state]` ([string]): **Allowed Values**: `READY_FOR_TESTING`, `SUPERSEDED`
- `filter[state]` ([string]): **Allowed Values**: `AWAITING_UPLOAD`, `PROCESSING`, `FAILED`, `COMPLETE`
- `filter[version]` ([string])
- `include` ([string]): **Allowed Values**: `backgroundAsset`, `internalBetaRelease`, `externalBetaRelease`, `appStoreRelease`, `assetFile`, `manifestFile`
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `version`, `-version`
- `fields[backgroundAssetUploadFiles]` ([string]): **Allowed Values**: `assetDeliveryState`, `assetToken`, `assetType`, `fileName`, `fileSize`, `sourceFileChecksum`, `sourceFileChecksums`, `uploadOperations`
- `fields[backgroundAssets]` ([string]): **Allowed Values**: `archived`, `assetPackIdentifier`, `createdDate`, `usedBytes`, `app`, `versions`, `appStoreVersion`, `internalBetaVersion`, `externalBetaVersion`
- `filter[locale]` ([string])
- `filter[platforms]` ([string]): **Allowed Values**: `IOS`, `MAC_OS`, `TV_OS`, `VISION_OS`

## Responses

- `200` OK (`BackgroundAssetVersionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading background asset information
- [List all background assets for an app](./get-v1-apps-_id_-backgroundassets.md)
  Get information about the Apple-hosted background assets for a specific app.
- [List the assets packs ids for an app](./get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Read Background Assets Information](./get-v1-backgroundassets-_id_.md)
  Get details about a specific background asset.
- [Read version ids for a background asset](./get-v1-backgroundassets-_id_-relationships-versions.md)
  Get version IDs about a specific background asset version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-backgroundassets-_id_-versions)*