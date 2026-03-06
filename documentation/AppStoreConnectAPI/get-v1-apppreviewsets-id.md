# Read App Preview Set Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get an app preview set that includes its display target, language, and the previews it contains.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}`

## Parameters

- `fields[appPreviewSets]` ([string])
- `fields[appPreviews]` ([string])
- `include` ([string])
- `limit[appPreviews]` (integer)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppreviewsets-_id_)*