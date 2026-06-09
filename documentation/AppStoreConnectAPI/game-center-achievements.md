# Game Center achievements

**Framework**: App Store Connect API

Manage achievements for your apps.

#### Overview

An achievement is a distinction that a player earns for reaching a milestone, or performing an action, defined by you and programmed into your app. After an achievement has gone live for any version of your app, it can’t be removed.

For more information about how to use achievements in your app, see [`Manage achievements`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/manage-achievements).

## Topics

### Reading achievements
- [Read Game Center Achievement Information](get-v2-gamecenterachievements-_id_.md)
  Get information about a specific Game Center achievement.
- [List All Versions for a Game Center Achievement](get-v2-gamecenterachievements-_id_-versions.md)
  Get a list of versions for a specific Game Center achievement.
- [Get All Version IDs for a Game Center Achievement](get-v2-gamecenterachievements-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center achievement.
- [List All Achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [Read Achievement Information](get-v1-gamecenterachievements-_id_.md)
  Read information about a specific Game Center achievement.
- [List All Localizations for an Achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [Read Release Information for an Achievement](get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [List Associated Group Achievement Information for an Achievement](get-v1-gamecenterachievements-_id_-groupachievement.md)
  Read information about the group for specific achievement.
- [List Group Achievements for an Achievement](get-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  List associated group achievements for a specific achievement.
- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
### Creating, modifying, and deleting achievements
- [Create a Game Center Achievement](post-v2-gamecenterachievements.md)
  Create a Game Center achievement.
- [Modify a Game Center Achievement](patch-v2-gamecenterachievements-_id_.md)
  Update a specific Game Center achievement.
- [Modify the Activity for a Game Center Achievement](patch-v2-gamecenterachievements-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center achievement.
- [Delete a Game Center Achievement](delete-v2-gamecenterachievements-_id_.md)
  Delete a specific Game Center achievement.
- [Create an Achievement](post-v1-gamecenterachievements.md)
  Add an achievement to a Game Center detail.
- [Modify an Achievement](patch-v1-gamecenterachievements-_id_.md)
  Modify properties for a specific achievement.
- [Modify the Group for an Achievement](patch-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  Modify the achievement group for a specific achievement.
- [Modify the activity for a Game Center achievement](patch-v1-gamecenterachievements-_id_-relationships-activity.md)
- [Delete an Achievement](delete-v1-gamecenterachievements-_id_.md)
  Delete a specific achievement.
### Objects
- [object GameCenterAchievementV2](gamecenterachievementv2.md)
  The data structure that represents a Game Center achievement v2 resource.
- [object GameCenterAchievementV2CreateRequest](gamecenterachievementv2createrequest.md)
  The request body you use to create a Game Center achievement v2.
- [object GameCenterAchievementV2Response](gamecenterachievementv2response.md)
  A response that contains a single Game Center achievement v2 resource.
- [object GameCenterAchievementV2UpdateRequest](gamecenterachievementv2updaterequest.md)
  The request body you use to update a Game Center achievement v2.
- [object GameCenterAchievementsV2Response](gamecenterachievementsv2response.md)
  A response that contains a single Game Center achievement v2 resource.
- [object GameCenterAchievementV2ActivityLinkageRequest](gamecenterachievementv2activitylinkagerequest.md)
  The data structure that represents a Game Center achievement v2 activity linkage request resource.
- [object GameCenterAchievementV2VersionsLinkagesResponse](gamecenterachievementv2versionslinkagesresponse.md)
  A response that contains a list of Game Center achievement v2 version linkage resources.
- [object GameCenterAchievement](gamecenterachievement.md)
  A reward in Game Center that players earn by completing specific challenges or milestones in a game.
- [object GameCenterAchievementCreateRequest](gamecenterachievementcreaterequest.md)
  A request body you use to create a Game Center achievement.
- [object GameCenterAchievementGroupAchievementLinkageRequest](gamecenterachievementgroupachievementlinkagerequest.md)
  The request body you use to attach an achievement to an achievement group.
- [object GameCenterAchievementGroupAchievementLinkageResponse](gamecenterachievementgroupachievementlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object GameCenterAchievementResponse](gamecenterachievementresponse.md)
  The response body for endpoints that create, read, or modify a single Game Center achievement.
- [object GameCenterAchievementUpdateRequest](gamecenterachievementupdaterequest.md)
  The request body you use to update a Game Center achievement.
- [object GameCenterAchievementsResponse](gamecenterachievementsresponse.md)
  The response body for endpoints that list Game Center achievements.
- [object GameCenterAchievementActivityLinkageRequest](gamecenterachievementactivitylinkagerequest.md)
- [object GameCenterAchievementLocalizationsLinkagesResponse](gamecenterachievementlocalizationslinkagesresponse.md)
- [object GameCenterAchievementReleasesLinkagesResponse](gamecenterachievementreleaseslinkagesresponse.md)
- [object StringToStringMap](stringtostringmap.md)
  A dictionary object mapping arbitrary string keys to string values, used for flexible key-value metadata.

## See Also

- [Game Center achievements localizations](game-center-achievements-localizations.md)
  Manage localizations for your achievements.
- [Game Center achievements images](game-center-achievements-images.md)
  Manage images for your Game Center achievements.
- [Game Center achievement versions](game-center-achievement-versions.md)
  Manage versions for your Game Center achievements.
- [Game Center achievement releases](game-center-achievement-releases.md)
  Manage releases for your Game Center achievements.
- [Game Center player achievements](game-center-player-achievements.md)
  Manage Game Center achievements by player for your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-achievements)*