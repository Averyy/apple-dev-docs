# Modify an app screenshot

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit an app screenshot after uploading it.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appScreenshots/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot resource ID from the [`List all app screenshots for an app screenshot set`](get-v1-appscreenshotsets-_id_-appscreenshots.md) response.

## See Also

- [Create an app screenshot](post-v1-appscreenshots.md)
  Add a new screenshot to a screenshot set.
- [Delete an app screenshot](delete-v1-appscreenshots-_id_.md)
  Delete an app screenshot that is associated with a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appscreenshots-_id_)*