# Delete an app preview

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app preview within a preview set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appPreviews/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app preview resource ID from the [`List all app previews for an app preview set`](get-v1-apppreviewsets-_id_-apppreviews.md) response.

## See Also

- [Create an app preview](post-v1-apppreviews.md)
  Add a new app preview to a preview set.
- [Modify an app preview](patch-v1-apppreviews-_id_.md)
  Commit the app preview after uploading it, and update the poster frame timecode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-apppreviews-_id_)*