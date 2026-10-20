# Read background asset version information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific background asset version.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [App Store Connect API 4.2 release notes](./app-store-connect-api-4-2-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/backgroundAssetVersions/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `backgroundAssetVersions` resource ID from the [`Read Version Details for a Background Asset`](./get-v1-backgroundassets-_id_-versions.md) response.

### Query Parameters

- `fields[backgroundAssetVersions]` ([string]): **Allowed Values**: `createdDate`, `platforms`, `state`, `stateDetails`, `version`, `locale`, `backgroundAsset`, `internalBetaRelease`, `externalBetaRelease`, `appStoreRelease`, `assetFile`, `manifestFile`, `backgroundAssetUploadFiles`
- `include` ([string]): **Allowed Values**: `backgroundAsset`, `internalBetaRelease`, `externalBetaRelease`, `appStoreRelease`, `assetFile`, `manifestFile`
- `fields[backgroundAssetUploadFiles]` ([string]): **Allowed Values**: `assetDeliveryState`, `assetToken`, `assetType`, `fileName`, `fileSize`, `sourceFileChecksum`, `sourceFileChecksums`, `uploadOperations`
- `fields[backgroundAssetVersionAppStoreReleases]` ([string]): **Allowed Values**: `state`, `backgroundAssetVersion`
- `fields[backgroundAssetVersionExternalBetaReleases]` ([string]): **Allowed Values**: `state`, `backgroundAssetVersion`
- `fields[backgroundAssetVersionInternalBetaReleases]` ([string]): **Allowed Values**: `state`, `backgroundAssetVersion`
- `fields[backgroundAssets]` ([string]): **Allowed Values**: `archived`, `assetPackIdentifier`, `createdDate`, `usedBytes`, `app`, `versions`, `appStoreVersion`, `internalBetaVersion`, `externalBetaVersion`

## Responses

- `200` OK (`BackgroundAssetVersionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading background asset version information
- [Read background asset version app store releases information](./get-v1-backgroundassetversionappstorereleases-_id_.md)
  Get the state of a background asset version App Store release.
- [Read Background Assets External Beta Release Information](./get-v1-backgroundassetversionexternalbetareleases-_id_.md)
  Get the state of a background asset version external beta release.
- [Read Background Assets Internal Beta Release Information](./get-v1-backgroundassetversioninternalbetareleases-_id_.md)
  Get the state of a background asset version internal beta release.
- [Read Background Asset Upload File Information for a Background Asset Version](./get-v1-backgroundassetversions-_id_-backgroundassetuploadfiles.md)
  Get details about a background asset upload file for a specific background asset version.
- [Get the background asset upload files resource id for a background asset version](./get-v1-backgroundassetversions-_id_-relationships-backgroundassetuploadfiles.md)
  Get the ID for an uploaded asset pack Apple hosted background asset version


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-backgroundassetversions-_id_)*