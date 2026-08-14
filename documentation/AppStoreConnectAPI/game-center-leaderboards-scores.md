# Game Center leaderboards scores

**Framework**: App Store Connect API

Create and modify Game Center leaderboards scores.

#### Overview

This endpoint is different than most in App Store Connect API, with this you can create or modify a player’s leaderboard score in your app. Any and all data you send through this endpoint overwrites existing data for the player’s score.

> 💡 **Tip**:  These endpoint requires information from GameKit, specifically [`gamePlayerID`](https://developer.apple.com/documentation/gamekit/gkplayer/gameplayerid).

## Topics

### Managing Game Center leaderboard scores
- [Add a Score to a Leaderbaord](post-v1-gamecenterleaderboardentrysubmissions.md)
  Add a new score for a player to a leaderboard.
### Objects
- [object GameCenterLeaderboardEntrySubmission](gamecenterleaderboardentrysubmission.md)
  A player’s score submission to a Game Center leaderboard, including the score value and context.
- [object GameCenterLeaderboardEntrySubmissionCreateRequest](gamecenterleaderboardentrysubmissioncreaterequest.md)
  The request body you use to create a Game Center leaderboard entry submission.
- [object GameCenterLeaderboardEntrySubmissionResponse](gamecenterleaderboardentrysubmissionresponse.md)
  A response confirming a player’s score submission to a Game Center leaderboard.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-leaderboards-scores)*