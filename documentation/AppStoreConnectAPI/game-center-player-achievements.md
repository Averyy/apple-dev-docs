# Game Center player achievements

**Framework**: App Store Connect API

Manage Game Center achievements by player for your apps.

##### Overview

This endpoint is different than most in App Store Connect API, this’s used to create or modify a player’s achievement in your app. Any and all data you send through this endpoint overwrites existing data for the player.

## Topics

### Creating Game Center player achievements
- [POST /v1/gameCenterPlayerAchievementSubmissions](post-v1-gamecenterplayerachievementsubmissions.md)
  Add a new entry for a player’s score for a Game Center achievement.
### Objects
- [object GameCenterPlayerAchievementSubmission](gamecenterplayerachievementsubmission.md)
- [object GameCenterPlayerAchievementSubmissionCreateRequest](gamecenterplayerachievementsubmissioncreaterequest.md)
  The request body you use to create an Game Center player achievement.
- [object GameCenterPlayerAchievementSubmissionResponse](gamecenterplayerachievementsubmissionresponse.md)
  A response that contains a single Game Center player achievement resource.

## See Also

- [Game Center achievements](game-center-achievements.md)
  Manage achievements for your apps.
- [Game Center achievements localizations](game-center-achievements-localizations.md)
  Manage localizations for your achievements.
- [Game Center achievements images](game-center-achievements-images.md)
  Manage images for your Game Center achievements.
- [Game Center achievement releases](game-center-achievement-releases.md)
  Manage releases for your Game Center achievements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-player-achievements)*