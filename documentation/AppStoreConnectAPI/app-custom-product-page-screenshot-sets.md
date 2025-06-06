# App Custom Product Page Screenshot Sets

**Framework**: App Store Connect API

Create sets of app screenshots for an app custom product page localization.

#### Overview

An `appScreenshotSets` resource represents a set of screenshots that you intend to upload to App Store Connect. Create an appScreenshotSets resource as a container for all screenshots associated with a locale and display target, for example, screenshots for Simplified Chinese on an iPhone with a 6.5-inch display. Next, upload individual screenshots using the [`App Screenshots`](app-screenshots.md) resource.

## Topics

### Endpoints
- [Read App Screenshot Set Information](get-v1-appscreenshotsets-_id_.md)
  Get an app screenshot set including its display target, language, and the screenshot it contains.
- [Create an App Screenshot Set](post-v1-appscreenshotsets.md)
  Add a new screenshot set to an App Store version localization for a specific screenshot type and display size.
- [Delete an App Screenshot Set](delete-v1-appscreenshotsets-_id_.md)
  Delete an app screenshot set and all of its screenshots.
- [Get All App Screenshot IDs for an App Screenshot Set](get-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Get the ordered screenshot IDs in a screenshot set.
- [List All App Screenshots for an App Screenshot Set](get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.
- [Replace All App Screenshots for an App Screenshot Set](patch-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Change the order of the screenshots in a screenshot set.
### Objects
- [object AppScreenshotSet](appscreenshotset.md)
  The data structure that represent an app screenshot set resource.
- [object AppScreenshotSetCreateRequest](appscreenshotsetcreaterequest.md)
  The request body you use to create an app screenshot set.
- [object AppScreenshotSetResponse](appscreenshotsetresponse.md)
  A response that contains a single app screenshot set resource.
- [object AppScreenshotSetsResponse](appscreenshotsetsresponse.md)
  A response that contains a list of app screenshot set resources.
- [object AppScreenshotSetAppScreenshotsLinkagesRequest](appscreenshotsetappscreenshotslinkagesrequest.md)
  A request body you use to reorder the screenshots in a screenshot set.
- [object AppScreenshotSetAppScreenshotsLinkagesResponse](appscreenshotsetappscreenshotslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type ScreenshotDisplayType](screenshotdisplaytype.md)
  A string that represents the display type of an app screenshot.

## See Also

- [App Custom Product Page Screenshots](app-custom-product-page-screenshots.md)
  Upload and download app screenshots for an app locale and display target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-custom-product-page-screenshot-sets)*