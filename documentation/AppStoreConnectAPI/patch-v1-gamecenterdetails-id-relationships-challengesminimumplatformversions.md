# Modify the Challenges Minimum Platform Version for a Game Center Detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the relationship between a challenges minimum platform version and a specific Game Center detail.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/challengesMinimumPlatformVersions`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center detail resource ID from the [`Read the State of Game Center for an App`](get-v1-apps-_id_-gamecenterdetail.md) response.

## See Also

- [Read Challenge Information](get-v1-gamecenterchallenges-_id_.md)
  Get information for a specific Game Center challenge.
- [Read the Versions for a Challenge](get-v1-gamecenterchallenges-_id_-versions.md)
  Get a list of versions for a specific Game Center challenge.
- [Create a Challenge](post-v1-gamecenterchallenges.md)
  Add a challenge to a Game Center detail or group by referencing an existing leaderboard.
- [Modify a Challenge](patch-v1-gamecenterchallenges-_id_.md)
  Update details for a specific Game Center challenge.
- [Modify the Leaderboard for a Game Center Challenge](patch-v1-gamecenterchallenges-_id_-relationships-leaderboardv2.md)
  Update the leaderboard relationship for a specific Game Center challenge.
- [Modify the Leaderboard for a Challenge](patch-v1-gamecenterchallenges-_id_-relationships-leaderboard.md)
  Update the relationship between a leaderbaord and a specific Game Center challenge.
- [Delete a Challenge](delete-v1-gamecenterchallenges-_id_.md)
  Remove a specific Game Center challenge.
- [Read the Challenges for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.
- [Read the Challenges for a Game Center Group](get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterChallenges](get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)
- [Read the Challenges for a Game Center Group](get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterChallenges](get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions)*