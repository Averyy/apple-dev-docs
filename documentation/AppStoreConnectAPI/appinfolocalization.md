# AppInfoLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an App Info Localizations resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppInfoLocalization
```

## Topics

### Objects
- [object AppInfoLocalization.Attributes](appinfolocalization/attributes-data.dictionary.md)
  Attributes that describe an App Info Localizations resource.
- [object AppInfoLocalization.Relationships](appinfolocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppInfoLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppInfoLocalization.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppInfoLocalizationCreateRequest](appinfolocalizationcreaterequest.md)
  The request body you use to create an App Info Localization.
- [object AppInfoLocalizationResponse](appinfolocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized app info entry.
- [object AppInfoLocalizationUpdateRequest](appinfolocalizationupdaterequest.md)
  The request body you use to update an App Info Localization.
- [object AppInfoLocalizationsResponse](appinfolocalizationsresponse.md)
  The response body for endpoints that list localized app info entries for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinfolocalization)*