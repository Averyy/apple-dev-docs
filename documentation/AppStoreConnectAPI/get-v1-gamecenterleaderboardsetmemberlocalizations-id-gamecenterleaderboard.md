# Read Leaderboard Information for a Leaderboard Set Member Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a leaderboard for a specific leaderboard set member localization.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetMemberLocalizations/{id}/gameCenterLeaderboard`

## Parameters

- `fields[gameCenterDetails]` ([string])
- `fields[gameCenterGroups]` ([string])
- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `fields[gameCenterLeaderboardReleases]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `include` ([string])
- `limit[gameCenterLeaderboardSets]` (integer)
- `limit[localizations]` (integer)
- `limit[releases]` (integer)
- `fields[gameCenterActivities]` ([string])
- `fields[gameCenterChallenges]` ([string])

## See Also

- [Read Leaderboard Set Member Localization Information](get-v1-gamecenterleaderboardsetmemberlocalizations.md)
  Get information about leaderboard member set localizations.
- [Read the leaderboard id for a leaderboard set member localization](get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboard.md)
  Get the leaderboard ID for a specific leaderboard set member localization.
- [Read Leaderboard Set Information for a Leaderboard Set Member Localization](get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboardset.md)
  Get information about a leaderboard set for a specific leaderboard set member localization.
- [Get the leaderboard set ID for a Game Center leaderboard set member localization](get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboardset.md)
- [Create a Leaderboard Set Member Localization](post-v1-gamecenterleaderboardsetmemberlocalizations.md)
  Add a new leaderboard set localization.
- [Modify a Leaderboard Set Member Localization](patch-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Edit a leaderboard set member localization.
- [Delete a Leaderboard Set Member Localization](delete-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard set member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboard)*