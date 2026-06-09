# BackgroundAssetVersionAppStoreRelease

**Framework**: App Store Connect API  
**Kind**: dictionary

A release of a background asset version to App Store customers, making the background content available on their devices.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```swift
object BackgroundAssetVersionAppStoreRelease
```

## Topics

### Dictionaries
- [object BackgroundAssetVersionAppStoreRelease.Attributes](backgroundassetversionappstorerelease/attributes-data.dictionary.md)
  Attributes that describe a background asset version App Store release resource.
- [object BackgroundAssetVersionAppStoreRelease.Relationships](backgroundassetversionappstorerelease/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BackgroundAssetVersionAppStoreRelease.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (BackgroundAssetVersionAppStoreRelease.Relationships)
- `type` (string) *(required)*

## See Also

- [object BackgroundAsset](backgroundasset.md)
  A downloadable content package that your app fetches in the background before or after installation, managed through Apple-hosted background assets.
- [object BackgroundAssetCreateRequest](backgroundassetcreaterequest.md)
  The request body you use to create a background asset record.
- [object BackgroundAssetResponse](backgroundassetresponse.md)
  A response containing a single background asset downloadable content package.
- [object BackgroundAssetVersion](backgroundassetversion.md)
  A specific version of a background asset, containing the upload files your app downloads after installation.
- [object BackgroundAssetVersionAppStoreReleaseResponse](backgroundassetversionappstorereleaseresponse.md)
  A response containing a single App Store release record for a background asset version.
- [object BackgroundAssetVersionBackgroundAssetUploadFilesLinkagesResponse](backgroundassetversionbackgroundassetuploadfileslinkagesresponse.md)
  A response containing the resource identifiers of upload files associated with a background asset version.
- [object BackgroundAssetVersionCreateRequest](backgroundassetversioncreaterequest.md)
  The request body you use to create a background asset version.
- [object BackgroundAssetVersionExternalBetaRelease](backgroundassetversionexternalbetarelease.md)
  A release of a background asset version to external TestFlight testers for validation.
- [object BackgroundAssetVersionExternalBetaReleaseResponse](backgroundassetversionexternalbetareleaseresponse.md)
  A response containing a single external beta release record for a background asset version.
- [object BackgroundAssetVersionInternalBetaRelease](backgroundassetversioninternalbetarelease.md)
  A release of a background asset version to internal testers, allowing you to validate asset delivery before public distribution.
- [object BackgroundAssetVersionInternalBetaReleaseResponse](backgroundassetversioninternalbetareleaseresponse.md)
  A response containing a single internal beta release record for a background asset version.
- [object BackgroundAssetVersionsLinkagesResponse](backgroundassetversionslinkagesresponse.md)
  A response containing the resource identifiers of background asset versions linked to an app.
- [object BackgroundAssetVersionResponse](backgroundassetversionresponse.md)
  A response containing a single version of a background asset.
- [object BackgroundAssetVersionsResponse](backgroundassetversionsresponse.md)
  A response containing a list of versions for a background asset.
- [object BackgroundAssetsResponse](backgroundassetsresponse.md)
  A response containing a list of background assets for an app.
- [object AppBackgroundAssetsLinkagesResponse](appbackgroundassetslinkagesresponse.md)
  A response containing the resource identifiers of background asset versions linked to an app.
- [object BackgroundAsset](backgroundasset.md)
  A downloadable content package that your app fetches in the background before or after installation, managed through Apple-hosted background assets.
- [object BackgroundAssetCreateRequest](backgroundassetcreaterequest.md)
  The request body you use to create a background asset record.
- [object BackgroundAssetResponse](backgroundassetresponse.md)
  A response containing a single background asset downloadable content package.
- [object BackgroundAssetsResponse](backgroundassetsresponse.md)
  A response containing a list of background assets for an app.
- [object BackgroundAssetUploadFile](backgroundassetuploadfile.md)
  A file included in a background asset upload operation, with its upload URL and verification checksum.
- [object BackgroundAssetUploadFileCreateRequest](backgroundassetuploadfilecreaterequest.md)
  The request body you use to create a background asset upload file.
- [object BackgroundAssetUploadFileResponse](backgroundassetuploadfileresponse.md)
  A response containing a single background asset upload file record.
- [object BackgroundAssetUploadFilesResponse](backgroundassetuploadfilesresponse.md)
  A response containing a list of upload files for a background asset.
- [object BackgroundAssetUploadFileUpdateRequest](backgroundassetuploadfileupdaterequest.md)
  The request body you use to update a background asset upload file.
- [object BackgroundAssetVersion](backgroundassetversion.md)
  A specific version of a background asset, containing the upload files your app downloads after installation.
- [object BackgroundAssetVersionAppStoreReleaseResponse](backgroundassetversionappstorereleaseresponse.md)
  A response containing a single App Store release record for a background asset version.
- [type BackgroundAssetVersionAppStoreReleaseState](backgroundassetversionappstorereleasestate.md)
  A string that represents the release state of a background asset.
- [object BackgroundAssetVersionBackgroundAssetUploadFilesLinkagesResponse](backgroundassetversionbackgroundassetuploadfileslinkagesresponse.md)
  A response containing the resource identifiers of upload files associated with a background asset version.
- [object BackgroundAssetVersionCreateRequest](backgroundassetversioncreaterequest.md)
  The request body you use to create a background asset version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/backgroundassetversionappstorerelease)*