# Game Center groups

**Framework**: App Store Connect API

Manage groups between your apps.

#### Overview

Use groups to connect multiple apps so they use common Game Center elements including: achievements, Game Center details, leaderboards, and leaderboard sets.

Use this resource to:

- Create and modify Game Center groups.
- Read and modify relationships between a Game Center group and achievements, Game Center details, leaderboards, and leaderboard sets.

## Topics

### Managing groups
- [Read group information](get-v1-gamecentergroups.md)
  List information for all groups.
- [Read group information for a specific group](get-v1-gamecentergroups-_id_.md)
  Read information for a specific group.
- [Create a group](post-v1-gamecentergroups.md)
  Add a new group.
- [Modify a group](patch-v1-gamecentergroups-_id_.md)
  Edit the reference name for a group.
- [Delete a group](delete-v1-gamecentergroups-_id_.md)
  Remove a group.
- [List all Game Center achievements for a Game Center group](get-v1-gamecentergroups-_id_-gamecenterachievementsv2.md)
  Get a list of achievements for a specific Game Center group.
- [List all Game Center leaderboard sets for a Game Center group](get-v1-gamecentergroups-_id_-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard sets for a specific Game Center group.
- [List all Game Center leaderboards for a Game Center group](get-v1-gamecentergroups-_id_-gamecenterleaderboardsv2.md)
  Get a list of leaderboards for a specific Game Center group.
- [List the achievements in a group](get-v1-gamecentergroups-_id_-gamecenterachievements.md)
  List achievements information for a specific group.
- [List Game Center details for a group](get-v1-gamecentergroups-_id_-gamecenterdetails.md)
  Read Game Center detail information for a specific group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterDetails](get-v1-gamecentergroups-_id_-relationships-gamecenterdetails.md)
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterDetails](get-v1-gamecentergroups-_id_-relationships-gamecenterdetails.md)
- [List Game Center leaderboard sets in a group](get-v1-gamecentergroups-_id_-gamecenterleaderboardsets.md)
  Read Game Center leaderboard sets information for a specific group.
- [List Game Center leaderboards for a group](get-v1-gamecentergroups-_id_-gamecenterleaderboards.md)
  Read Game Center leaderboard information for a specific group.
