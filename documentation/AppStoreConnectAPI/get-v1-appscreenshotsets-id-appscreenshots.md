# List all app screenshots for an app screenshot set

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all ordered screenshots in a screenshot set.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshotSets/{id}/appScreenshots`

## Parameters

- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.
- `limit` (integer): The maximum number of app screenshot resources to return.
- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [Get all app screenshot ids for an app screenshot set](get-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Get the ordered screenshot IDs in a screenshot set.
- [Replace all app screenshots for an app screenshot set](patch-v1-appscreenshotsets-_id_-relationships-appscreenshots.md)
  Change the order of the screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshotsets-_id_-appscreenshots)*