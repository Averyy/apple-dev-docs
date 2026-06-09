# App Previews

**Framework**: App Store Connect API

Upload and download app previews for an app locale and display target.

#### Overview

An `appPreviews` resource represents a single app preview for an app locale and display target. Use this resource to:

- Upload new app previews to App Store Connect.
- Download existing app previews.
- Set a custom timestamp for the preview’s poster frame.

To upload app previews, begin by creating an [`App Preview Sets`](app-preview-sets.md) resource for the locale and display target. For more information, see [`App preview specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-preview-specifications).

## Topics

### Listing App Previews and Reading Information
- [List all app previews for an app preview set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Read app preview information](get-v1-apppreviews-_id_.md)
  Get information about an app preview and its upload and processing status.
### Creating, Modifying, and Deleting App Previews
- [Create an app preview](post-v1-apppreviews.md)
  Add a new app preview to a preview set.
- [Modify an app preview](patch-v1-apppreviews-_id_.md)
  Commit the app preview after uploading it, and update the poster frame timecode.
- [Delete an app preview](delete-v1-apppreviews-_id_.md)
  Delete an app preview within a preview set.
### Objects and Data Types
- [object AppPreview](apppreview.md)
  The data structure that represent an App Previews resource.
- [object AppPreviewCreateRequest](apppreviewcreaterequest.md)
  The request body you use to create an App Preview.
- [object AppPreviewUpdateRequest](apppreviewupdaterequest.md)
  The request body you use to update an App Preview.
- [object AppPreviewResponse](apppreviewresponse.md)
  The response body for endpoints that create, read, or modify an app preview video.
- [object AppPreviewsResponse](apppreviewsresponse.md)
  The response body for endpoints that list app preview videos in a preview set.
- [object UploadOperation](uploadoperation.md)
  Upload instructions for assets such as app previews and app screenshots.
- [type PreviewType](previewtype.md)
  String that represents the display type of an app preview.
- [object PreviewFrameImage](previewframeimage.md)
  The properties that describe a preview frame image for an app preview or app event video.
- [object AppMediaVideoState](appmediavideostate.md)
  The properties that describe the state of an app preview or app event video.
- [object AppMediaPreviewFrameImageState](appmediapreviewframeimagestate.md)
  The properties that describe the state of a preview frame image for an app preveiew or app event video.

## See Also

- [Uploading App Previews](uploading-app-previews.md)
  Upload your app previews, including video files, to App Store Connect by using the asset upload APIs.
- [Uploading Assets to App Store Connect](uploading-assets-to-app-store-connect.md)
  Upload screenshots, app previews, attachments for App Review, and routing app coverage files to App Store Connect.
- [App Preview Sets](app-preview-sets.md)
  Create sets of app previews to upload to App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-previews)*