# Delete an app screenshot set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an app screenshot set and all of its screenshots.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot set resource ID from the [`List all app screenshot sets for an app store version localization`](get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md) response.

## See Also

- [Create an app screenshot set](post-v1-appscreenshotsets.md)
  Add a new screenshot set to an App Store version localization for a specific screenshot type and display size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appscreenshotsets-_id_)*