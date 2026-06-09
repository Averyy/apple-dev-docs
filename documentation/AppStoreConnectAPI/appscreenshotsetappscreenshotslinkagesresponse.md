# AppScreenshotSetAppScreenshotsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response body that contains a list of related resource IDs.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppScreenshotSetAppScreenshotsLinkagesResponse
```

## Topics

### Objects
- [object AppScreenshotSetAppScreenshotsLinkagesResponse.Data](appscreenshotsetappscreenshotslinkagesresponse/data-data.dictionary.md)
  The data element of the response body.

## Properties

- `data` ([AppScreenshotSetAppScreenshotsLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppScreenshotSet](appscreenshotset.md)
  The data structure that represent an app screenshot set resource.
- [object AppScreenshotSetCreateRequest](appscreenshotsetcreaterequest.md)
  The request body you use to create an app screenshot set.
- [object AppScreenshotSetResponse](appscreenshotsetresponse.md)
  The response body for endpoints that create or read a set of app screenshots for a display size.
- [object AppScreenshotSetsResponse](appscreenshotsetsresponse.md)
  The response body for endpoints that list app screenshot sets for an App Store version localization.
- [object AppScreenshotSetAppScreenshotsLinkagesRequest](appscreenshotsetappscreenshotslinkagesrequest.md)
  A request body you use to reorder the screenshots in a screenshot set.
- [type ScreenshotDisplayType](screenshotdisplaytype.md)
  A string that represents the display type of an app screenshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appscreenshotsetappscreenshotslinkagesresponse)*