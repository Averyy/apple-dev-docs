# Game Center activities

**Framework**: App Store Connect API

Manage Game Center activities for your apps.

#### Overview

To manage Game Center activities, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `MARKETING`

## Topics

### Managing Game Center activities
- [Create an activity](post-v1-gamecenteractivities.md)
  Create an activity for your Game Center detail or Game Center group.
- [Modify the achievements for a Game Center activity](post-v1-gamecenteractivities-_id_-relationships-achievements.md)
  Update the relationship between achievements and a specific Game Center activity.
- [Modify the leaderboards for a Game Center activity](post-v1-gamecenteractivities-_id_-relationships-leaderboards.md)
  Update the relationship between a leaderboard and a specific Game Center activity.
- [Read activity information](get-v1-gamecenteractivities-_id_.md)
  Get information for a specific Game Center activity.
- [Read the versions for an activity](get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [GET /v1/gameCenterActivities/{id}/relationships/versions](get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [List all activities for a Game Center detail](get-v1-gamecenterdetails-_id_-gamecenteractivities.md)
  Get activity release information for a specific Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterActivities](get-v1-gamecenterdetails-_id_-relationships-gamecenteractivities.md)
- [List all activities for a Game Center group](get-v1-gamecentergroups-_id_-gamecenteractivities.md)
  Get a list of all activities for a Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterActivities](get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
- [Modify an activity](patch-v1-gamecenteractivities-_id_.md)
  Update details for a specific Game Center activity.
- [Delete an activity](delete-v1-gamecenteractivities-_id_.md)
  Remove a specific Game Center activity.
- [Remove an achievement from an activity](delete-v1-gamecenteractivities-_id_-relationships-achievements.md)
  Remove the relationship between an achievement and a Game Center activity.
- [Remove a leaderboard from an activity](delete-v1-gamecenteractivities-_id_-relationships-leaderboards.md)
  Remove the relationship between a leaderboard and a Game Center activity.
### Objects
- [object GameCenterActivitiesResponse](gamecenteractivitiesresponse.md)
  A response that contains a list of activities resources.
- [object GameCenterActivity](gamecenteractivity.md)
  The data structure that represents a Game Center activity resource.
- [object GameCenterActivityAchievementsLinkagesRequest](gamecenteractivityachievementslinkagesrequest.md)
  The request body you use to create a link betweeen an achievement and an activity resource.
- [object GameCenterActivityLeaderboardsLinkagesRequest](gamecenteractivityleaderboardslinkagesrequest.md)
  The request body you use to create a link betweeen a leaderboard and an activity resource.
- [object GameCenterActivityCreateRequest](gamecenteractivitycreaterequest.md)
  The request body you use to create an activity resource.
- [object GameCenterActivityResponse](gamecenteractivityresponse.md)
  A response that contains a single activity resource.
- [object GameCenterActivityUpdateRequest](gamecenteractivityupdaterequest.md)
  The request body you use to update an activity.
- [object GameCenterActivityVersion](gamecenteractivityversion.md)
  The data structure that represents an activity version resource.
- [object GameCenterActivityVersionCreateRequest](gamecenteractivityversioncreaterequest.md)
  The request body you use to create an activity version resource.
- [object GameCenterActivityLocalizationImageLinkageResponse](gamecenteractivitylocalizationimagelinkageresponse.md)

## See Also

- [Game Center activity versions](game-center-activity-versions.md)
  Manage versions for your Game Center activities.
- [Game Center activity version releases](game-center-activity-version-releases.md)
  Manage version releases for your Game Center activities.
- [Game Center activity localizations](game-center-activity-localizations.md)
  Manage localizations for your Game Center activities.
- [Game Center activity images](game-center-activity-images.md)
  Manage images for your Game Center activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-activities)*