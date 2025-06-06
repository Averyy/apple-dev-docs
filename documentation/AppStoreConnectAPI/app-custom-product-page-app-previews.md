# App Custom Product Page App Previews

**Framework**: App Store Connect API

Upload and download app previews for an app locale and display target.

#### Overview

An `appPreviews` resource represents a single app preview for an app locale and display target. Use this resource to:

- Upload new app previews to App Store Connect.
- Download existing app previews.
- Set a custom timestamp for the preview’s poster frame.

To upload app previews, begin by using [`Create an App Preview Set`](post-v1-apppreviewsets.md) endpoint for the locale and display target. For more information, see [`App preview specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-preview-specifications).

## Topics

### Endpoints
- [List All App Previews for an App Preview Set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Read App Preview Information](get-v1-apppreviews-_id_.md)
  Get information about an app preview and its upload and processing status.
- [Create an App Preview](post-v1-apppreviews.md)
  Add a new app preview to a preview set.
- [Modify an App Preview](patch-v1-apppreviews-_id_.md)
  Commit the app preview after uploading it, and update the poster frame timecode.
- [Delete an App Preview](delete-v1-apppreviews-_id_.md)
  Delete an app preview within a preview set.
### Objects
- [object AppPreview](apppreview.md)
  The data structure that represent an App Previews resource.
- [object AppPreviewCreateRequest](apppreviewcreaterequest.md)
  The request body you use to create an App Preview.
- [object AppPreviewUpdateRequest](apppreviewupdaterequest.md)
  The request body you use to update an App Preview.
- [object AppPreviewResponse](apppreviewresponse.md)
  A response that contains a single App Previews resource.
- [object AppPreviewsResponse](apppreviewsresponse.md)
  A response that contains a list of App Preview resources.
- [object UploadOperation](uploadoperation.md)
  Upload instructions for assets such as app previews and app screenshots.
- [type PreviewType](previewtype.md)
  String that represents the display type of an app preview.

## See Also

- [App Custom Product Page App Preview Sets](app-custom-product-page-app-preview-sets.md)
  Create sets of app previews to upload to App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-custom-product-page-app-previews)*