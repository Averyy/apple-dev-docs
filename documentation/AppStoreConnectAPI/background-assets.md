# Background assets

**Framework**: App Store Connect API

Assets for your app that you can upload and download separately from the Apple hosted app.

#### Overview

Use the Background Assets API to manage content that Apple hosts, so people can download that content outside your main app bundle on the App Store. You submit asset packs to app review; your app can have:

- Multiple background asset packs
- Versions of asset packs, each with unique content
- One active beta version and one App Store version per asset pack
- Updates to content without creating a new app version

To manage Apple hosted background assets, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `DEVELOPER`

## Topics

### Essentials
- [Uploading and versioning Apple hosted background assets](managing-apple-hosted-background-assets.md)
  Manage background assets for your App store apps.
### Relating background assets to your app
- [Create asset pack record](post-v1-backgroundassets.md)
  Create an asset pack record for your Apple hosted background assets.
- [Create asset pack version record](post-v1-backgroundassetversions.md)
  Create an asset pack version record for your Apple hosted background assets.
### Uploading background asset files
- [Read information for an uploaded asset pack](get-v1-backgroundassetuploadfiles-_id_.md)
  Get details about an uploaded asset pack for Apple hosted background asset.
- [Create a reservation for an asset pack upload](post-v1-backgroundassetuploadfiles.md)
  Begin the process of uploading an asset pack for Apple hosted background assets.
- [Commit an uploaded asset pack to a background asset version.](patch-v1-backgroundassetuploadfiles-_id_.md)
  Associate an uploaded asset pack with a background asset version to finish the upload process.
### Reading background asset information
- [List all assets packs for an app](get-v1-apps-_id_-backgroundassets.md)
  Get information about the Apple hosted background assets for a specific app.
- [Read background assets information](get-v1-backgroundassets-_id_.md)
  Get details about a specific background asset.
- [Read version details for a specific background asset](get-v1-backgroundassets-_id_-versions.md)
  Get details about a specific background asset version.
- [GET /v1/backgroundAssets/{id}/relationships/versions](get-v1-backgroundassets-_id_-relationships-versions.md)
### Reading background asset version information
- [Read background assets internal beta release information](get-v1-backgroundassetversioninternalbetareleases-_id_.md)
  Get the state of a background asset version internal beta release.
- [Read background assets information](get-v1-backgroundassetversions-_id_.md)
- [Read background asset upload file information for a background asset version.](get-v1-backgroundassetversions-_id_-backgroundassetuploadfiles.md)
  Get details about a background asset upload file for a specific background asset version.
- [Get the background asset upload files resource ID for a background asset version](get-v1-backgroundassetversions-_id_-relationships-backgroundassetuploadfiles.md)
  Get the ID for an uploaded asset pack Apple hosted background asset version
### Objects
- [object BackgroundAsset](backgroundasset.md)
  The data structure that represents a background asset resource.
- [object BackgroundAssetCreateRequest](backgroundassetcreaterequest.md)
  The request body you use to create a background asset record.
- [object BackgroundAssetResponse](backgroundassetresponse.md)
  A response that contains a single background asset version resource.
- [object BackgroundAssetVersion](backgroundassetversion.md)
  The data structure that represents a background asset version resource.
- [object BackgroundAssetVersionBackgroundAssetUploadFilesLinkagesResponse](backgroundassetversionbackgroundassetuploadfileslinkagesresponse.md)
  A response that contains a list of background asset upload files related to a background asset version.
- [object BackgroundAssetVersionCreateRequest](backgroundassetversioncreaterequest.md)
  The request body you use to create a background asset version.
- [object BackgroundAssetVersionInternalBetaRelease](backgroundassetversioninternalbetarelease.md)
  The data structure that represents a background asset version internal beta release resource.
- [object BackgroundAssetVersionInternalBetaReleaseResponse](backgroundassetversioninternalbetareleaseresponse.md)
  A response that contains a single background asset version internal beta release resource.
- [object BackgroundAssetVersionsLinkagesResponse](backgroundassetversionslinkagesresponse.md)
  A response that contains a list of versions for background assets.
- [object BackgroundAssetVersionResponse](backgroundassetversionresponse.md)
  A response that contains a single background asset version resource.
- [object BackgroundAssetVersionsResponse](backgroundassetversionsresponse.md)
  A response that contains a list of background asset version resources.
- [object BackgroundAssetsResponse](backgroundassetsresponse.md)
  A response that contains a list of background asset version resources.
- [object BackgroundAssetUploadFile](backgroundassetuploadfile.md)
  The data structure that represents a background asset upload file resource.
- [object BackgroundAssetUploadFileCreateRequest](backgroundassetuploadfilecreaterequest.md)
  The request body you use to create a background asset upload file .
- [object BackgroundAssetUploadFileResponse](backgroundassetuploadfileresponse.md)
  A response that contains a single background asset upload file resource.
- [object BackgroundAssetUploadFileUpdateRequest](backgroundassetuploadfileupdaterequest.md)
  The request body you use to update a background asset upload file.
- [object BackgroundAssetUploadFilesResponse](backgroundassetuploadfilesresponse.md)
  A response that contains a list of background asset upload file resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/background-assets)*