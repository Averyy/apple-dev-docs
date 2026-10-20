# Read Leaderboard Set Member Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about leaderboard member set localizations.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetMemberLocalizations`

## Parameters

### Query Parameters

- `fields[gameCenterLeaderboardSetMemberLocalizations]` ([string]): **Allowed Values**: `name`, `locale`, `gameCenterLeaderboardSet`, `gameCenterLeaderboard`
- `fields[gameCenterLeaderboardSets]` ([string]) *(deprecated)*: **Allowed Values**: `referenceName`, `vendorIdentifier`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboardSet`, `localizations`, `gameCenterLeaderboards`, `releases`
- `fields[gameCenterLeaderboards]` ([string]) *(deprecated)*: **Allowed Values**: `defaultFormatter`, `referenceName`, `vendorIdentifier`, `submissionType`, `scoreSortType`, `scoreRangeStart`, `scoreRangeEnd`, `recurrenceStartDate`, `recurrenceDuration`, `recurrenceRule`, `archived`, `activityProperties`, `visibility`, `gameCenterDetail`, `gameCenterGroup`, `groupLeaderboard`, `gameCenterLeaderboardSets`, `localizations`, `releases`, `activity`, `challenge`
- `filter[gameCenterLeaderboardSet]` ([string]) *(required)* *(deprecated)*
- `filter[gameCenterLeaderboard]` ([string]) *(required)* *(deprecated)*
- `include` ([string]): **Allowed Values**: `gameCenterLeaderboardSet`, `gameCenterLeaderboard`
- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`GameCenterLeaderboardSetMemberLocalizationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set member localizations
- [Read Leaderboard Information for a Leaderboard Set Member Localization](./get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboard.md)
  Get information about a leaderboard for a specific leaderboard set member localization.
- [Read the leaderboard id for a leaderboard set member localization](./get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboard.md)
  Get the leaderboard ID for a specific leaderboard set member localization.
- [Read Leaderboard Set Information for a Leaderboard Set Member Localization](./get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-gamecenterleaderboardset.md)
  Get information about a leaderboard set for a specific leaderboard set member localization.
- [Get the leaderboard set ID for a Game Center leaderboard set member localization](./get-v1-gamecenterleaderboardsetmemberlocalizations-_id_-relationships-gamecenterleaderboardset.md)
- [Create a Leaderboard Set Member Localization](./post-v1-gamecenterleaderboardsetmemberlocalizations.md)
  Add a new leaderboard set localization.
- [Modify a Leaderboard Set Member Localization](./patch-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Edit a leaderboard set member localization.
- [Delete a Leaderboard Set Member Localization](./delete-v1-gamecenterleaderboardsetmemberlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard set member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardsetmemberlocalizations)*