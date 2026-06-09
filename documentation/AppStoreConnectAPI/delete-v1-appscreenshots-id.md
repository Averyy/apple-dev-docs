# Delete an app screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app screenshot that is associated with a screenshot set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appScreenshots/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot resource ID from the [`List all app screenshots for an app screenshot set`](get-v1-appscreenshotsets-_id_-appscreenshots.md) response.

## See Also

- [Create an app screenshot](post-v1-appscreenshots.md)
  Add a new screenshot to a screenshot set.
- [Modify an app screenshot](patch-v1-appscreenshots-_id_.md)
  Commit an app screenshot after uploading it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appscreenshots-_id_)*