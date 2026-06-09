# AppClipDefaultExperience

**Framework**: App Store Connect API  
**Kind**: dictionary

The default App Clip experience that launches when no advanced experience matches, linking to an App Store review detail and localized metadata.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDefaultExperience
```

## Topics

### Objects
- [object AppClipDefaultExperience.Attributes](appclipdefaultexperience/attributes-data.dictionary.md)
  The attributes that describe a Default App Clip Experiences resource.
- [object AppClipDefaultExperience.Relationships](appclipdefaultexperience/relationships-data.dictionary.md)
  The relationships of the Default App Clip Experiences resource you included in the request and those on which you can operate.

## Properties

- `attributes` (AppClipDefaultExperience.Attributes): The attributes that describe the Default App Clip Experiences resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Default App Clip Experiences resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (AppClipDefaultExperience.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AppClipDefaultExperienceResponse](appclipdefaultexperienceresponse.md)
  The response body for endpoints that create, read, or modify the default App Clip experience.
- [object AppClipDefaultExperienceCreateRequest](appclipdefaultexperiencecreaterequest.md)
  The request body you use to create a default App Clip experience.
- [object AppClipDefaultExperienceUpdateRequest](appclipdefaultexperienceupdaterequest.md)
  The request body you use to update a default App Clip experience.
- [object AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageRequest](appclipdefaultexperiencereleasewithappstoreversionlinkagerequest.md)
  The request body you use to relate a released App Store version with a default App Clip experience.
- [object AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageResponse](appclipdefaultexperiencereleasewithappstoreversionlinkageresponse.md)
  A response that contains the ID of a single related App Store Versions resource.
- [object AppClipAppClipDefaultExperiencesLinkagesResponse](appclipappclipdefaultexperienceslinkagesresponse.md)
- [object AppClipDefaultExperienceAppClipDefaultExperienceLocalizationsLinkagesResponse](appclipdefaultexperienceappclipdefaultexperiencelocalizationslinkagesresponse.md)
- [object AppClipDefaultExperienceLocalizationAppClipHeaderImageLinkageResponse](appclipdefaultexperiencelocalizationappclipheaderimagelinkageresponse.md)
- [object AppClipDefaultExperienceAppClipAppStoreReviewDetailLinkageResponse](appclipdefaultexperienceappclipappstorereviewdetaillinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [type AppClipAction](appclipaction.md)
  A string that represents the call-to-action verb on the App Clip card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperience)*