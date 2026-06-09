# Replace all app previews for an app preview set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change the order of the app previews in a preview set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appPreviewSets/{id}/relationships/appPreviews`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview set resource ID from the [`List all app preview sets for an app store version localization`](get-v1-appstoreversionlocalizations-_id_-apppreviewsets.md) response.

## See Also

- [List all app previews for an app preview set](get-v1-apppreviewsets-_id_-apppreviews.md)
  List all ordered app previews in a preview set.
- [Get all app preview ids for an app preview set](get-v1-apppreviewsets-_id_-relationships-apppreviews.md)
  Get the ordered app preview IDs in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-apppreviewsets-_id_-relationships-apppreviews)*