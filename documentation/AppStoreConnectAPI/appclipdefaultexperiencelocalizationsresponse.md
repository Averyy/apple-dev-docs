# AppClipDefaultExperienceLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localized App Clip card subtitles for a default experience.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDefaultExperienceLocalizationsResponse
```

## Properties

- `data` ([AppClipDefaultExperienceLocalization]) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object AppClipDefaultExperienceLocalization](appclipdefaultexperiencelocalization.md)
  The localized metadata for a default App Clip experience, including the subtitle displayed on the App Clip card.
- [object AppClipDefaultExperienceLocalizationResponse](appclipdefaultexperiencelocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized App Clip card subtitle.
- [object AppClipDefaultExperienceLocalizationCreateRequest](appclipdefaultexperiencelocalizationcreaterequest.md)
  The request body you use to create a Default App Clip Experience Localization.
- [object AppClipDefaultExperienceLocalizationUpdateRequest](appclipdefaultexperiencelocalizationupdaterequest.md)
  The request body for updating the localized subtitle and action button label for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperiencelocalizationsresponse)*