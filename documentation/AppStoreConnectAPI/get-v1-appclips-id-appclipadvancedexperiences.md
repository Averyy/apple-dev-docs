# List All Advanced App Clip Experiences for an App Clip

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all advanced App Clip experiences for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}/appClipAdvancedExperiences`

## Parameters

- `fields[appClipAdvancedExperienceLocalizations]` ([string]): Additional fields to include for each Advanced App Clip Experiences resource returned by the response.
- `fields[appClipAdvancedExperiences]` ([string]): Additional fields to include for each Advanced App Clip Experiences resource returned by the response.
- `filter[action]` ([string]): Filter the returned advanced App Clip experiences using the verb that appears on the App Clip card.
- `filter[placeStatus]` ([string]): Filter the returned advanced App Clip experiences using the status of the associated place in Apple Maps.
- `filter[status]` ([string]): Filter the returned advanced App Clip experiences using their status.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Advanced App Clip Experiences resources to return.
- `limit[localizations]` (integer): The number of included Advanced App Clip Experiences resources to return if the advanced App Clip experience localizations relationship is included.
- `fields[appClips]` ([string])
- `fields[appClipAdvancedExperienceImages]` ([string])

## See Also

- [List All Default App Clip Experiences for an App Clip](get-v1-appclips-_id_-appclipdefaultexperiences.md)
  Get all default App Clip experiences for an App Clip.
- [GET /v1/appClips/{id}/relationships/appClipAdvancedExperiences](get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)
- [GET /v1/appClips/{id}/relationships/appClipDefaultExperiences](get-v1-appclips-_id_-relationships-appclipdefaultexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_-appclipadvancedexperiences)*