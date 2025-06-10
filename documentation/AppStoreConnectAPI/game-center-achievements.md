# Game Center achievements

**Framework**: App Store Connect API

Manage achievements for your apps.

#### Overview

An achievement is a distinction that a player earns for reaching a milestone, or performing an action, defined by you and programmed into your app. After an achievement has gone live for any version of your app, it can’t be removed.

For more information about how to use achievements in your app, see [`Configure achievements`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/configure-achievements).

## Topics

### Reading achievements
- [List all achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [Read achievement information](get-v1-gamecenterachievements-_id_.md)
  Read information about a specific Game Center achievement.
- [List all localizations for an achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [Read release information for an achievement](get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [GET /v1/gameCenterAchievements/{id}/relationships/releases](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [List associated group achievement information for an achievement](get-v1-gamecenterachievements-_id_-groupachievement.md)
  Read information about the group for specific achievement.
- [List group achievements for an achievement](get-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  List associated group achievements for a specific achievement.
- [List achievement releases ](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/achievementReleases](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
### Creating, modifying, and deleting achievements
- [Create an achievement](post-v1-gamecenterachievements.md)
  Add an achievement to a Game Center detail.
- [Modify an achievement](patch-v1-gamecenterachievements-_id_.md)
  Modify properties for a specific achievement.
- [Modify the group for an achievement](patch-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  Modify the achievement group for a specific achievement.
- [PATCH /v1/gameCenterAchievements/{id}/relationships/activity](patch-v1-gamecenterachievements-_id_-relationships-activity.md)
- [Delete an achievement](delete-v1-gamecenterachievements-_id_.md)
  Delete a specific achievement.
### Objects
- [object GameCenterAchievement](gamecenterachievement.md)
  The data structure that represents a Game Center achievement resource.
- [object GameCenterAchievementCreateRequest](gamecenterachievementcreaterequest.md)
  A request body you use to create a Game Center achievement.
- [object GameCenterAchievementGroupAchievementLinkageRequest](gamecenterachievementgroupachievementlinkagerequest.md)
  The request body you use to attach an achievement to an achievement group.
- [object GameCenterAchievementGroupAchievementLinkageResponse](gamecenterachievementgroupachievementlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object GameCenterAchievementResponse](gamecenterachievementresponse.md)
  A response that contains a single Game Center achievement resource.
- [object GameCenterAchievementUpdateRequest](gamecenterachievementupdaterequest.md)
  The request body you use to update a Game Center achievement.
- [object GameCenterAchievementsResponse](gamecenterachievementsresponse.md)
  A response that contains a list of Game Center achievement resources.
- [object GameCenterAchievementActivityLinkageRequest](gamecenterachievementactivitylinkagerequest.md)
- [object GameCenterAchievementLocalizationsLinkagesResponse](gamecenterachievementlocalizationslinkagesresponse.md)
- [object GameCenterAchievementReleasesLinkagesResponse](gamecenterachievementreleaseslinkagesresponse.md)

## See Also

- [Game Center achievements localizations](game-center-achievements-localizations.md)
  Manage localizations for your achievements.
- [Game Center achievements images](game-center-achievements-images.md)
  Manage images for your Game Center achievements.
- [Game Center achievement releases](game-center-achievement-releases.md)
  Manage releases for your Game Center achievements.
- [Game Center player achievements](game-center-player-achievements.md)
  Manage Game Center achievements by player for your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-achievements)*