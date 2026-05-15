# Commit an Uploaded Asset Pack to a Background Asset Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Associate an uploaded asset pack with a background asset version to finish the upload process.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)
- [Uploading and versioning Apple hosted background assets](managing-apple-hosted-background-assets.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/backgroundAssetUploadFiles/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `backgroundAssetUploadFiles` resource ID from the [`Read Background Asset Upload File Information for a Background Asset Version`](get-v1-backgroundassetversions-_id_-backgroundassetuploadfiles.md) response.

## See Also

- [Read Information for an Uploaded Asset Pack](get-v1-backgroundassetuploadfiles-_id_.md)
  Get details about an uploaded asset pack for Apple hosted background asset.
- [Create a Reservation for an Asset Pack Upload](post-v1-backgroundassetuploadfiles.md)
  Begin the process of uploading an asset pack for Apple-hosted background assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-backgroundassetuploadfiles-_id_)*