# Read Advanced App Clip Experience Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperiences/{id}`

## Parameters

- `fields[appClipAdvancedExperiences]` ([string]): Additional fields to include for each Advanced App Clip Experiences resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[localizations]` (integer): The number of included Advanced App Clip Experiences resources to return if the advanced App Clip experience localizations relationship is included.

## See Also

- [Create an Advanced App Clip Experience](post-v1-appclipadvancedexperiences.md)
  Configure a new advanced App Clip experience.
- [Modify and Delete an Advanced App Clip Experience](patch-v1-appclipadvancedexperiences-_id_.md)
  Update and delete an existing advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipadvancedexperiences-_id_)*