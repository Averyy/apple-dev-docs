# AppScreenshotSetsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list app screenshot sets for an App Store version localization.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppScreenshotSetsResponse
```

## Properties

- `data` ([AppScreenshotSet]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppScreenshotSet](appscreenshotset.md)
  The data structure that represent an app screenshot set resource.
- [object AppScreenshotSetCreateRequest](appscreenshotsetcreaterequest.md)
  The request body you use to create an app screenshot set.
- [object AppScreenshotSetResponse](appscreenshotsetresponse.md)
  The response body for endpoints that create or read a set of app screenshots for a display size.
- [object AppScreenshotSetAppScreenshotsLinkagesRequest](appscreenshotsetappscreenshotslinkagesrequest.md)
  A request body you use to reorder the screenshots in a screenshot set.
- [object AppScreenshotSetAppScreenshotsLinkagesResponse](appscreenshotsetappscreenshotslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type ScreenshotDisplayType](screenshotdisplaytype.md)
  A string that represents the display type of an app screenshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appscreenshotsetsresponse)*