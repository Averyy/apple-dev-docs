# AppClipDefaultExperienceUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDefaultExperienceUpdateRequest
```

## Topics

### Objects
- [object AppClipDefaultExperienceUpdateRequest.Data](appclipdefaultexperienceupdaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (AppClipDefaultExperienceUpdateRequest.Data) *(required)*: The resource data.

## See Also

- [object AppClipDefaultExperience](appclipdefaultexperience.md)
  The default App Clip experience that launches when no advanced experience matches, linking to an App Store review detail and localized metadata.
- [object AppClipDefaultExperienceResponse](appclipdefaultexperienceresponse.md)
  The response body for endpoints that create, read, or modify the default App Clip experience.
- [object AppClipDefaultExperienceCreateRequest](appclipdefaultexperiencecreaterequest.md)
  The request body you use to create a default App Clip experience.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperienceupdaterequest)*