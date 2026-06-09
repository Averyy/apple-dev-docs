# List all compatible versions for a game center enabled version

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

- [List all game center enabled versions for an app](get-v1-apps-_id_-gamecenterenabledversions.md)
  Get a list of Game Center enabled versions for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterenabledversions-_id_-compatibleversions)*