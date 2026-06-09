# Build uploads

**Framework**: App Store Connect API

Read metadata for app builds you upload to App Store Connect.

#### Overview

Use this resource to upload and manage build uploads for your apps. Use the `BUILD_UPLOAD_STATE_UPDATED` webhook event type to get information about build upload status changes. To learn more, see [`WebhookEventType`](webhookeventtype.md).

The `buildUploads` resource represents the overall concept of the upload, whereas the `buildUploadFiles` resource represents the actual files that you upload. You can also use Xcode or Transporter to upload app binaries. To learn more, see [`Transporter`](https://developer.apple.comhttps://apps.apple.com/us/app/transporter/id1450874784).

To read information about your builds after a successful upload, use the [`Builds`](builds.md) resource.

## Topics

### Managing build uploads
- [List All Build Uploads for an App](get-v1-apps-_id_-builduploads.md)
  Get a list of all build uploads for a specific app.
- [List all build uploads ids for an app](get-v1-apps-_id_-relationships-builduploads.md)
  Get a list of all build upload Ids for a specific app.
- [Read Build Upload Information](get-v1-builduploads-_id_.md)
  Get details about a specific build upload file for an app.
- [Create a Build Upload](post-v1-builduploads.md)
  Add a new build upload to an app.
- [Remove a Build Upload](delete-v1-builduploads-_id_.md)
  Remove a specific build upload for an app.
### Reading and uploading build files
- [Read Build Upload File Information](get-v1-builduploadfiles-_id_.md)
  Get details about a specific build upload file for a build upload.
- [Read build upload file information for a build upload](get-v1-builduploads-_id_-builduploadfiles.md)
  Get build upload file information for a specific build upload.
- [Read the build upload file id for a build upload](get-v1-builduploads-_id_-relationships-builduploadfiles.md)
  Get the build upload file ID for a specific build upload.
- [Create a Reservation for a Build Upload File](post-v1-builduploadfiles.md)
  Reserve a build upload file for a specific build upload.
- [Commit a Build Upload File](patch-v1-builduploadfiles-_id_.md)
  Commit a build upload file to a specific build upload.
### Objects
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
- [object BuildUploadFilesResponse](builduploadfilesresponse.md)
  A response containing a list of file upload records for a build upload operation.
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

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Build Bundles](build-bundles.md)
  Read metadata for app and App Clip binaries included in a build you upload to App Store Connect.
- [Build Icons](build-icons.md)
  Get icons from your app’s binary that are uploaded to App Store.
- [App Encryption Declarations](app-encryption-declarations.md)
  View, and assign to builds, the declarations about types of encryption used in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-uploads)*