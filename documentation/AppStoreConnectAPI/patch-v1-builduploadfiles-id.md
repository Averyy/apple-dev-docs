# Commit a Build Upload File

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit a build upload file to a specific build upload.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/buildUploadFiles/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read Build Upload File Information](get-v1-builduploadfiles-_id_.md)
  Get details about a specific build upload file for a build upload.
- [GET /v1/buildUploads/{id}/buildUploadFiles](get-v1-builduploads-_id_-builduploadfiles.md)
  Get build upload file information for a specific build upload.
- [Read the Build Upload File ID for a Build Upload](get-v1-builduploads-_id_-relationships-builduploadfiles.md)
  Get the build upload file ID for a specific build upload.
- [Create a Reservation for a Build Upload File](post-v1-builduploadfiles.md)
  Reserve a build upload file for a specific build upload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-builduploadfiles-_id_)*