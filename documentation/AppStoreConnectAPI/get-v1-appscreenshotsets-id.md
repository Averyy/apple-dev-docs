# Read app screenshot set information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get an app screenshot set including its display target, language, and the screenshot it contains.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}`

## Parameters

- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.
- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appScreenshots]` (integer): The maximum number of related app screenshots resources to return.
- `fields[appCustomProductPageLocalizations]` ([string])
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshotsets-_id_)*