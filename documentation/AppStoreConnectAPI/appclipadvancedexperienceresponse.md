# AppClipAdvancedExperienceResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single App Clip advanced experience configuration.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAdvancedExperienceResponse
```

## Properties

- `data` (AppClipAdvancedExperience) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object AppClipAdvancedExperience](appclipadvancedexperience.md)
  A configured trigger for an App Clip experience, associated with a physical location, NFC tag, QR code, or App Store link.
- [object AppClipAdvancedExperienceLocalization](appclipadvancedexperiencelocalization.md)
  The localized text and action button label for an App Clip advanced experience in a specific language.
- [object AppClipAdvancedExperienceCreateRequest](appclipadvancedexperiencecreaterequest.md)
  The request body you use to create an advanced App Clip experience.
- [object AppClipAdvancedExperienceUpdateRequest](appclipadvancedexperienceupdaterequest.md)
  The request body you use to update an advanced App Clip experience.
- [type AppClipAdvancedExperienceLanguage](appclipadvancedexperiencelanguage.md)
  A string value identifying the language for an App Clip advanced experience localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperienceresponse)*