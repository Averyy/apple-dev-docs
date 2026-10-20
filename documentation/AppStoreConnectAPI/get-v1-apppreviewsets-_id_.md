# Read app preview set information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get an app preview set that includes its display target, language, and the previews it contains.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}`

## Parameters

- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.
- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appPreviews]` (integer): The maximum number of related app previews resources to return.
- `fields[appCustomProductPageLocalizations]` ([string])
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string])
- `fields[appStoreVersionLocalizations]` ([string])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppreviewsets-_id_)*