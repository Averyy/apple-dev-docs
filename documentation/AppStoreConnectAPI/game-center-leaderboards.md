# Game Center leaderboards

**Framework**: App Store Connect API

Create and manage leaderboards for your apps.

#### Overview

Use leaderboards in your games so players can compare their scores against other players in the same game. When you configure leaderboards in App Store Connect, you specify details such as the scores to collect and how to order them.

For more information about how to use leaderboards in your app, see [`Configure leaderboards`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/configure-leaderboards/).

## Topics

### Reading leaderboards
- [Read Game Center leaderboard information](get-v2-gamecenterleaderboards-_id_.md)
  Get information about a specific Game Center leaderboard.
- [List all versions for a Game Center leaderboard](get-v2-gamecenterleaderboards-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard.
- [Get all version IDs for a Game Center leaderboard](get-v2-gamecenterleaderboards-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard.
- [Read leaderboard information](get-v1-gamecenterleaderboards-_id_.md)
  Read information about a specific leaderboard.
- [Read group information for a leaderboard](get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List all localizations for a leaderboard](get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/localizations](get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [List all groups to which a leaderboard belongs ](get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  List associated group leaderboards for a specific leaderboard.
- [List releases for a leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [GET /v1/gameCenterLeaderboards/{id}/relationships/releases](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)
### Creating, modifying, and deleting leaderboards
- [Create a Game Center leaderboard](post-v2-gamecenterleaderboards.md)
  Create a Game Center leaderboard.
- [Modify a Game Center leaderboard](patch-v2-gamecenterleaderboards-_id_.md)
  Update a specific Game Center leaderboard.
- [Modify the activity for a Game Center leaderboard](patch-v2-gamecenterleaderboards-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center leaderboard.
- [Modify the challenge for a Game Center leaderboard](patch-v2-gamecenterleaderboards-_id_-relationships-challenge.md)
  Update the challenge relationship for a specific Game Center leaderboard.
- [Delete a Game Center leaderboard](delete-v2-gamecenterleaderboards-_id_.md)
  Delete a specific Game Center leaderboard.
- [Create a leaderboard](post-v1-gamecenterleaderboards.md)
  Add a new leaderboard to your app.
- [Edit a leaderboard](patch-v1-gamecenterleaderboards-_id_.md)
  Modify the details of a leaderboard.
- [Edit the relationship between a leaderboard and a group leaderboard](patch-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  Modify the group leadboard to which a leaderboard belongs.
- [PATCH /v1/gameCenterLeaderboards/{id}/relationships/activity](patch-v1-gamecenterleaderboards-_id_-relationships-activity.md)
- [PATCH /v1/gameCenterLeaderboards/{id}/relationships/challenge](patch-v1-gamecenterleaderboards-_id_-relationships-challenge.md)
- [Delete a leaderboard](delete-v1-gamecenterleaderboards-_id_.md)
  Delete a leaderboard from your app.
### Objects and types
- [object GameCenterLeaderboardV2](gamecenterleaderboardv2.md)
  The data structure that represents a Game Center leaderboard v2 resource.
- [object GameCenterLeaderboardV2CreateRequest](gamecenterleaderboardv2createrequest.md)
  The request body you use to create a Game Center leaderboard v2.
- [object GameCenterLeaderboardV2Response](gamecenterleaderboardv2response.md)
  A response that contains a single Game Center leaderboard v2 resource.
- [object GameCenterLeaderboardV2UpdateRequest](gamecenterleaderboardv2updaterequest.md)
  The request body you use to update a Game Center leaderboard v2.
- [object GameCenterLeaderboardsV2Response](gamecenterleaderboardsv2response.md)
  A response that contains a list of Game Center leaderboard resources.
- [object GameCenterLeaderboardV2ActivityLinkageRequest](gamecenterleaderboardv2activitylinkagerequest.md)
  The data structure that represents a Game Center leaderboard v2 activity linkage request resource.
- [object GameCenterLeaderboardV2ChallengeLinkageRequest](gamecenterleaderboardv2challengelinkagerequest.md)
  The data structure that represents a Game Center leaderboard v2 challenge linkage request resource.
- [object GameCenterLeaderboardV2VersionsLinkagesResponse](gamecenterleaderboardv2versionslinkagesresponse.md)
  A response that contains a list of Game Center leaderboard v2 version linkage resources.
- [object GameCenterLeaderboardUpdateRequest](gamecenterleaderboardupdaterequest.md)
  The request body you use to update a leaderboard.
- [object GameCenterLeaderboardsResponse](gamecenterleaderboardsresponse.md)
  A response that contains multiple leaderboard resources.
- [object GameCenterLeaderboard](gamecenterleaderboard.md)
  The data structure that represent a leaderboard resource.
- [object GameCenterLeaderboardCreateRequest](gamecenterleaderboardcreaterequest.md)
  The request body you use to create a leaderboard.
- [object GameCenterLeaderboardResponse](gamecenterleaderboardresponse.md)
  A response that contains a single leaderboard image resource.
- [object GameCenterLeaderboardGroupLeaderboardLinkageRequest](gamecenterleaderboardgroupleaderboardlinkagerequest.md)
  The request body you use to attach an individual leaderbaord to a group leaderboard.
- [object GameCenterLeaderboardGroupLeaderboardLinkageResponse](gamecenterleaderboardgroupleaderboardlinkageresponse.md)
  A response confriming a relationship between a leaderboard and group leaderboard.
- [object GameCenterLeaderboardActivityLinkageRequest](gamecenterleaderboardactivitylinkagerequest.md)
- [object GameCenterLeaderboardChallengeLinkageRequest](gamecenterleaderboardchallengelinkagerequest.md)
- [type GameCenterLeaderboardFormatter](gamecenterleaderboardformatter.md)
  The values you can select to describe the format of a leaderboard.
- [object StringToStringMap](stringtostringmap.md)

## See Also

- [Game Center leaderboard images](game-center-leaderboard-images.md)
  Read and manage image assets for Game Center leaderboards.
- [Game Center leaderboard localizations](game-center-leaderboard-localizations.md)
  Manage localizations for Game Center leaderboards.
- [Game Center leaderboard versions](game-center-leaderboard-versions.md)
  Manage versions for your Game Center leaderboards.
- [Game Center leaderboard releases](game-center-leaderboard-releases.md)
  Read, create, and delete Game Center leaderboards releases.
- [Game Center leaderboards scores](game-center-leaderboards-scores.md)
  Create and modify Game Center leaderboards scores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-leaderboards)*