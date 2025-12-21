# Background assets

**Framework**: App Store Connect API

Assets for your app that you can upload and download separately from the Apple hosted app.

#### Overview

Use the Background Assets API to manage content that Apple hosts, so people can download that content outside your main app bundle on the App Store. You submit asset packs to app review; your app can have:

- Multiple background asset packs
- Versions of asset packs, each with unique content
- One active beta version and one App Store version per asset pack
- Updates to content without creating a new app version

To learn more about integrating Apple-hosted background assets into your app, see [`Downloading asset packs hosted by Apple`](https://developer.apple.comhttps://developer.apple.com/documentation/backgroundassets/downloading-asset-packs-hosted-by-apple) and to learn more about validating the behavior of your background assets, see [`Testing your asset packs locally`](https://developer.apple.comhttps://developer.apple.com/documentation/backgroundassets/testing-asset-packs-locally).

To manage Apple-hosted background assets, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `DEVELOPER`

## Topics

### Essentials
- [Uploading and versioning Apple hosted background assets](managing-apple-hosted-background-assets.md)
  Manage background assets for your App store apps.
### Relating background assets to your app
- [Create asset pack record](post-v1-backgroundassets.md)
  Create an asset pack record for your Apple-hosted background assets.
- [Create asset pack version record](post-v1-backgroundassetversions.md)
  Create an asset pack version record for your Apple-hosted background assets.
### Uploading background asset files
- [Read information for an uploaded asset pack](get-v1-backgroundassetuploadfiles-_id_.md)
  Get details about an uploaded asset pack for Apple hosted background asset.
- [Create a reservation for an asset pack upload](post-v1-backgroundassetuploadfiles.md)
  Begin the process of uploading an asset pack for Apple-hosted background assets.
- [Commit an uploaded asset pack to a background asset version](patch-v1-backgroundassetuploadfiles-_id_.md)
  Associate an uploaded asset pack with a background asset version to finish the upload process.
### Reading background asset information
- [List all assets packs for an app](get-v1-apps-_id_-backgroundassets.md)
  Get information about the Apple-hosted background assets for a specific app.
- [List the assets packs IDs for an app](get-v1-apps-_id_-relationships-backgroundassets.md)
  Get a list of the Apple hosted background asset IDs for a specific app.
- [Read background assets information](get-v1-backgroundassets-_id_.md)
  Get details about a specific background asset.
- [Read version details for a background asset](get-v1-backgroundassets-_id_-versions.md)
  Get details about a specific background asset version.
- [Read version IDs for a background asset](get-v1-backgroundassets-_id_-relationships-versions.md)
  Get version IDs about a specific background asset version.
### Reading background asset version information
- [Read background asset version App Store releases information.](get-v1-backgroundassetversionappstorereleases-_id_.md)
  Get the state of a background asset version App Store release.
- [Read background assets external beta release information](get-v1-backgroundassetversionexternalbetareleases-_id_.md)
  Get the state of a background asset version external beta release.
- [Read background assets internal beta release information](get-v1-backgroundassetversioninternalbetareleases-_id_.md)
  Get the state of a background asset version internal beta release.
- [Read background assets information](get-v1-backgroundassetversions-_id_.md)
  Get details about a specific background asset version.
- [Read background asset upload file information for a background asset version](get-v1-backgroundassetversions-_id_-backgroundassetuploadfiles.md)
  Get details about a background asset upload file for a specific background asset version.
- [Get the background asset upload files resource ID for a background asset version](get-v1-backgroundassetversions-_id_-relationships-backgroundassetuploadfiles.md)
  Get the ID for an uploaded asset pack Apple hosted background asset version
### Objects
- [object AppBackgroundAssetsLinkagesResponse](appbackgroundassetslinkagesresponse.md)
  A response that contains a list of IDs of related background assets.
- [object BackgroundAsset](backgroundasset.md)
  The data structure that represents a background asset resource.
- [object BackgroundAssetCreateRequest](backgroundassetcreaterequest.md)
  The request body you use to create a background asset record.
- [object BackgroundAssetResponse](backgroundassetresponse.md)
  A response that contains a single background asset version resource.
- [object BackgroundAssetsResponse](backgroundassetsresponse.md)
  A response that contains a list of background asset version resources.
- [object BackgroundAssetUploadFile](backgroundassetuploadfile.md)
  The data structure that represents a background asset upload file resource.
- [object BackgroundAssetUploadFileCreateRequest](backgroundassetuploadfilecreaterequest.md)
  The request body you use to create a background asset upload file.
- [object BackgroundAssetUploadFileResponse](backgroundassetuploadfileresponse.md)
  A response that contains a single background asset upload file resource.
- [object BackgroundAssetUploadFilesResponse](backgroundassetuploadfilesresponse.md)
  A response that contains a list of background asset upload file resources.
- [object BackgroundAssetUploadFileUpdateRequest](backgroundassetuploadfileupdaterequest.md)
  The request body you use to update a background asset upload file.
- [object BackgroundAssetVersion](backgroundassetversion.md)
  The data structure that represents a background asset version resource.
- [object BackgroundAssetVersionAppStoreRelease](backgroundassetversionappstorerelease.md)
  The data structure that represents a background asset version app store release resource.
- [object BackgroundAssetVersionAppStoreReleaseResponse](backgroundassetversionappstorereleaseresponse.md)
  A response that contains a single background asset version App Store release response resource.
- [type BackgroundAssetVersionAppStoreReleaseState](backgroundassetversionappstorereleasestate.md)
  A string that represents the release of a asset.
- [object BackgroundAssetVersionBackgroundAssetUploadFilesLinkagesResponse](backgroundassetversionbackgroundassetuploadfileslinkagesresponse.md)
  A response that contains a list of background asset upload files related to a background asset version.
- [object BackgroundAssetVersionCreateRequest](backgroundassetversioncreaterequest.md)
  The request body you use to create a background asset version.
- [object BackgroundAssetVersionExternalBetaRelease](backgroundassetversionexternalbetarelease.md)
  The data structure that represents a background asset version external beta release resource.
- [object BackgroundAssetVersionExternalBetaReleaseResponse](backgroundassetversionexternalbetareleaseresponse.md)
  A response that contains a single background asset version external beta release response resource.
- [type BackgroundAssetVersionExternalBetaReleaseState](backgroundassetversionexternalbetareleasestate.md)
  The data structure that represents a background asset version external beta release state.
- [object BackgroundAssetVersionInternalBetaRelease](backgroundassetversioninternalbetarelease.md)
  The data structure that represents a background asset version internal beta release resource.
- [object BackgroundAssetVersionInternalBetaReleaseResponse](backgroundassetversioninternalbetareleaseresponse.md)
  A response that contains a single background asset version internal beta release resource.
- [object BackgroundAssetVersionResponse](backgroundassetversionresponse.md)
  A response that contains a single background asset version resource.
- [object BackgroundAssetVersionsLinkagesResponse](backgroundassetversionslinkagesresponse.md)
  A response that contains a list of versions for background assets.
- [object BackgroundAssetVersionsResponse](backgroundassetversionsresponse.md)
  A response that contains a list of background asset version resources.
- [type BackgroundAssetVersionState](backgroundassetversionstate.md)
  The possible states for a background asset version.
- [type ChecksumAlgorithm](checksumalgorithm.md)
  The data structure that represents a checksum algorithm resource.
- [object Checksums](checksums.md)
  The data structure that represents a checksums resource.
- [object StateDetail](statedetail.md)
  A resource describing import validation errors, warnings and information.
- [object DeliveryFileUploadOperation](deliveryfileuploadoperation.md)
  The data structure that represents a delivery file upload operation resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/background-assets)*