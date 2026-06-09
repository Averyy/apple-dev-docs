# AppClipDefaultExperienceLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a localized App Clip card subtitle.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDefaultExperienceLocalizationResponse
```

## Properties

- `data` (AppClipDefaultExperienceLocalization) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object AppClipDefaultExperienceLocalization](appclipdefaultexperiencelocalization.md)
  The localized metadata for a default App Clip experience, including the subtitle displayed on the App Clip card.
- [object AppClipDefaultExperienceLocalizationCreateRequest](appclipdefaultexperiencelocalizationcreaterequest.md)
  The request body you use to create a Default App Clip Experience Localization.
- [object AppClipDefaultExperienceLocalizationUpdateRequest](appclipdefaultexperiencelocalizationupdaterequest.md)
  The request body for updating the localized subtitle and action button label for a default App Clip experience.
- [object AppClipDefaultExperienceLocalizationsResponse](appclipdefaultexperiencelocalizationsresponse.md)
  The response body for endpoints that list localized App Clip card subtitles for a default experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperiencelocalizationresponse)*