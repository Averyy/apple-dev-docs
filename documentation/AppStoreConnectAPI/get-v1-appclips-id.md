# Read app clip information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific App Clip.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}`

## Parameters

- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each default App Clip experience resource returned by the response.
- `fields[appClips]` ([string]): Additional fields to include for each app clip resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appClipDefaultExperiences]` (integer): The maximum number of related default App Clip experience resources to return.
- `fields[apps]` ([string])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_)*