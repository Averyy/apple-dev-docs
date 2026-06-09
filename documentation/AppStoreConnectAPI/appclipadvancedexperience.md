# AppClipAdvancedExperience

**Framework**: App Store Connect API  
**Kind**: dictionary

A configured trigger for an App Clip experience, associated with a physical location, NFC tag, QR code, or App Store link.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAdvancedExperience
```

## Topics

### Objects
- [object AppClipAdvancedExperience.Attributes](appclipadvancedexperience/attributes-data.dictionary.md)
  The attributes that describe an Advanced App Clip Experiences resource.
- [object AppClipAdvancedExperience.Relationships](appclipadvancedexperience/relationships-data.dictionary.md)
  The relationships of the Advanced App Clip Experiences resource you included in the request and those on which you can operate.

## Properties

- `attributes` (AppClipAdvancedExperience.Attributes): The attributes that describe the Advanced App Clip Experiences resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies an Advanced App Clip Experiences resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (AppClipAdvancedExperience.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AppClipAdvancedExperienceResponse](appclipadvancedexperienceresponse.md)
  A response containing a single App Clip advanced experience configuration.
- [object AppClipAdvancedExperienceLocalization](appclipadvancedexperiencelocalization.md)
  The localized text and action button label for an App Clip advanced experience in a specific language.
- [object AppClipAdvancedExperienceCreateRequest](appclipadvancedexperiencecreaterequest.md)
  The request body you use to create an advanced App Clip experience.
- [object AppClipAdvancedExperienceUpdateRequest](appclipadvancedexperienceupdaterequest.md)
  The request body you use to update an advanced App Clip experience.
- [type AppClipAdvancedExperienceLanguage](appclipadvancedexperiencelanguage.md)
  A string value identifying the language for an App Clip advanced experience localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperience)*