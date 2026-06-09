# AppClipDefaultExperienceLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized metadata for a default App Clip experience, including the subtitle displayed on the App Clip card.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDefaultExperienceLocalization
```

## Topics

### Objects
- [object AppClipDefaultExperienceLocalization.Attributes](appclipdefaultexperiencelocalization/attributes-data.dictionary.md)
  The attributes that describe a Default App Clip Experience Localizations resource.
- [object AppClipDefaultExperienceLocalization.Relationships](appclipdefaultexperiencelocalization/relationships-data.dictionary.md)
  The relationships of the Default App Clip Experience Localizations resource you included in the request and those on which you can operate.

## Properties

- `attributes` (AppClipDefaultExperienceLocalization.Attributes): The attributes that describe the Default App Clip Experience Localizations resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Default App Clip Experience Localizations resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (AppClipDefaultExperienceLocalization.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AppClipDefaultExperienceLocalizationResponse](appclipdefaultexperiencelocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized App Clip card subtitle.
- [object AppClipDefaultExperienceLocalizationCreateRequest](appclipdefaultexperiencelocalizationcreaterequest.md)
  The request body you use to create a Default App Clip Experience Localization.
- [object AppClipDefaultExperienceLocalizationUpdateRequest](appclipdefaultexperiencelocalizationupdaterequest.md)
  The request body for updating the localized subtitle and action button label for a default App Clip experience.
- [object AppClipDefaultExperienceLocalizationsResponse](appclipdefaultexperiencelocalizationsresponse.md)
  The response body for endpoints that list localized App Clip card subtitles for a default experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperiencelocalization)*