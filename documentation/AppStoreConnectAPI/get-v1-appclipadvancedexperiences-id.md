# Read advanced app clip experience information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperiences/{id}`

## Parameters

- `fields[appClipAdvancedExperiences]` ([string]): Additional fields to include for each advanced App Clip experiences resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[localizations]` (integer): The maximum number of related localizations resources to return.
- `fields[appClipAdvancedExperienceImages]` ([string])
- `fields[appClipAdvancedExperienceLocalizations]` ([string])
- `fields[appClips]` ([string])

## See Also

- [Create an advanced app clip experience](post-v1-appclipadvancedexperiences.md)
  Configure a new advanced App Clip experience.
- [Modify and delete an advanced app clip experience](patch-v1-appclipadvancedexperiences-_id_.md)
  Update and delete an existing advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipadvancedexperiences-_id_)*