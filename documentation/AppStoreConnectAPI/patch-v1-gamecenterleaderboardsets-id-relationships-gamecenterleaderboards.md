# Modify the Leaderboards in Leaderboard Set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Edit the positions of leaderboards in an existing leaderboard set.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardSets/{id}/relationships/gameCenterLeaderboards`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a Game Center Leaderboard Set](post-v2-gamecenterleaderboardsets.md)
  Create a Game Center leaderboard set.
- [Add a Leaderboard to a Game Center Leaderboard Set](post-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Add a leaderboard to a Game Center leaderboard set.
- [Modify a Game Center Leaderboard Set](patch-v2-gamecenterleaderboardsets-_id_.md)
  Update a specific Game Center leaderboard set.
- [Modify the Leaderboards for a Game Center Leaderboard Set](patch-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Update the leaderboards relationship for a specific Game Center leaderboard set.
- [Delete a Game Center Leaderboard Set](delete-v2-gamecenterleaderboardsets-_id_.md)
  Delete a specific Game Center leaderboard set.
- [Delete a Game Center Leaderboard Set](delete-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Delete a specific Game Center leaderboard set.
- [Create a Leaderboard Set](post-v1-gamecenterleaderboardsets.md)
  Add a new leaderboard set to your app.
- [Create a Relationship Between a Leaderboard and a Leaderboard Set](post-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Add a leaderboard to a leaderboard set.
- [Edit a Leaderboard Set](patch-v1-gamecenterleaderboardsets-_id_.md)
  Modify the metadata for a leaderboard set.
- [Edit the Releationship Between a Leaderboard and a Group Leaderboard](patch-v1-gamecenterleaderboardsets-_id_-relationships-groupleaderboardset.md)
  Modify the group leaderboards in a leaderboard set.
- [Delete a Leaderboard Set](delete-v1-gamecenterleaderboardsets-_id_.md)
  Delete a specifc leaderboard set.
- [Delete the Relationship Between a Leaderboard and a Leaderboard Set](delete-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Remove a leaderboard from a leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards)*