- [List all activities for a Game Center group](get-v1-gamecentergroups-_id_-gamecenteractivities.md)
  Get a list of all activities for a Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterActivities](get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
- [Read the challenges for a Game Center group](get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [GET /v1/gameCenterGroups/{id}/relationships/gameCenterChallenges](get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)
### Reading and modifying group relationships
- [Get all achievement IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenterachievementsv2.md)
  Get a list of achievement resource IDs for a specific Game Center group.
- [Get all leaderboard set IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Get a list of leaderboard set resource IDs for a specific Game Center group.
- [Get all leaderboard IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenterleaderboardsv2.md)
  Get a list of leaderboard resource IDs for a specific Game Center group.
- [Modify the achievements for a Game Center group](patch-v1-gamecentergroups-_id_-relationships-gamecenterachievementsv2.md)
  Update the achievements relationship for a specific Game Center group.
- [Modify the leaderboard sets for a Game Center group](patch-v1-gamecentergroups-_id_-relationships-gamecenterleaderboardsetsv2.md)
  Update the leaderboard sets relationship for a specific Game Center group.
- [Modify the leaderboards for a Game Center group](patch-v1-gamecentergroups-_id_-relationships-gamecenterleaderboardsv2.md)
  Update the leaderboards relationship for a specific Game Center group.
- [Read the achievements in a group](get-v1-gamecentergroups-_id_-relationships-gamecenterachievements.md)
  List all the achievements associated with a specific group.
- [Read the leaderboard sets in a group](get-v1-gamecentergroups-_id_-relationships-gamecenterleaderboardsets.md)
  List all the leaderboard sets associated with a specific group.
- [Read the leaderboards in a group](get-v1-gamecentergroups-_id_-relationships-gamecenterleaderboards.md)
  List all the leaderboard associated with a specific group.
- [Edit the achievements associated with a group](patch-v1-gamecentergroups-_id_-relationships-gamecenterachievements.md)
  Modify the achievements in a specific group.
- [Edit the leaderboard sets associated with a group](patch-v1-gamecentergroups-_id_-relationships-gamecenterleaderboardsets.md)
  Modify the leaderboard sets in a specific group.
- [Edit the leaderboard associated with a group](patch-v1-gamecentergroups-_id_-relationships-gamecenterleaderboards.md)
  Modify the Game Center leaderboards in a specific group.
### Objects
- [object GameCenterGroup](gamecentergroup.md)
  The data structure that represents a group resource.
- [object GameCenterGroupCreateRequest](gamecentergroupcreaterequest.md)
  The request body you use to create a group.
- [object GameCenterGroupGameCenterAchievementsV2LinkagesRequest](gamecentergroupgamecenterachievementsv2linkagesrequest.md)
  The data structure that represents a Game Center group Game Center achievement linkage request resource.
- [object GameCenterGroupGameCenterAchievementsV2LinkagesResponse](gamecentergroupgamecenterachievementsv2linkagesresponse.md)
  A response that contains a list of Game Center group Game Center achievement linkage resources.
- [object GameCenterGroupGameCenterLeaderboardSetsV2LinkagesRequest](gamecentergroupgamecenterleaderboardsetsv2linkagesrequest.md)
  The data structure that represents a Game Center group Game Center leaderboard set linkage request resource.
- [object GameCenterGroupGameCenterLeaderboardSetsV2LinkagesResponse](gamecentergroupgamecenterleaderboardsetsv2linkagesresponse.md)
  A response that contains a list of Game Center group Game Center leaderboard set linkage resources.
- [object GameCenterGroupGameCenterLeaderboardsV2LinkagesRequest](gamecentergroupgamecenterleaderboardsv2linkagesrequest.md)
  The data structure that represents a Game Center group Game Center leaderboard linkage request resource.
- [object GameCenterGroupGameCenterLeaderboardsV2LinkagesResponse](gamecentergroupgamecenterleaderboardsv2linkagesresponse.md)
  A response that contains a list of Game Center group Game Center leaderboard linkage resources.
- [object GameCenterGroupGameCenterAchievementsLinkagesRequest](gamecentergroupgamecenterachievementslinkagesrequest.md)
  The request body you use to create a relationship between a group and an achievement.
- [object GameCenterGroupGameCenterAchievementsLinkagesResponse](gamecentergroupgamecenterachievementslinkagesresponse.md)
  A response that confirms a relationship between a group and an achievement.
- [object GameCenterGroupGameCenterLeaderboardSetsLinkagesRequest](gamecentergroupgamecenterleaderboardsetslinkagesrequest.md)
  The request body you use to create a relationship between a group and a leaderboard set.
- [object GameCenterGroupGameCenterLeaderboardSetsLinkagesResponse](gamecentergroupgamecenterleaderboardsetslinkagesresponse.md)
  A response that confirms a relationship between a group and leaderboard set.
- [object GameCenterGroupGameCenterLeaderboardsLinkagesRequest](gamecentergroupgamecenterleaderboardslinkagesrequest.md)
  The request body you use to create a relationship between a group and a leaderboard.
- [object GameCenterGroupGameCenterLeaderboardsLinkagesResponse](gamecentergroupgamecenterleaderboardslinkagesresponse.md)
  A response that confirms a relationship between a group and a leaderboard.
- [object GameCenterGroupResponse](gamecentergroupresponse.md)
  A response that contains a single group resource.
- [object GameCenterGroupUpdateRequest](gamecentergroupupdaterequest.md)
  The request body you use to update a group.
- [object GameCenterGroupsResponse](gamecentergroupsresponse.md)
  A response that contains one or more groups.
- [object GameCenterGroupGameCenterActivitiesLinkagesResponse](gamecentergroupgamecenteractivitieslinkagesresponse.md)
- [object GameCenterGroupGameCenterChallengesLinkagesResponse](gamecentergroupgamecenterchallengeslinkagesresponse.md)
- [object GameCenterGroupGameCenterDetailsLinkagesResponse](gamecentergroupgamecenterdetailslinkagesresponse.md)

## See Also

- [Game Center details](game-center-details.md)
  Manage enablement, achievement, leaderboard, and localization details for your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-groups)*