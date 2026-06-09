# AppScreenshotSet

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an app screenshot set resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppScreenshotSet
```

## Topics

### Objects
- [object AppScreenshotSet.Attributes](appscreenshotset/attributes-data.dictionary.md)
  Attributes that describe an App Screenshot Sets resource.
- [object AppScreenshotSet.Relationships](appscreenshotset/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppScreenshotSet.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppScreenshotSet.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppScreenshotSetCreateRequest](appscreenshotsetcreaterequest.md)
  The request body you use to create an app screenshot set.
- [object AppScreenshotSetResponse](appscreenshotsetresponse.md)
  The response body for endpoints that create or read a set of app screenshots for a display size.
- [object AppScreenshotSetsResponse](appscreenshotsetsresponse.md)
  The response body for endpoints that list app screenshot sets for an App Store version localization.
- [object AppScreenshotSetAppScreenshotsLinkagesRequest](appscreenshotsetappscreenshotslinkagesrequest.md)
  A request body you use to reorder the screenshots in a screenshot set.
- [object AppScreenshotSetAppScreenshotsLinkagesResponse](appscreenshotsetappscreenshotslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type ScreenshotDisplayType](screenshotdisplaytype.md)
  A string that represents the display type of an app screenshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appscreenshotset)*