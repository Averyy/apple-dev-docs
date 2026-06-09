# AppClipAdvancedExperienceCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request body.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAdvancedExperienceCreateRequest.Data
```

## Topics

### Objects
- [object AppClipAdvancedExperienceCreateRequest.Data.Attributes](appclipadvancedexperiencecreaterequest/data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new Advanced App Clip Experiences resource.
- [object AppClipAdvancedExperienceCreateRequest.Data.Relationships](appclipadvancedexperiencecreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (AppClipAdvancedExperienceCreateRequest.Data.Attributes) *(required)*: The attributes that describe the request that creates an Advanced App Clip Experiences resource.
- `relationships` (AppClipAdvancedExperienceCreateRequest.Data.Relationships) *(required)*: The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AppClipAdvancedExperienceLocalizationInlineCreate](appclipadvancedexperiencelocalizationinlinecreate.md)
  An inline object for specifying localized text and action button when creating an App Clip advanced experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperiencecreaterequest/data-data.dictionary)*