# Read App Screenshot Set Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get an app screenshot set including its display target, language, and the screenshot it contains.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}`

## Parameters

- `fields[appScreenshotSets]` ([string])
- `fields[appScreenshots]` ([string])
- `include` ([string])
- `limit[appScreenshots]` (integer)
- `fields[appCustomProductPageLocalizations]` ([string])
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshotsets-_id_)*