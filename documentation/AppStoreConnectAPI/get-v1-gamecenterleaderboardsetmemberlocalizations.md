# Read leaderboard set member localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about leaderboard member set localizations.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetMemberLocalizations`

## Parameters

- `fields[gameCenterLeaderboardSetMemberLocalizations]` ([string])
- `fields[gameCenterLeaderboardSets]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `filter[gameCenterLeaderboardSet]` ([string]) *(required)*
- `filter[gameCenterLeaderboard]` ([string]) *(required)*
- `include` ([string])
- `limit` (integer)

## See Also

- [Read leaderboard information for a leaderboard set member localization](get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboard.md)
  Get information about a leaderboard for a specific leaderboard set member localization.
- [Read tge leaderboard ID for a leaderboard set member localization](get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboard.md)
  Get the leaderboard ID for a specific leaderboard set member localization.
- [Read leaderboard set information for a leaderboard set member localization](get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboardset.md)
  Get information about a leaderboard set for a specific leaderboard set member localization.
- [GET /v1/gameCenterLeaderboardSetMemberLocalizations/{id}/relationships/gameCenterLeaderboardSet](get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboardset.md)
- [Create a leaderboard set member localization](post-v1-gamecenterleaderboardsetmemberlocalizations.md)
  Add a new leaderboard set localization.
- [Modify a leaderboard set member localization](patch-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Edit a leaderboard set member localization.
- [Delete a leaderboard set member localization](delete-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard set member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardsetmemberlocalizations)*