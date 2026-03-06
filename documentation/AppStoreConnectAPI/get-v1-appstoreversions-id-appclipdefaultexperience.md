# Get the Default App Clip Experience for an App Store Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the default App Clip experience for an App Store version of your app.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/appClipDefaultExperience`

## Parameters

- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each Default App Clip Experiences resource returned by the response.
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each Default App Clip Experiences resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appClipDefaultExperienceLocalizations]` (integer): The number of included Default App Clip Experiences resources to return if the default App Clip experience localizations relationship is included.
- `fields[appClips]` ([string])
- `fields[appClipAppStoreReviewDetails]` ([string])
- `fields[appStoreVersions]` ([string])

## See Also

- [Get the Default App Clip Experiences Resource ID for an App Store Version](get-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Get the ID of an app’s related default App Clip experience.
- [Modify the Default App Clip Experience of an App Store Version](patch-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Update the relationship between an App Store version and a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-appclipdefaultexperience)*