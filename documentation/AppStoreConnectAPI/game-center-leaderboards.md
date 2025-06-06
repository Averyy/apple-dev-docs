# Game Center leaderboards

**Framework**: App Store Connect API

Create and manage leaderboards for your apps.

#### Overview

Use leaderboards in your games so players can compare their scores against other players in the same game. When you configure leaderboards in App Store Connect, you specify details such as the scores to collect and how to order them.

For more information about how to use leaderboards in your app, see [`Configure leaderboards`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/configure-leaderboards/).

## Topics

### Reading leaderboards
- [Read leaderboard information](get-v1-gamecenterleaderboards-_id_.md)
  Read information about a specific leaderboard.
- [Read group information for a leaderboard](get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List all localizations for a leaderboard](get-v1-gamecenterleaderboards-_id_-localizations.md)
  Get a list of localized metadata for a leaderboard.
- [List all groups to which a leaderboard belongs ](get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  List associated group leaderboards for a specific leaderboard.
- [List releases for a leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
### Creating, modifying, and deleting leaderboards
- [Create a leaderboard](post-v1-gamecenterleaderboards.md)
  Add a new leaderboard to your app.
- [Edit a leaderboard](patch-v1-gamecenterleaderboards-_id_.md)
  Modify the details of a leaderboard.
- [Edit the relationship between a leaderboard and a group leaderboard](patch-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  Modify the group leadboard to which a leaderboard belongs.
- [Delete a leaderboard](delete-v1-gamecenterleaderboards-_id_.md)
  Delete a leaderboard from your app.
### Objects
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

## See Also

- [Game Center leaderboard images](game-center-leaderboard-images.md)
  Read and manage image assets for Game Center leaderboards.
- [Game Center leaderboard releases](game-center-leaderboard-releases.md)
  Read, create, and delete Game Center leaderboards releases.
- [Game Center leaderboard localizations](game-center-leaderboard-localizations.md)
  Manage localizations for Game Center leaderboards.
- [Game Center leaderboards scores](game-center-leaderboards-scores.md)
  Create and modify Game Center leaderboards scores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-leaderboards)*