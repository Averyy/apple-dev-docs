# Game Center leaderboards scores

**Framework**: App Store Connect API

Create and modify Game Center leaderboards scores.

#### Overview

This endpoint is different than most in App Store Connect API, with this you can create or modify a player’s leaderboard score in your app. Any and all data you send through this endpoint overwrites existing data for the player’s score.

> 💡 **Tip**:  These endpoint requires information from GameKit, specifically [`gamePlayerID`](https://developer.apple.com/documentation/GameKit/GKPlayer/gamePlayerID).

## Topics

### Managing Game Center leaderboard scores
- [POST /v1/gameCenterLeaderboardEntrySubmissions](post-v1-gamecenterleaderboardentrysubmissions.md)
  Add a new score for a player to a leaderboard.
### Objects
- [object GameCenterLeaderboardEntrySubmission](gamecenterleaderboardentrysubmission.md)
  The data structure that represent an Game Center leaderboard entry submission resource.
- [object GameCenterLeaderboardEntrySubmissionCreateRequest](gamecenterleaderboardentrysubmissioncreaterequest.md)
  The request body you use to create an Game Center leaderboard entry submssion.
- [object GameCenterLeaderboardEntrySubmissionResponse](gamecenterleaderboardentrysubmissionresponse.md)
  A response that contains a Game Center leaderboard entry submission.

## See Also

- [Game Center leaderboards](game-center-leaderboards.md)
  Create and manage leaderboards for your apps.
- [Game Center leaderboard images](game-center-leaderboard-images.md)
  Read and manage image assets for Game Center leaderboards.
- [Game Center leaderboard releases](game-center-leaderboard-releases.md)
  Read, create, and delete Game Center leaderboards releases.
- [Game Center leaderboard localizations](game-center-leaderboard-localizations.md)
  Manage localizations for Game Center leaderboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-leaderboards-scores)*