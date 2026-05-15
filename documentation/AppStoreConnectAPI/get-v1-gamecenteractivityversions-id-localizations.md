# List All Localizations for an Activity Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about the default localization for a specific Game Center activity version.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterActivityVersions/{id}/localizations`

## Parameters

- `fields[gameCenterActivityImages]` ([string])
- `fields[gameCenterActivityLocalizations]` ([string])
- `fields[gameCenterActivityVersions]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read the Versions for an Activity](get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [GET /v1/gameCenterActivities/{id}/relationships/versions](get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [Read Activity Version Information](get-v1-gamecenteractivityversions-_id_.md)
  Get information for a specific Game Center activity version.
- [Read Default Image Information for an Activity Version](get-v1-gamecenteractivityversions-_id_-defaultimage.md)
  Get details about the default image for a specific Game Center activity version.
- [GET /v1/gameCenterActivityVersions/{id}/relationships/defaultImage](get-v1-gamecenteractivityversions-_id_-relationships-defaultimage.md)
- [GET /v1/gameCenterActivityVersions/{id}/relationships/localizations](get-v1-gamecenteractivityversions-_id_-relationships-localizations.md)
- [Add an Activity Version Release](post-v1-gamecenteractivityversionreleases.md)
  Add a version release for a specific Game Center activity.
- [Create an Activity Version](post-v1-gamecenteractivityversions.md)
  Add an activity to a Game Center detail, group, or leaderboard.
- [Modify an Activity Version](patch-v1-gamecenteractivityversions-_id_.md)
  Update a specific activity version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenteractivityversions-_id_-localizations)*