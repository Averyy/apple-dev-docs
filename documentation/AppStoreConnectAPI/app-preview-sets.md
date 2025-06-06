# App Preview Sets

**Framework**: App Store Connect API

Create sets of app previews to upload to App Store Connect.

#### Overview

An `appPreviewSets` resource represents a collection of app previews for an app locale and display target; for example, a set of screenshots for the Simplified Chinese listing of your app for an iPhone with a 6.5” display size. Use app preview sets to:

- Begin the process of uploading app previews.
- Reorder app previews after they’re uploaded.

To upload individual previews, uses the [`App Previews`](app-previews.md) resource.

For more information about app previews, see [`App information`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-information).

## Topics

### Getting Preview Sets and Reading Information
- [Read App Preview Set Information](get-v1-apppreviewsets-_id_.md)
  Get an app preview set that includes its display target, language, and the previews it contains.
### Creating and Deleting Preview Sets
- [Create an App Preview Set](post-v1-apppreviewsets.md)
  Add a new app preview set to an App Store version localization for a specific app preview type and display size.
- [Delete an App Preview Set](delete-v1-apppreviewsets-_id_.md)
  Delete an app preview set and all of its previews.
### Listing and Reordering All Previews in a Set
- [List All App Previews for an App Preview Set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Get All App Preview IDs for an App Preview Set](get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.
- [Replace All App Previews for an App Preview Set](patch-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Change the order of the app previews in a preview set.
### Objects
- [object AppPreviewSet](apppreviewset.md)
  The data structure that represent an App Preview Sets resource.
- [object AppPreviewSetCreateRequest](apppreviewsetcreaterequest.md)
  The request body you use to create an App Preview Set.
- [object AppPreviewSetResponse](apppreviewsetresponse.md)
  A response that contains a single App Preview Sets resource.
- [object AppPreviewSetsResponse](apppreviewsetsresponse.md)
  A response that contains a list of App Preview Set resources.
- [object AppPreviewSetAppPreviewsLinkagesRequest](apppreviewsetapppreviewslinkagesrequest.md)
  A request body you use to reorder the app previews in a preview set.
- [object AppPreviewSetAppPreviewsLinkagesResponse](apppreviewsetapppreviewslinkagesresponse.md)
  A response body that contains a list of related resource IDs.

## See Also

- [Uploading App Previews](uploading-app-previews.md)
  Upload your app previews, including video files, to App Store Connect by using the asset upload APIs.
- [Uploading Assets to App Store Connect](uploading-assets-to-app-store-connect.md)
  Upload screenshots, app previews, attachments for App Review, and routing app coverage files to App Store Connect.
- [App Previews](app-previews.md)
  Upload and download app previews for an app locale and display target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-preview-sets)*