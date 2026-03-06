# List All Compatible Versions for a Game Center Enabled Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterEnabledVersions/{id}/compatibleVersions`

## Parameters

- `fields[gameCenterEnabledVersions]` ([string])
- `filter[app]` ([string])
- `filter[id]` ([string])
- `filter[platform]` ([string])
- `filter[versionString]` ([string])
- `include` ([string])
- `limit` (integer)
- `sort` ([string])
- `limit[compatibleVersions]` (integer)
- `fields[apps]` ([string])

## See Also

- [List All Game Center Enabled Versions for an App](get-v1-apps-_id_-gamecenterenabledversions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterenabledversions-_id_-compatibleversions)*