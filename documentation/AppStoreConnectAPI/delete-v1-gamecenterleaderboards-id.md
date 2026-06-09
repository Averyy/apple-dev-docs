# Delete a Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a leaderboard from your app.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the leaderboard resource ID from the [`Get leaderboards information`](get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md) response.

## See Also

- [Create a Game Center Leaderboard](post-v2-gamecenterleaderboards.md)
  Create a Game Center leaderboard.
- [Modify a Game Center Leaderboard](patch-v2-gamecenterleaderboards-_id_.md)
  Update a specific Game Center leaderboard.
- [Modify the Activity for a Game Center Leaderboard](patch-v2-gamecenterleaderboards-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center leaderboard.
- [Modify the Challenge for a Game Center Leaderboard](patch-v2-gamecenterleaderboards-_id_-relationships-challenge.md)
  Update the challenge relationship for a specific Game Center leaderboard.
- [Delete a Game Center Leaderboard](delete-v2-gamecenterleaderboards-_id_.md)
  Delete a specific Game Center leaderboard.
- [Create a Leaderboard](post-v1-gamecenterleaderboards.md)
  Add a new leaderboard to your app.
- [Edit a Leaderboard](patch-v1-gamecenterleaderboards-_id_.md)
  Modify the details of a leaderboard.
- [Edit the Relationship Between a Leaderboard and a Group Leaderboard](patch-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  Modify the group leadboard to which a leaderboard belongs.
- [Modify the activity for a Game Center leaderboard](patch-v1-gamecenterleaderboards-_id_-relationships-activity.md)
- [Modify the challenge for a Game Center leaderboard](patch-v1-gamecenterleaderboards-_id_-relationships-challenge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterleaderboards-_id_)*