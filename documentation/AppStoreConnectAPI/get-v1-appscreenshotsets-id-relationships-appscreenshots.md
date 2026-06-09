# Get all app screenshot ids for an app screenshot set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the ordered screenshot IDs in a screenshot set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}/relationships/appScreenshots`

## Parameters

- `limit` (integer): The maximum number of app screenshot resource identifiers to return.

## See Also

- [List all app screenshots for an app screenshot set](get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.
- [Replace all app screenshots for an app screenshot set](patch-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Change the order of the screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshotsets-_id_-relationships-appscreenshots)*