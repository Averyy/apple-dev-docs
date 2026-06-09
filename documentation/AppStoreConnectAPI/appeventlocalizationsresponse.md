# AppEventLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localized entries for an in-app event.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventLocalizationsResponse
```

## Properties

- `data` ([AppEventLocalization]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppEventLocalization](appeventlocalization.md)
  The localized name, short description, and long description for an App Store app event in a specific language.
- [object AppEventLocalizationCreateRequest](appeventlocalizationcreaterequest.md)
  The request body you use to create an app event localization.
- [object AppEventLocalizationResponse](appeventlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized in-app event entry.
- [object AppEventLocalizationUpdateRequest](appeventlocalizationupdaterequest.md)
  The request body you use to update an app event localization update request.
- [object AppEventLocalizationAppEventScreenshotsLinkagesResponse](appeventlocalizationappeventscreenshotslinkagesresponse.md)
- [object AppEventLocalizationAppEventVideoClipsLinkagesResponse](appeventlocalizationappeventvideoclipslinkagesresponse.md)
- [object AppEventLocalizationsLinkagesResponse](appeventlocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventlocalizationsresponse)*