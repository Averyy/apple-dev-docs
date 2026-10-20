# AppClipDefaultExperienceCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships to other resources that you can set with this request.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipDefaultExperienceCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object AppClipDefaultExperienceCreateRequest.Data.Relationships.AppClip](./relationships-data.dictionary/appclip-data.dictionary.md)
  The relationship to the App Clips resource you set with the request that creates a Default App Clip Experiences resource.
- [object AppClipDefaultExperienceCreateRequest.Data.Relationships.AppClipDefaultExperienceTemplate](./relationships-data.dictionary/appclipdefaultexperiencetemplate-data.dictionary.md)
  The relationship to the Default App Clip Experience Templates resource you set with the request that creates a Default App Clip Experiences resource.
- [object AppClipDefaultExperienceCreateRequest.Data.Relationships.ReleaseWithAppStoreVersion](./relationships-data.dictionary/releasewithappstoreversion-data.dictionary.md)
  The relationship to the App Store Versions resource you set with the request that creates a Default App Clip Experiences resource.

## Properties

- `appClip` (AppClipDefaultExperienceCreateRequest.Data.Relationships.AppClip) *(required)*: The related App Clips resource.
- `appClipDefaultExperienceTemplate` (AppClipDefaultExperienceCreateRequest.Data.Relationships.AppClipDefaultExperienceTemplate): The related Default App Clip Experience Templates resource.
- `releaseWithAppStoreVersion` (AppClipDefaultExperienceCreateRequest.Data.Relationships.ReleaseWithAppStoreVersion): The related App Store Versions resource.

## See Also

### Objects
- [object AppClipDefaultExperienceCreateRequest.Data.Attributes](./attributes-data.dictionary.md)
  The attributes you set that describe the Default App Clip Experiences resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperiencecreaterequest/data-data.dictionary/relationships-data.dictionary)*