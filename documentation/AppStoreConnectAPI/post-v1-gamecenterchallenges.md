# Create a Challenge

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a challenge to a Game Center detail or group by referencing an existing leaderboard.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)
- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)
- [App Store Connect API 4.3 release notes](app-store-connect-api-4-3-release-notes.md)
- [Configuring Game Center challenges](configuring-game-center-challenges.md)

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterChallenges`

## See Also

- [Read Challenge Information](get-v1-gamecenterchallenges-_id_.md)
  Get information for a specific Game Center challenge.
- [Read the Versions for a Challenge](get-v1-gamecenterchallenges-_id_-versions.md)
  Get a list of versions for a specific Game Center challenge.
- [Modify a Challenge](patch-v1-gamecenterchallenges-_id_.md)
  Update details for a specific Game Center challenge.
- [Modify the Leaderboard for a Game Center Challenge](patch-v1-gamecenterchallenges-_id_-relationships-leaderboardv2.md)
  Update the leaderboard relationship for a specific Game Center challenge.
- [Modify the Leaderboard for a Challenge](patch-v1-gamecenterchallenges-_id_-relationships-leaderboard.md)
  Update the relationship between a leaderbaord and a specific Game Center challenge.
- [Modify the challenges minimum platform version for a game center detail](patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions.md)
  Update the relationship between a challenges minimum platform version and a specific Game Center detail.
- [Delete a Challenge](delete-v1-gamecenterchallenges-_id_.md)
  Remove a specific Game Center challenge.
- [Read the challenges for a game center detail](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.
- [Read the challenges for a game center group](get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [List Game Center challenge IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)
- [Read the challenges for a game center group](get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [List Game Center challenge IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterchallenges)*