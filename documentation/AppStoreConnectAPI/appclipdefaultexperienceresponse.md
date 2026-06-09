# AppClipDefaultExperienceResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify the default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDefaultExperienceResponse
```

## Properties

- `data` (AppClipDefaultExperience) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object AppClipDefaultExperience](appclipdefaultexperience.md)
  The default App Clip experience that launches when no advanced experience matches, linking to an App Store review detail and localized metadata.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperienceresponse)*