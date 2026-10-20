# Delete a Leaderboard Set Member Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a localization that’s associated with a leaderboard set member.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSetMemberLocalizations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing leaderboard set member localizations
- [Read Leaderboard Set Member Localization Information](./get-v1-gamecenterleaderboardsetmemberlocalizations.md)
  Get information about leaderboard member set localizations.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterleaderboardsetmemberlocalizations-_id_)*