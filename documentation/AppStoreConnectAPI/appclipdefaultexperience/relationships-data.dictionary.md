# AppClipDefaultExperience.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the Default App Clip Experiences resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipDefaultExperience.Relationships
```

## Topics

### Objects
- [object AppClipDefaultExperience.Relationships.AppClip](./relationships-data.dictionary/appclip-data.dictionary.md)
  The data and links that describe the relationship between the Default App Clip Experiences and the App Clips resources.
- [object AppClipDefaultExperience.Relationships.AppClipAppStoreReviewDetail](./relationships-data.dictionary/appclipappstorereviewdetail-data.dictionary.md)
  The data and links that describe the relationship between the Default App Clip Experiences and the App Clip App Store Review Details resources.
- [object AppClipDefaultExperience.Relationships.AppClipDefaultExperienceLocalizations](./relationships-data.dictionary/appclipdefaultexperiencelocalizations-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Default App Clip Experiences and the Default App Clip Experience Localizations resources.
- [object AppClipDefaultExperience.Relationships.ReleaseWithAppStoreVersion](./relationships-data.dictionary/releasewithappstoreversion-data.dictionary.md)
  The data and links that describe the relationship between the Default App Clip Experiences and the App Store Versions resources.

## Properties

- `appClip` (AppClipDefaultExperience.Relationships.AppClip): The related App Clips resource.
- `appClipAppStoreReviewDetail` (AppClipDefaultExperience.Relationships.AppClipAppStoreReviewDetail): The related App Clip App Store Review Details resource.
- `appClipDefaultExperienceLocalizations` (AppClipDefaultExperience.Relationships.AppClipDefaultExperienceLocalizations): The related Default App Clip Experience Localizations resource.
- `releaseWithAppStoreVersion` (AppClipDefaultExperience.Relationships.ReleaseWithAppStoreVersion): The related App Store Versions resource.

## See Also

### Objects
- [object AppClipDefaultExperience.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a Default App Clip Experiences resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperience/relationships-data.dictionary)*