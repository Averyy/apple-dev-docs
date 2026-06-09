# Get all app preview ids for an app preview set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the ordered app preview IDs in a preview set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}/relationships/appPreviews`

## Parameters

- `limit` (integer): The maximum number of app preview resource identifiers to return.

## See Also

- [List all app previews for an app preview set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Replace all app previews for an app preview set](patch-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Change the order of the app previews in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppreviewsets-_id_-relationships-apppreviews)*