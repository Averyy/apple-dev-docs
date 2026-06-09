# BuildUploadFilesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of file upload records for a build upload operation.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```swift
object BuildUploadFilesResponse
```

## Properties

- `data` ([BuildUploadFile]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object BuildUpload](buildupload.md)
  A multi-file upload operation for submitting an app build to App Store Connect.
- [object BuildUploadBuildUploadFilesLinkagesResponse](builduploadbuilduploadfileslinkagesresponse.md)
  A response containing the resource identifiers of upload files associated with a build upload.
- [object BuildUploadCreateRequest](builduploadcreaterequest.md)
  The request body for initiating a build upload operation.
- [object BuildUploadFile](builduploadfile.md)
  A single file upload record within a build upload operation, containing the upload URL and checksum for verification.
- [object BuildUploadFileCreateRequest](builduploadfilecreaterequest.md)
  The request body for creating a file upload record within a build upload operation.
- [object BuildUploadFileResponse](builduploadfileresponse.md)
  A response containing a single file upload record for a build upload.
- [object BuildUploadFileUpdateRequest](builduploadfileupdaterequest.md)
  The request body you use to commit a build upload file.
- [object BuildUploadResponse](builduploadresponse.md)
  A response containing a single build upload operation record.
- [object BuildUploadsResponse](builduploadsresponse.md)
  A response containing a list of build upload operations.
- [type BuildUploadState](builduploadstate.md)
  A string that represents the state of a build upload.
- [object AppBuildUploadsLinkagesResponse](appbuilduploadslinkagesresponse.md)
  A response containing the resource identifiers of builds associated with an app’s upload operations.
- [object StateDetail](statedetail.md)
  A resource describing import validation errors, warnings and information.
- [object DeliveryFileUploadOperation](deliveryfileuploadoperation.md)
  An upload operation descriptor containing the URL, HTTP method, and required headers for uploading a background asset file to Apple’s servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/builduploadfilesresponse)*