# Game Center challenges

**Framework**: App Store Connect API

Manage Game Center challenges for your apps.

#### Overview

Use the challenges API to create and configure ways to link players directly to your content in your game. Once you create a challenge you can link it to a activity. To learn more about activies, see [`Configuring Game center activities`](configuring-game-center-activities.md).

Challenges encourage your players to invite their friends into your game for friendly competitions in score-baseed rounds. Players will see your challenges promoted throughout the Games app and other places around the OS as suggestions for enjoying their games with friends. They can invite their Game Center friends and anyone from their contacts, see scores appear in real-time, get notified at key moments until a winner is crowned, and have a rematch. Challenges are built on top of leaderboards, turning single-player game activities into a social experience players can share with their friends. To learn more about integrating challenges into your game, see [`Creating engaging challenges from leaderboards`](https://developer.apple.comhttps://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards).

To manage challenges, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `MARKETING`
- `TECHNICAL`
- `DEVELOPER`

## Topics

### Managing challenges
- [Read challenge information](get-v1-gamecenterchallenges-_id_.md)
  Get information for a specific Game Center challenge.
- [Read the versions for a challenge](get-v1-gamecenterchallenges-_id_-versions.md)
  Get a list of versions for a specific Game Center challenge.
- [Create a challenge](post-v1-gamecenterchallenges.md)
  Add a challenge to a Game Center detail or group by referencing an existing leaderboard.
- [Modify a challenge](patch-v1-gamecenterchallenges-_id_.md)
  Update details for a specific Game Center challenge.
- [Modify the leaderboard for a Game Center challenge](patch-v1-gamecenterchallenges-_id_-relationships-leaderboardv2.md)
  Update the leaderboard relationship for a specific Game Center challenge.
- [Modify the leaderboard for a challenge](patch-v1-gamecenterchallenges-_id_-relationships-leaderboard.md)
  Update the relationship between a leaderbaord and a specific Game Center challenge.
- [Modify the challenges minimum platform version for a Game Center detail](patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions.md)
  Update the relationship between a challenges minimum platform version and a specific Game Center detail.
- [Delete a challenge](delete-v1-gamecenterchallenges-_id_.md)
  Remove a specific Game Center challenge.
- [Read the challenges for a Game Center detail](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.
- [Read the challenges for a Game Center group](get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterChallenges](get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)
- [Read the challenges for a Game Center group](get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterChallenges](get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)
### Objects
- [object GameCenterChallenge](gamecenterchallenge.md)
  The data structure that represent a challenge.
- [object GameCenterChallengesResponse](gamecenterchallengesresponse.md)
  A response that contains a list of Game Center challenge resources.
- [object GameCenterChallengeCreateRequest](gamecenterchallengecreaterequest.md)
  The request body you use to create a challenge.
- [object GameCenterChallengeResponse](gamecenterchallengeresponse.md)
  A response that contains a single challenge resource.
- [object GameCenterChallengeUpdateRequest](gamecenterchallengeupdaterequest.md)
  The request body you use to update a challenge.
- [object GameCenterChallengeVersion](gamecenterchallengeversion.md)
  The data structure that represent a challenge version.
- [object GameCenterChallengeVersionRelease](gamecenterchallengeversionrelease.md)
  The data structure that represent a challenge version release.
- [object GameCenterChallengeLeaderboardV2LinkageRequest](gamecenterchallengeleaderboardv2linkagerequest.md)
  The data structure that represents a Game Center challenge leaderboard linkage request resource.
- [object GameCenterChallengeLeaderboardLinkageRequest](gamecenterchallengeleaderboardlinkagerequest.md)
- [object GameCenterChallengeVersionsLinkagesResponse](gamecenterchallengeversionslinkagesresponse.md)

## See Also

- [Configuring Game Center challenges](configuring-game-center-challenges.md)
  Setup and configure social experiences around leaderboards for friendly competition.
- [Game Center challenge versions](game-center-challenges-versions.md)
  Manage compatible Game Center challenge versions.
- [Game Center challenge version releases](game-center-challenges-version-releases.md)
  Manage compatible Game Center challenge version releases.
- [Game Center challenges localizations](game-center-challenges-localizations.md)
  Manage compatible Game Center-enabled versions.
- [Game Center challenge images](game-center-challenge-images.md)
  Manage image assets for your Game Center challenges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-challenges)*