# AppClipAdvancedExperienceCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create an advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAdvancedExperienceCreateRequest
```

## Topics

### Objects
- [object AppClipAdvancedExperienceLocalizationInlineCreate](appclipadvancedexperiencelocalizationinlinecreate.md)
  An inline object for specifying localized text and action button when creating an App Clip advanced experience.
- [object AppClipAdvancedExperienceCreateRequest.Data](appclipadvancedexperiencecreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (AppClipAdvancedExperienceCreateRequest.Data) *(required)*: The resource data.
- `included` ([AppClipAdvancedExperienceLocalizationInlineCreate]): The relationship data to include in the response.

## See Also

- [object AppClipAdvancedExperience](appclipadvancedexperience.md)
  A configured trigger for an App Clip experience, associated with a physical location, NFC tag, QR code, or App Store link.
- [object AppClipAdvancedExperienceResponse](appclipadvancedexperienceresponse.md)
  A response containing a single App Clip advanced experience configuration.
- [object AppClipAdvancedExperienceLocalization](appclipadvancedexperiencelocalization.md)
  The localized text and action button label for an App Clip advanced experience in a specific language.
- [object AppClipAdvancedExperienceUpdateRequest](appclipadvancedexperienceupdaterequest.md)
  The request body you use to update an advanced App Clip experience.
- [type AppClipAdvancedExperienceLanguage](appclipadvancedexperiencelanguage.md)
  A string value identifying the language for an App Clip advanced experience localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperiencecreaterequest)*