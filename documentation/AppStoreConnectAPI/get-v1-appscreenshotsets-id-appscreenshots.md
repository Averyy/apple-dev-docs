# List All App Screenshots for an App Screenshot Set

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all ordered screenshots in a screenshot set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}/appScreenshots`

## Parameters

- `fields[appScreenshots]` ([string])
- `limit` (integer)
- `fields[appScreenshotSets]` ([string])
- `include` ([string])

## See Also

- [Get All App Screenshot IDs for an App Screenshot Set](get-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Get the ordered screenshot IDs in a screenshot set.
- [Replace All App Screenshots for an App Screenshot Set](patch-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Change the order of the screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshotsets-_id_-appscreenshots)*