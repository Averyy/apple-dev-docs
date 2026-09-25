# Game Center score moderations

**Framework**: App Store Connect API

Review and moderate scores players submit to your app’s leaderboards.

#### Overview

Score moderations represent the scores players submit to a Game Center leaderboard, which you review and choose to block or unblock. Blocking a score removes it from the leaderboard, and unblocking reinstates it. Use this resource to:

- Read the scores players submit to a leaderboard, and filter them by whether they’re blocked.
- Block or unblock a submitted score.

For the equivalent workflow in App Store Connect, see [`Manage scores and players`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/manage-scores-and-players/). For more information about configuring leaderboards, see [`Configure leaderboards`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/configure-leaderboards/).

## Topics

### Reading score moderations
- [List Score Moderations for a Leaderboard](get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md)
  List the score moderations for a leaderboard.
- [List Score Moderation IDs for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-relationships-gamecenterscoremoderations.md)
  List the score moderation IDs for a Game Center leaderboard.
### Blocking and unblocking scores
- [Modify a Game Center Score Moderation](patch-v1-gamecenterscoremoderations-_id_.md)
  Block or unblock a score submitted to a leaderboard.
### Objects
- [object GameCenterScoreModeration](gamecenterscoremoderation.md)
  A score submitted to a Game Center leaderboard that you review and choose to block or unblock.
- [object GameCenterScoreModerationResponse](gamecenterscoremoderationresponse.md)
  The response body for endpoints that modify a single Game Center score moderation.
- [object GameCenterScoreModerationUpdateRequest](gamecenterscoremoderationupdaterequest.md)
  The request body you use to update a Game Center score moderation.
- [object GameCenterScoreModerationsResponse](gamecenterscoremoderationsresponse.md)
  The response body for endpoints that list Game Center score moderations.
- [object GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse](gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse.md)
  The response body for endpoints that list the score moderation linkages for a Game Center leaderboard.

## See Also

- [Game Center leaderboards](game-center-leaderboards.md)
  Create and manage leaderboards for your apps.
- [Game Center leaderboard images](game-center-leaderboard-images.md)
  Read and manage image assets for Game Center leaderboards.
- [Game Center leaderboard localizations](game-center-leaderboard-localizations.md)
  Manage localizations for Game Center leaderboards.
- [Game Center leaderboard versions](game-center-leaderboard-versions.md)
  Manage versions for your Game Center leaderboards.
- [Game Center leaderboard releases](game-center-leaderboard-releases.md)
  Read, create, and delete Game Center leaderboards releases.
- [Game Center leaderboards scores](game-center-leaderboards-scores.md)
  Create and modify Game Center leaderboards scores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-score-moderations)*