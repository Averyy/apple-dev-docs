# AppInfoLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a localized app info entry.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppInfoLocalizationResponse
```

## Properties

- `data` (AppInfoLocalization) *(required)*
- `links` (DocumentLinks) *(required)*
- `included` ([AppInfo])

## See Also

- [object AppInfoLocalization](appinfolocalization.md)
  The data structure that represent an App Info Localizations resource.
- [object AppInfoLocalizationCreateRequest](appinfolocalizationcreaterequest.md)
  The request body you use to create an App Info Localization.
- [object AppInfoLocalizationUpdateRequest](appinfolocalizationupdaterequest.md)
  The request body you use to update an App Info Localization.
- [object AppInfoLocalizationsResponse](appinfolocalizationsresponse.md)
  The response body for endpoints that list localized app info entries for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinfolocalizationresponse)*