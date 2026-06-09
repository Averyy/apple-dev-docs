# Get the default app clip experience for an app store version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the default App Clip experience for an App Store version of your app.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/appClipDefaultExperience`

## Parameters

- `fields[appClipDefaultExperienceLocalizations]` ([string]): Additional fields to include for each App Clip default experience localization resource returned by the response.
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each App Clip default experience resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appClipDefaultExperienceLocalizations]` (integer): The maximum number of related App Clip default experience localization resources to return.
- `fields[appClips]` ([string]): Additional fields to include for each App Clip resource returned by the response.
- `fields[appClipAppStoreReviewDetails]` ([string]): Additional fields to include for each App Clip App Store review detail resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.

## See Also

- [Get the default app clip experiences resource id for an app store version](get-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Get the ID of an app’s related default App Clip experience.
- [Modify the default app clip experience of an app store version](patch-v1-appstoreversions-_id_-relationships-appclipdefaultexperience.md)
  Update the relationship between an App Store version and a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-appclipdefaultexperience)*