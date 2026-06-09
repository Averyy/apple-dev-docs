# AppEventLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized name, short description, and long description for an App Store app event in a specific language.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventLocalization
```

## Topics

### Objects
- [object AppEventLocalization.Attributes](appeventlocalization/attributes-data.dictionary.md)
  Attributes that describe an app event localization resource.
- [object AppEventLocalization.Relationships](appeventlocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppEventLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppEventLocalization.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppEventLocalizationCreateRequest](appeventlocalizationcreaterequest.md)
  The request body you use to create an app event localization.
- [object AppEventLocalizationResponse](appeventlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized in-app event entry.
- [object AppEventLocalizationUpdateRequest](appeventlocalizationupdaterequest.md)
  The request body you use to update an app event localization update request.
- [object AppEventLocalizationsResponse](appeventlocalizationsresponse.md)
  The response body for endpoints that list localized entries for an in-app event.
- [object AppEventLocalizationAppEventScreenshotsLinkagesResponse](appeventlocalizationappeventscreenshotslinkagesresponse.md)
- [object AppEventLocalizationAppEventVideoClipsLinkagesResponse](appeventlocalizationappeventvideoclipslinkagesresponse.md)
- [object AppEventLocalizationsLinkagesResponse](appeventlocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventlocalization)*