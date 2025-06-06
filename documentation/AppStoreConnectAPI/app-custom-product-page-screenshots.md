# App Custom Product Page Screenshots

**Framework**: App Store Connect API

Upload and download app screenshots for an app locale and display target.

#### Overview

An `appScreenshots` resource represents a single app screenshot for an app locale and display target. Use this resource to:

- Upload new app screenshots to App Store Connect.
- Download existing screenshots.

To upload screenshots, begin by using the [`Create an App Screenshot Set`](post-v1-appscreenshotsets.md) endpoint for the locale and display target. To upload screenshots, you must create an asset reservation, then follow the upload operations specified in the response.

## Topics

### Endpoints
- [List app screenshot sets for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-appscreenshotsets.md)
  List the app screenshot sets for a specific custom product page localization.
- [List All App Screenshots for an App Screenshot Set](get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.
- [Read App Screenshot Information](get-v1-appscreenshots-_id_.md)
  Get information about an app screenshot and its upload and processing status.
- [Create an App Screenshot](post-v1-appscreenshots.md)
  Add a new screenshot to a screenshot set.
- [Modify an App Screenshot](patch-v1-appscreenshots-_id_.md)
  Commit an app screenshot after uploading it.
- [Delete an App Screenshot](delete-v1-appscreenshots-_id_.md)
  Delete an app screenshot that is associated with a screenshot set.
### Objects
- [object AppScreenshot](appscreenshot.md)
  The data structure that represent an App Screenshots resource.
- [object AppScreenshotCreateRequest](appscreenshotcreaterequest.md)
  The request body you use to create an App Screenshot.
- [object AppScreenshotUpdateRequest](appscreenshotupdaterequest.md)
  The request body you use to update an App Screenshot.
- [object AppScreenshotResponse](appscreenshotresponse.md)
  A response that contains a single App Screenshots resource.
- [object AppScreenshotsResponse](appscreenshotsresponse.md)
  A response that contains a list of App Screenshots resources.
- [object UploadOperation](uploadoperation.md)
  Upload instructions for assets such as app previews and app screenshots.

## See Also

- [App Custom Product Page Screenshot Sets](app-custom-product-page-screenshot-sets.md)
  Create sets of app screenshots for an app custom product page localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-custom-product-page-screenshots)*