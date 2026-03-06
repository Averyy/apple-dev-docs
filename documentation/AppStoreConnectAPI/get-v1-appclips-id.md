# Read App Clip Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}`

## Parameters

- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each App Clips resource returned by the response.
- `fields[appClips]` ([string]): Additional fields to include for each App Clips resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appClipDefaultExperiences]` (integer): The number of included App Clips resources to return if the default App Clip experience localizations relationship is included.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_)*