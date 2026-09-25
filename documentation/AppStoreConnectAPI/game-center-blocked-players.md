# Game Center blocked players

**Framework**: App Store Connect API

Block and unblock the Game Center players who can play your game.

#### Overview

Blocked players represent the Game Center players you block from playing a game. Blocking a player prevents that player from playing the game the Game Center detail belongs to, and unblocking reinstates access. Use this resource to:

- Read the players you block for a game.
- Block or unblock a player for a game.

> 💡 **Tip**:  These endpoints require information from GameKit, specifically [`gamePlayerID`](https://developer.apple.com/documentation/gamekit/gkplayer/gameplayerid).

A [`GameCenterDetailPlayer`](gamecenterdetailplayer.md) uses the player’s game-scoped ID as its resource ID.

For the equivalent workflow in App Store Connect, see [`Manage scores and players`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/manage-scores-and-players/).

## Topics

### Reading blocked players
- [List Blocked Players](get-v1-gamecenterdetails-_id_-blockedplayers.md)
  List the blocked players for a game.
- [List Blocked Player IDs](get-v1-gamecenterdetails-_id_-relationships-blockedplayers.md)
  List the blocked player IDs for a Game Center detail.
### Blocking and unblocking players
- [Modify a Game Center Detail Player](patch-v1-gamecenterdetailplayers-_id_.md)
  Block or unblock a player for a game.
### Objects
- [object GameCenterDetailPlayer](gamecenterdetailplayer.md)
  A Game Center player tied to a single game, whom you can block from playing that game.
- [object GameCenterDetailPlayerResponse](gamecenterdetailplayerresponse.md)
  The response body for endpoints that modify a Game Center player in an app’s Game Center configuration.
- [object GameCenterDetailPlayerUpdateRequest](gamecenterdetailplayerupdaterequest.md)
  The request body you use to update a Game Center detail player.
- [object GameCenterDetailPlayersResponse](gamecenterdetailplayersresponse.md)
  The response body for endpoints that list the blocked players for a game.
- [object GameCenterDetailBlockedPlayersLinkagesResponse](gamecenterdetailblockedplayerslinkagesresponse.md)
  The response body for endpoints that list the blocked player IDs related to a Game Center detail.

## See Also

- [Game Center details](game-center-details.md)
  Manage enablement, achievement, leaderboard, and localization details for your apps.
- [Game Center groups](game-center-groups.md)
  Manage groups between your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-blocked-players)*