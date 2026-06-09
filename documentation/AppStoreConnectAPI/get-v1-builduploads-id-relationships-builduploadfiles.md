# Read the build upload file id for a build upload

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the build upload file ID for a specific build upload.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildUploads/{id}/relationships/buildUploadFiles`

## Parameters

- `limit` (integer)

## See Also

- [Read Build Upload File Information](get-v1-builduploadfiles-_id_.md)
  Get details about a specific build upload file for a build upload.
- [Read build upload file information for a build upload](get-v1-builduploads-_id_-builduploadfiles.md)
  Get build upload file information for a specific build upload.
- [Create a Reservation for a Build Upload File](post-v1-builduploadfiles.md)
  Reserve a build upload file for a specific build upload.
- [Commit a Build Upload File](patch-v1-builduploadfiles-_id_.md)
  Commit a build upload file to a specific build upload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builduploads-_id_-relationships-builduploadfiles)*