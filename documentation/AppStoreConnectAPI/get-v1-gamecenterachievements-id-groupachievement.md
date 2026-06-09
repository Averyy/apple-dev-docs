# List Associated Group Achievement Information for an Achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read information about the group for specific achievement.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}/groupAchievement`

## Parameters

- `fields[gameCenterAchievementLocalizations]` ([string])
- `fields[gameCenterAchievementReleases]` ([string])
- `fields[gameCenterAchievements]` ([string])
- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `include` ([string])
- `limit[localizations]` (integer)
- `limit[releases]` (integer)
- `fields[gameCenterActivities]` ([string])

## See Also

- [Read Game Center Achievement Information](get-v2-gamecenterachievements-_id_.md)
  Get information about a specific Game Center achievement.
- [List All Versions for a Game Center Achievement](get-v2-gamecenterachievements-_id_-versions.md)
  Get a list of versions for a specific Game Center achievement.
- [Get All Version IDs for a Game Center Achievement](get-v2-gamecenterachievements-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center achievement.
- [List All Achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [Read Achievement Information](get-v1-gamecenterachievements-_id_.md)
  Read information about a specific Game Center achievement.
- [List All Localizations for an Achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [Read Release Information for an Achievement](get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [List Group Achievements for an Achievement](get-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  List associated group achievements for a specific achievement.
- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievements-_id_-groupachievement)*