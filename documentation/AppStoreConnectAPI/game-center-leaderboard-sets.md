# Game Center leaderboard sets

**Framework**: App Store Connect API

Manage Game Center leaderboard sets for your apps.

#### Overview

Leaderboard sets organize several leaderboards into a single unit. For example, in a game that includes many levels, you might define a leaderboard set to organize the leaderboards for each level. A single app can have 100 leaderboard sets, and a set can have a maximum of 100 leaderboards. You must have at least one leaderboard for your app before you can create a leaderboard set. Once you add leaderboard sets to your app, all future leaderboards that you configure for the app must be included in a leaderboard set.

The process to start using leaderboard sets to organize your app’s leaderboards includes these steps:

- Create the first leaderboard set.
- Create additional leaderboard sets.
- Add new leaderboards directly into leaderboard sets.

For more information about how to use Leaderboard sets in your app, see [`Configure leaderboards sets`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/configure-leaderboard-sets).

## Topics

### Reading leaderboard sets
- [Read Game Center leaderboard set information](get-v2-gamecenterleaderboardsets-_id_.md)
  Get information about a specific Game Center leaderboard set.
- [List all leaderboards for a Game Center leaderboard set](get-v2-gamecenterleaderboardsets-_id_-gamecenterleaderboards.md)
  Get a list of leaderboards for a specific Game Center leaderboard set.
