# Read app preview information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app preview and its upload and processing status.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPreviews/{id}`

## Parameters

- `fields[appPreviews]` ([string]): Additional fields to include for each app preview resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appPreviewSets]` ([string])

## See Also

- [List all app previews for an app preview set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppreviews-_id_)*