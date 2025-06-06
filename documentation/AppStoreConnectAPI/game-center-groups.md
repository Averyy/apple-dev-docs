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
- [List the achievements in a group](get-v1-gamecentergroups-_id_-gamecenterachievements.md)
  List achievements information for a specific group.
- [List Game Center details for a group](get-v1-gamecentergroups-_id_-gamecenterdetails.md)
  Read Game Center detail information for a specific group.
- [List Game Center leaderboard sets in a group](get-v1-gamecentergroups-_id_-gamecenterleaderboardsets.md)
  Read Game Center leaderboard sets information for a specific group.
- [List Game Center leaderboards for a group](get-v1-gamecentergroups-_id_-gamecenterleaderboards.md)
  Read Game Center leaderboard information for a specific group.
### Reading and modifying group relationships
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

## See Also

- [Game Center details](game-center-details.md)
  Manage enablement, achievement, leaderboard, and localization details for your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-groups)*