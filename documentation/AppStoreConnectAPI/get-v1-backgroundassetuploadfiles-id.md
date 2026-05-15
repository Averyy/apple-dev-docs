# Read Information for an Uploaded Asset Pack

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about an uploaded asset pack for Apple hosted background asset.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/backgroundAssetUploadFiles/{id}`

## Parameters

- `fields[backgroundAssetUploadFiles]` ([string])

## See Also

- [Create a Reservation for an Asset Pack Upload](post-v1-backgroundassetuploadfiles.md)
  Begin the process of uploading an asset pack for Apple-hosted background assets.
- [Commit an Uploaded Asset Pack to a Background Asset Version](patch-v1-backgroundassetuploadfiles-_id_.md)
  Associate an uploaded asset pack with a background asset version to finish the upload process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-backgroundassetuploadfiles-_id_)*