- [Get all leaderboard IDs for a Game Center leaderboard set](get-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Get a list of leaderboard resource IDs for a specific Game Center leaderboard set.
- [List all versions for a Game Center leaderboard set](get-v2-gamecenterleaderboardsets-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard set.
- [Get all version IDs for a Game Center leaderboard set](get-v2-gamecenterleaderboardsets-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard set.
- [Read leaderboard set information](get-v1-gamecenterleaderboardsets-_id_.md)
  Read information about a specific leaderboard set.
- [List leaderboard information for a leaderboard set](get-v1-gamecenterleaderboardsets-_id_-gamecenterleaderboards.md)
  Read the leadboards that belong to a learderboard set.
- [List leaderboard sets in a group leaderboard set](get-v1-gamecenterleaderboardsets-_id_-groupleaderboardset.md)
  List information about leaderboards and leaderboard sets in a group leaderboard set.
- [List all localizations for a leaderboard set](get-v1-gamecenterleaderboardsets-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard set.
- [GET /v1/gameCenterLeaderboardSets/{id}/relationships/localizations](get-v1-gamecenterleaderboardsets-_id_-relationships-localizations.md)
- [Read the leaderboards in a leaderboard set](get-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  List all leaderboards in a leaderboard set.
- [Read the group leaderboard set in a leaderboard set](get-v1-gamecenterleaderboardsets-_id_-relationships-groupleaderboardset.md)
  List all the group leaderboard sets in a leaderboard set.
- [List releases for a leaderboard set](get-v1-gamecenterleaderboardsets-_id_-releases.md)
  Read the state of releases for a leaderboard set and related information.
- [GET /v1/gameCenterLeaderboardSets/{id}/relationships/releases](get-v1-gamecenterleaderboardsets-_id_-relationships-releases.md)
### Creating, editing, and deleting leaderboard sets
- [Create a Game Center leaderboard set](post-v2-gamecenterleaderboardsets.md)
  Create a Game Center leaderboard set.
- [Add a leaderboard to a Game Center leaderboard set](post-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Add a leaderboard to a Game Center leaderboard set.
- [Modify a Game Center leaderboard set](patch-v2-gamecenterleaderboardsets-_id_.md)
  Update a specific Game Center leaderboard set.
- [Modify the leaderboards for a Game Center leaderboard set](patch-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Update the leaderboards relationship for a specific Game Center leaderboard set.
- [Delete a Game Center leaderboard set](delete-v2-gamecenterleaderboardsets-_id_.md)
  Delete a specific Game Center leaderboard set.
- [Delete a Game Center leaderboard set](delete-v2-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Delete a specific Game Center leaderboard set.
- [Create a leaderboard set](post-v1-gamecenterleaderboardsets.md)
  Add a new leaderboard set to your app.
- [Create a relationship between a leaderboard and a leaderboard set](post-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Add a leaderboard to a leaderboard set.
- [Edit a leaderboard set](patch-v1-gamecenterleaderboardsets-_id_.md)
  Modify the metadata for a leaderboard set.
- [Modify the leaderboards in leaderboard set](patch-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Edit the positions of leaderboards in an existing leaderboard set.
- [Edit the releationship between a leaderboard and a group leaderboard](patch-v1-gamecenterleaderboardsets-_id_-relationships-groupleaderboardset.md)
  Modify the group leaderboards in a leaderboard set.
- [Delete a leaderboard set](delete-v1-gamecenterleaderboardsets-_id_.md)
  Delete a specifc leaderboard set.
- [Delete the relationship between a leaderboard and a leaderboard set](delete-v1-gamecenterleaderboardsets-_id_-relationships-gamecenterleaderboards.md)
  Remove a leaderboard from a leaderboard set.
### Objects
- [object GameCenterLeaderboardSetV2](gamecenterleaderboardsetv2.md)
  The data structure that represents a Game Center leaderboard set v2 resource.
- [object GameCenterLeaderboardSetV2CreateRequest](gamecenterleaderboardsetv2createrequest.md)
  The request body you use to create a Game Center leaderboard set v2.
- [object GameCenterLeaderboardSetV2Response](gamecenterleaderboardsetv2response.md)
  A response that contains a single Game Center leaderboard set v2 resource.
- [object GameCenterLeaderboardSetV2UpdateRequest](gamecenterleaderboardsetv2updaterequest.md)
  The request body you use to update a Game Center leaderboard set v2.
- [object GameCenterLeaderboardSetsV2Response](gamecenterleaderboardsetsv2response.md)
  A response that contains a single Game Center leaderboard set v2 resource.
- [object GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesRequest](gamecenterleaderboardsetv2gamecenterleaderboardslinkagesrequest.md)
  The data structure that represents a Game Center leaderboard set v2 Game Center leaderboard linkage request resource.
- [object GameCenterLeaderboardSetV2GameCenterLeaderboardsLinkagesResponse](gamecenterleaderboardsetv2gamecenterleaderboardslinkagesresponse.md)
  A response that contains a list of Game Center leaderboard set v2 Game Center leaderboard linkage resources.
- [object GameCenterLeaderboardSetV2VersionsLinkagesResponse](gamecenterleaderboardsetv2versionslinkagesresponse.md)
  A response that contains a list of Game Center leaderboard set v2 version linkage resources.
- [object GameCenterLeaderboardSet](gamecenterleaderboardset.md)
  The data structure that represent a leaderboard set resource.
- [object GameCenterLeaderboardSetCreateRequest](gamecenterleaderboardsetcreaterequest.md)
  The request body you use to create a leaderboard set.
- [object GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesRequest](gamecenterleaderboardsetgamecenterleaderboardslinkagesrequest.md)
  The request body you use to create a relationship between a leaderboard set and a leaderboard.
- [object GameCenterLeaderboardSetGameCenterLeaderboardsLinkagesResponse](gamecenterleaderboardsetgamecenterleaderboardslinkagesresponse.md)
  A response that confirms a relationship between a leaderboard set and a leaderboard.
- [object GameCenterLeaderboardSetGroupLeaderboardSetLinkageRequest](gamecenterleaderboardsetgroupleaderboardsetlinkagerequest.md)
  The request body you use to create a relationship between a leaderboard set and a group leaderboard set.
- [object GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse](gamecenterleaderboardsetgroupleaderboardsetlinkageresponse.md)
  A response that confirms a relationship between a leaderboard set and a group leaderboard set.
- [object GameCenterLeaderboardSetResponse](gamecenterleaderboardsetresponse.md)
  A response that contains a single leaderboard set resource.
- [object GameCenterLeaderboardSetUpdateRequest](gamecenterleaderboardsetupdaterequest.md)
  The request body you use to update a leaderboard set.
- [object GameCenterLeaderboardSetsResponse](gamecenterleaderboardsetsresponse.md)
  A response that contains multiple leaderboard set resources.
- [object GameCenterLeaderboardSetLocalizationGameCenterLeaderboardSetImageLinkageResponse](gamecenterleaderboardsetlocalizationgamecenterleaderboardsetimagelinkageresponse.md)
- [object GameCenterLeaderboardSetLocalizationsLinkagesResponse](gamecenterleaderboardsetlocalizationslinkagesresponse.md)

## See Also

- [Game Center leaderboard set localizations](game-center-leaderboard-set-localizations.md)
  Manage localizations for your Game Center leaderboard sets.
- [Game Center leaderboard set images](game-center-leaderboard-set-images.md)
  Manage image assets for your Game Center leaderboard sets.
- [Game Center leaderboard set versions](game-center-leaderboard-set-versions.md)
  Manage versions for your Game Center leaderboard sets.
- [Game Center leaderboard set releases](game-center-leaderboard-set-releases.md)
  Manage a leaderboard set releases.
- [Game Center leaderboard set member localizations](game-center-leaderboard-set-member-localizations.md)
  Manage Game Center leaderboard set member localizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-leaderboard-sets)*