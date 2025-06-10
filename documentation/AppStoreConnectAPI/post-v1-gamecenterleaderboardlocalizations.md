# Create a leaderboard localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a new leaderboard localization.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

Use leaderboard formatters to specify the unit of measurement for a Game Center leaderboard. There is a new required attribute `defaultFormatter` when you use [`Create a leaderboard`](post-v1-gamecenterleaderboards.md), which gives all your localizations the same formatter. You can also optionally use `formatterOverride` to override a specific leaderboard localization when calling [`Create a leaderboard localization`](post-v1-gamecenterleaderboardlocalizations.md) or [`Modify a leaderboard localization`](patch-v1-gamecenterleaderboardlocalizations-_id_.md).

Before App Store Connect API version 3.0, formatters were based on localizations and were required for each localization. Legacy leaderboards created before the new addition of the Game Center APIs will not have a `defaultFormatter` value, the value would be `null` in this case. Any localizations created before the new addition of the Game Center APIs will always have a `formatterOverride`.

##### Example Request and Response

## See Also

- [List all localizations for a leaderboard](get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/localizations](get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [Read leaderboard localization information](get-v1-gamecenterleaderboardlocalizations-_id_.md)
  Get information about a leaderboard localization.
- [Read the image for a leaderboard localization](get-v1-gamecenterleaderboardlocalizations-_id_-gamecenterleaderboardimage.md)
  Get information about the image associated with a leaderboard localization.
- [GET /v1/gameCenterLeaderboardLocalizations/{id}/relationships/gameCenterLeaderboardImage](get-v1-gamecenterleaderboardlocalizations-_id_-relationships-gamecenterleaderboardimage.md)
- [Modify a leaderboard localization](patch-v1-gamecenterleaderboardlocalizations-_id_.md)
  Edit a leaderboard localization.
- [Delete a leaderboard localization](delete-v1-gamecenterleaderboardlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterleaderboardlocalizations)*