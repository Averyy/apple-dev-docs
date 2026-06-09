# Read app screenshot information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app screenshot and its upload and processing status.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appScreenshots/{id}`

## Parameters

- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appScreenshotSets]` ([string])

## See Also

- [List all app screenshots for an app screenshot set](get-v1-appscreenshotsets-_id_-appscreenshots.md)
  List all ordered screenshots in a screenshot set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appscreenshots-_id_)*