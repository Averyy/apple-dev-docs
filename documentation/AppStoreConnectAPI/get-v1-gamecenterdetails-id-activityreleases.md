# Get Activity Releases for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all activity release information for a specific Game Center detail.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game center activities](configuring-game-center-activities.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/activityReleases`

## Parameters

- `fields[gameCenterActivityVersionReleases]` ([string])
- `fields[gameCenterActivityVersions]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Get Activity Release IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-activityreleases.md)
  List all activity release IDs for a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-activityreleases)*