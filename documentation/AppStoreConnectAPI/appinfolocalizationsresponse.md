# AppInfoLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localized app info entries for an app.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppInfoLocalizationsResponse
```

## Properties

- `data` ([AppInfoLocalization]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)
- `included` ([AppInfo])

## See Also

- [object AppInfoLocalization](appinfolocalization.md)
  The data structure that represent an App Info Localizations resource.
- [object AppInfoLocalizationCreateRequest](appinfolocalizationcreaterequest.md)
  The request body you use to create an App Info Localization.
- [object AppInfoLocalizationResponse](appinfolocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized app info entry.
- [object AppInfoLocalizationUpdateRequest](appinfolocalizationupdaterequest.md)
  The request body you use to update an App Info Localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinfolocalizationsresponse)*