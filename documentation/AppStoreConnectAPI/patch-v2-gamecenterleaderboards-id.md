# Modify a Game Center Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update a specific Game Center leaderboard.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- 200:
- 400:
- 401:
- 403:
- 404:
- 409:
- 422:
- 429:

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboards/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create a Game Center Leaderboard](post-v2-gamecenterleaderboards.md)
  Create a Game Center leaderboard.
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
- [PATCH /v1/gameCenterLeaderboards/{id}/relationships/activity](patch-v1-gamecenterleaderboards-_id_-relationships-activity.md)
- [PATCH /v1/gameCenterLeaderboards/{id}/relationships/challenge](patch-v1-gamecenterleaderboards-_id_-relationships-challenge.md)
- [Delete a Leaderboard](delete-v1-gamecenterleaderboards-_id_.md)
  Delete a leaderboard from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-gamecenterleaderboards-_id_)*