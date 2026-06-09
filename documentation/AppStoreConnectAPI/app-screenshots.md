# App Screenshots

**Framework**: App Store Connect API

Upload and download app screenshots for an app locale and display target.

#### Overview

An `appScreenshots` resource represents a single app screenshot for an app locale and display target. Use this resource to:

- Upload new app screenshots to App Store Connect.
- Download existing screenshots.

To upload screenshots, begin by creating an [`App Screenshot Sets`](app-screenshot-sets.md) resource for the locale and display target. To upload screenshots, you must create an asset reservation, then follow the upload operations specified in the response.

> ❗ **Important**:  Some screenshot sizes are required in order to submit your app for review. You’ll get an error at submission time if you don’t provide all of the required assets. For information about screenshot requirements, see [`Screenshot specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/screenshot-specifications).

## Topics

### Getting Screenshots and Reading Information
- [List all app screenshots for an app screenshot set](get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.
- [Read app screenshot information](get-v1-appscreenshots-_id_.md)
  Get information about an app screenshot and its upload and processing status.
### Creating, Modifying, and Deleting Screenshots
- [Create an app screenshot](post-v1-appscreenshots.md)
  Add a new screenshot to a screenshot set.
- [Modify an app screenshot](patch-v1-appscreenshots-_id_.md)
  Commit an app screenshot after uploading it.
- [Delete an app screenshot](delete-v1-appscreenshots-_id_.md)
  Delete an app screenshot that is associated with a screenshot set.
### Objects
- [object AppScreenshot](appscreenshot.md)
  The data structure that represent an App Screenshots resource.
- [object AppScreenshotCreateRequest](appscreenshotcreaterequest.md)
  The request body you use to create an App Screenshot.
- [object AppScreenshotUpdateRequest](appscreenshotupdaterequest.md)
  The request body you use to update an App Screenshot.
- [object AppScreenshotResponse](appscreenshotresponse.md)
  The response body for endpoints that create, read, or modify an app screenshot.
- [object AppScreenshotsResponse](appscreenshotsresponse.md)
  The response body for endpoints that list screenshots in an app screenshot set.
- [object UploadOperation](uploadoperation.md)
  Upload instructions for assets such as app previews and app screenshots.

## See Also

- [App Screenshot Sets](app-screenshot-sets.md)
  Create sets of app screenshots to upload to App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-screenshots)*