# Replace all app screenshots for an app screenshot set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change the order of the screenshots in a screenshot set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}/relationships/appScreenshots`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app screenshot set resource ID from the [`List all app screenshot sets for an app store version localization`](get-v1-appstoreversionlocalizations-_id_-appscreenshotsets.md) response.

## See Also

- [Get all app screenshot ids for an app screenshot set](get-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Get the ordered screenshot IDs in a screenshot set.
- [List all app screenshots for an app screenshot set](get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appscreenshotsets-_id_-relationships-appscreenshots)*