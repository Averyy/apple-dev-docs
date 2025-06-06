# Game Center details

**Framework**: App Store Connect API

Manage enablement, achievement, leaderboard, and localization details for your apps.

#### Overview

Game Center details is the top-level endpoint for Game Center information for your apps. Use this resource to:

- Enable Game Center for an app.
- Read information about specific types of Game Center data, including achievements, leaderboards, and localizations.

To enable Game Center, begin by calling [`Enable Game Center for an app`](post-v1-gamecenterdetails.md). Then you can create and configure achievements, leaderboards, leaderboard sets, and more.

## Topics

### Reading Game Center details
- [Read the state of Game Center for an app](get-v1-apps-_id_-gamecenterdetail.md)
  Get Game Center detail information for an app.
- [Read Game Center details](get-v1-gamecenterdetails-_id_.md)
  Read a specific Game Center detail and related information.
- [Read app versions for a Game Center detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [Read the groups in a Game Center detail](get-v1-gamecenterdetails-_id_-gamecentergroup.md)
  Get a list of groups in a Game Center detail.
### Creating and editing Game Center details
- [Enable Game Center for an app](post-v1-gamecenterdetails.md)
  Create a Game Center detail for an app.
- [Modify a Game Center detail for an app](patch-v1-gamecenterdetails-_id_.md)
  Edit challenge state, default leaderboards, and groups.
- [Modify the associated leaderboard sets for a Game Center detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  Edit the associated leaderboard sets for a Game Center detail.
- [Modify the associated leaderboards for a Game Center detail](patch-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  Edit the associated leaderboards for a Game Center detail.
### Reading and editing Game Center detail achievements
- [List all achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [List achievement releases ](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievements](get-v1-gamecenterdetails-_id_-relationships-gamecenterachievements.md)
  List the achievements for a Game center detail.
- [Modify associated achievements](patch-v1-gamecenterdetails-_id_-relationships-gamecenterachievements.md)
  Modify the achievements for a Game center detail.
### Reading and editing Game Center detail leaderboards
- [Read leaderboard releases](get-v1-gamecenterdetails-_id_-leaderboardreleases.md)
  List all leaderboard releases for a Game Center detail.
- [Read leaderboard information](get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md)
  Get all leaderboards and related information for a Game Center detail.
- [List leaderboards](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md)
  ​List all leaderboards for a Game Center detail.
### Reading and editing leaderboard sets in a Game Center detail
- [Read leaderboard set information](get-v1-gamecenterdetails-_id_-gamecenterleaderboardsets.md)
  Get all leaderboard sets and related information for a Game Center detail.
- [List leaderboard sets](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboardsets.md)
  List all leaderboards for a Game Center detail.
- [Read leaderboard set release information](get-v1-gamecenterdetails-_id_-leaderboardsetreleases.md)
  List all leaderboard set releases for a Game Center detail.
### Objects
- [object GameCenterDetail](gamecenterdetail.md)
  The data structure that represents a Game Center detail resource.
- [object GameCenterDetailCreateRequest](gamecenterdetailcreaterequest.md)
  The request body you use to create a Game Center detail.
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
- [object GameCenterDetailResponse](gamecenterdetailresponse.md)
  A response that contains a single Game Center detail resource.
- [object GameCenterDetailUpdateRequest](gamecenterdetailupdaterequest.md)
  The request body you use to update a Game Center detail.
- [object GameCenterDetailsResponse](gamecenterdetailsresponse.md)
  A response that contains a list of Game Center detail resources.

## See Also

- [Game Center groups](game-center-groups.md)
  Manage groups between your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-details)*