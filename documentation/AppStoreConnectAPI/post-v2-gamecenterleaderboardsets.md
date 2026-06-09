# Create a Game Center Leaderboard Set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a Game Center leaderboard set.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- 201:
- 400:
- 401:
- 403:
- 409:
- 422:
- 429:

##### Discussion

Create a leaderboard set with a relationship to one of the following:

- `gameCenterDetail`
- `gameCenterGroup`
- `gameCenterLeaderboards`

If you create a leaderboard set with `gameCenterLeaderboards`, any leaderboards you attach are in the same app. If you create a leaderboard set with `gameCenterGroup`, any leaderboards you attach are in the same group.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardSets`

## See Also

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
- [Modify the leaderboards in a leaderboard set](patch-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Edit the positions of leaderboards in an existing leaderboard set.
- [Edit the relationship between a leaderboard and a group leaderboard](patch-v1-gamecenterleaderboardsets-_id_-relationships-groupleaderboardset.md)
  Modify the group leaderboards in a leaderboard set.
- [Delete a Leaderboard Set](delete-v1-gamecenterleaderboardsets-_id_.md)
  Delete a specific leaderboard set.
- [Delete the Relationship Between a Leaderboard and a Leaderboard Set](delete-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Remove a leaderboard from a leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-gamecenterleaderboardsets)*