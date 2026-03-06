# List All Default App Clip Experiences for an App Clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all default App Clip experiences for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}/appClipDefaultExperiences`

## Parameters

- `exists[releaseWithAppStoreVersion]` (boolean): Only include Default App Clip Experiences resources that have a related App Store Versions resource.
- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each Default App Clip Experiences resource returned by the response.
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each Default App Clip Experiences resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Default App Clip Experiences resources to return.
- `limit[appClipDefaultExperienceLocalizations]` (integer): The number of included Default App Clip Experiences resources to return if the default App Clip experience localizations relationship is included.
- `fields[appClips]` ([string])
- `fields[appClipAppStoreReviewDetails]` ([string])
- `fields[appStoreVersions]` ([string])

## See Also

- [List All Advanced App Clip Experiences for an App Clip](get-v1-appclips-_id_-appclipadvancedexperiences.md)
  Get all advanced App Clip experiences for an App Clip.
- [GET /v1/appClips/{id}/relationships/appClipAdvancedExperiences](get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)
- [GET /v1/appClips/{id}/relationships/appClipDefaultExperiences](get-v1-appclips-_id_-relationships-appclipdefaultexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_-appclipdefaultexperiences)*