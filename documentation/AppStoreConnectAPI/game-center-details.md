# Game Center details

**Framework**: App Store Connect API

Manage enablement, achievement, leaderboard, and localization details for your apps.

#### Overview

Game Center details is the top-level endpoint for Game Center information for your apps. Use this resource to:

- Enable Game Center for an app.
- Read information about specific types of Game Center data, including achievements, leaderboards, and localizations.

To enable Game Center, begin by calling [`Enable Game Center for an App`](post-v1-gamecenterdetails.md). Then you can create and configure achievements, leaderboards, leaderboard sets, and more.

## Topics

### Reading Game Center details
- [Read the State of Game Center for an App](get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [Read Game Center Details](get-v1-gamecenterdetails-_id_.md)
  Read a specific Game Center detail and related information.
- [Read App Versions for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterAppVersions](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [Read the Groups in a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecentergroup.md)
  Get a list of groups in a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterGroup](get-v1-gamecenterdetails-_id_-relationships-gamecentergroup.md)
- [Read the Challenges for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.
- [Read Challenge IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterchallenges.md)
  List all the challenge IDs for a specific Game Center detail.
### Creating and editing Game Center details
- [Enable Game Center for an App](post-v1-gamecenterdetails.md)
  Create a Game Center detail for an app.
- [Modify a Game Center Detail for an App](patch-v1-gamecenterdetails-_id_.md)
  Edit challenge state, default leaderboards, and groups.
- [Modify the Achievements for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievementsv2.md)
  Update the achievements relationship for a specific Game Center detail.
- [Modify the Leaderboard Sets for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Update the leaderboard sets relationship for a specific Game Center detail.
- [Modify the Leaderboards for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Update the leaderboards relationship for a specific Game Center detail.
- [Modify the Associated Leaderboard Sets for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  Edit the associated leaderboard sets for a Game Center detail.
- [Modify the Associated Leaderboards for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  Edit the associated leaderboards for a Game Center detail.
- [Modify the Challenges Minimum Platform Version for a Game Center Detail](patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions.md)
  Update the relationship between a challenges minimum platform version and a specific Game Center detail.
### Reading and editing Game Center detail achievements
- [List All Game Center Achievements for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterachievementsv2.md)
  Get a list of achievements for a specific Game Center detail.
- [Get All Achievement IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterachievementsv2.md)
  Get a list of achievement resource IDs for a specific Game Center detail.
- [List All Achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [List Achievement Releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/achievementReleases](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)
- [List Achievements](get-v1-gamecenterdetails-_id_-relationships-gamecenterachievements.md)
  List the achievements for a Game Center detail.
- [Modify Associated Achievements](patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievements.md)
  Modify the achievements for a Game Center detail.
### Reading and editing Game Center detail leaderboards
- [List All Game Center Leaderboards for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsv2.md)
  Get a list of leaderboards for a specific Game Center detail.
- [Get All Leaderboard IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsv2.md)
  Get a list of leaderboard resource IDs for a specific Game Center detail.
- [Read Leaderboard Releases](get-v1-gamecenterdetails-_id_-leaderboardreleases.md)
  List all leaderboard releases for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/leaderboardReleases](get-v1-gamecenterdetails-_id_-relationships-leaderboardreleases.md)
- [Read Leaderboard Information](get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md)
  Get all leaderboards and related information for a Game Center detail.
- [List Leaderboards](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  ​List all leaderboards for a Game Center detail.
### Reading and editing leaderboard sets in a Game Center detail
- [List All Game Center Leaderboard Sets for a Game Center Detail](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard sets for a specific Game Center detail.
- [Get All Leaderboard Set IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard set resource IDs for a specific Game Center detail.
- [Read Leaderboard Set Information](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsets.md)
  Get all leaderboard sets and related information for a Game Center detail.
- [List Leaderboard Sets](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  List all leaderboards for a Game Center detail.
- [Read Leaderboard Set Release Information](get-v1-gamecenterdetails-_id_-leaderboardsetreleases.md)
  List all leaderboard set releases for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/leaderboardSetReleases](get-v1-gamecenterdetails-_id_-relationships-leaderboardsetreleases.md)
### Reading Game center activity information
- [Get Activity Releases for a Game Center Detail](get-v1-gamecenterdetails-_id_-activityreleases.md)
  List all activity release information for a specific Game Center detail.
- [Get Activity Release IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-activityreleases.md)
  List all activity release IDs for a specific Game Center detail.
### Reading Game center challenge information
- [Get Challenge Releases for a Game Center Detail](get-v1-gamecenterdetails-_id_-challengereleases.md)
  List all challenge release information for a specific Game Center detail.
- [Read Challenge Release IDs for a Game Center Detail](get-v1-gamecenterdetails-_id_-relationships-challengereleases.md)
  List all the challenge release IDs for a specific Game Center detail.
### Objects
- [object GameCenterDetail](gamecenterdetail.md)
  The data structure that represents a Game Center detail resource.
- [object GameCenterDetailCreateRequest](gamecenterdetailcreaterequest.md)
  The request body you use to create a Game Center detail.
- [object GameCenterDetailGameCenterAchievementsV2LinkagesRequest](gamecenterdetailgamecenterachievementsv2linkagesrequest.md)
  The data structure that represents a Game Center detail Game Center achievement linkage request resource.
- [object GameCenterDetailGameCenterAchievementsV2LinkagesResponse](gamecenterdetailgamecenterachievementsv2linkagesresponse.md)
  A response that contains a list of Game Center detail Game Center achievement linkage resources.
- [object GameCenterDetailGameCenterLeaderboardSetsV2LinkagesRequest](gamecenterdetailgamecenterleaderboardsetsv2linkagesrequest.md)
  The data structure that represents a Game Center detail Game Center leaderboard set linkage request resource.
- [object GameCenterDetailGameCenterLeaderboardSetsV2LinkagesResponse](gamecenterdetailgamecenterleaderboardsetsv2linkagesresponse.md)
  A response that contains a list of Game Center detail Game Center leaderboard set linkage resources.
- [object GameCenterDetailGameCenterLeaderboardsV2LinkagesRequest](gamecenterdetailgamecenterleaderboardsv2linkagesrequest.md)
  The data structure that represents a Game Center detail Game Center leaderboard linkage request resource.
- [object GameCenterDetailGameCenterLeaderboardsV2LinkagesResponse](gamecenterdetailgamecenterleaderboardsv2linkagesresponse.md)
  A response that contains a list of Game Center detail Game Center leaderboard linkage resources.
- [object GameCenterDetailGameCenterAchievementsLinkagesRequest](gamecenterdetailgamecenterachievementslinkagesrequest.md)
  The request body you use to create a relationship between a Game Center detail and an achievement.
- [object GameCenterDetailGameCenterAchievementsLinkagesResponse](gamecenterdetailgamecenterachievementslinkagesresponse.md)
  A response that confirms a relationship between a Game Center detail and an achievement.
- [object GameCenterDetailGameCenterLeaderboardSetsLinkagesRequest](gamecenterdetailgamecenterleaderboardsetslinkagesrequest.md)
  The request body you use to create a relationship between a Game Center detail and a leaderboard set.
- [object GameCenterDetailGameCenterLeaderboardSetsLinkagesResponse](gamecenterdetailgamecenterleaderboardsetslinkagesresponse.md)
  A response that confirms a relationship between a Game Center detail and leaderboard set.
- [object GameCenterDetailGameCenterLeaderboardsLinkagesRequest](gamecenterdetailgamecenterleaderboardslinkagesrequest.md)
  The request body you use to create a relationship between a Game Center detail and a leaderboard.
- [object GameCenterDetailGameCenterLeaderboardsLinkagesResponse](gamecenterdetailgamecenterleaderboardslinkagesresponse.md)
  A response that confirms a relationship between a Game Center detail and a leaderboard.
- [object GameCenterDetailChallengesMinimumPlatformVersionsLinkagesRequest](gamecenterdetailchallengesminimumplatformversionslinkagesrequest.md)
  The data structure that represents a detail resource.
- [object GameCenterDetailResponse](gamecenterdetailresponse.md)
  A response that contains a single Game Center detail resource.
- [object GameCenterDetailUpdateRequest](gamecenterdetailupdaterequest.md)
  The request body you use to update a Game Center detail.
- [object GameCenterDetailsResponse](gamecenterdetailsresponse.md)
  A response that contains a list of Game Center detail resources.
- [object AppGameCenterDetailLinkageResponse](appgamecenterdetaillinkageresponse.md)
- [object GameCenterDetailAchievementReleasesLinkagesResponse](gamecenterdetailachievementreleaseslinkagesresponse.md)
- [object GameCenterDetailActivityReleasesLinkagesResponse](gamecenterdetailactivityreleaseslinkagesresponse.md)
- [object GameCenterDetailChallengeReleasesLinkagesResponse](gamecenterdetailchallengereleaseslinkagesresponse.md)
  A response that contains a list of IDs of related resources.
- [object GameCenterDetailGameCenterActivitiesLinkagesResponse](gamecenterdetailgamecenteractivitieslinkagesresponse.md)
- [object GameCenterDetailGameCenterAppVersionsLinkagesResponse](gamecenterdetailgamecenterappversionslinkagesresponse.md)
- [object GameCenterDetailGameCenterChallengesLinkagesResponse](gamecenterdetailgamecenterchallengeslinkagesresponse.md)
- [object GameCenterDetailGameCenterGroupLinkageResponse](gamecenterdetailgamecentergrouplinkageresponse.md)
- [object GameCenterDetailLeaderboardReleasesLinkagesResponse](gamecenterdetailleaderboardreleaseslinkagesresponse.md)
- [object GameCenterDetailLeaderboardSetReleasesLinkagesResponse](gamecenterdetailleaderboardsetreleaseslinkagesresponse.md)

## See Also

- [Game Center groups](game-center-groups.md)
  Manage groups between your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-details)*